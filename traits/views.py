from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, TemplateView, DetailView
from .models import Trait 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TraitForm
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render



class TraitListView(LoginRequiredMixin, ListView):
	model = Trait
	template_name = 'traits.html'
	login_url = 'login'
	paginate_by = 5

class MyTraitListView(LoginRequiredMixin, ListView):
	model = Trait
	template_name = 'my_traits.html'
	login_url = 'login'
	paginate_by = 5

class TraitCreateView(LoginRequiredMixin, CreateView):
	model = Trait
	template_name = 'trait_new.html'
	form_class = TraitForm
	success_url = reverse_lazy('trait_list')
	login_url = 'login'

	def form_valid(self, form):
		form.instance.curator = self.request.user
		return super().form_valid(form)

class HomePageView(TemplateView):
	template_name = 'index.html'

class TraitUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Trait
	form_class = TraitForm
	template_name = 'trait_edit.html'
	success_url = reverse_lazy('trait_list')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.curator == self.request.user

class TraitDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Trait
	template_name = 'trait_delete.html'
	success_url = reverse_lazy('trait_list')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.curator == self.request.user

class TraitDetailView(LoginRequiredMixin, DetailView):
	model = Trait
	template_name = 'trait_detail.html'
	login_url = 'login'

def search_view(request):
	ctx = {}
	url_parameter = request.GET.get("q")

	if url_parameter:
		traits = Trait.objects.filter(title__icontains=url_parameter)
	else:
		traits = Trait.objects.all()

	ctx["traits"] = traits

	if request.is_ajax():
		html = render_to_string(
			template_name="traits-results-partial.html", 
			context={"traits": traits}
		)

		data_dict = {"html_from_view": html}

		return JsonResponse(data=data_dict, safe=False)

	return render(request, "trait_search.html", context=ctx)





