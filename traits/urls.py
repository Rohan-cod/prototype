from django.urls import path

from .views import TraitListView, MyTraitListView, TraitCreateView, HomePageView, TraitDeleteView, TraitUpdateView, TraitDetailView, search_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('trait/', TraitListView.as_view(), name='trait_list'),
    path('mytrait/', MyTraitListView.as_view(), name='my_trait_list'),
    path('new/', TraitCreateView.as_view(), name='trait_new'),
    path('<int:pk>/',
         TraitDetailView.as_view(), name='trait_detail'),
    path('<int:pk>/delete/',
         TraitDeleteView.as_view(), name='trait_delete'),
    path('<int:pk>/edit/',
         TraitUpdateView.as_view(), name='trait_edit'),
    path('search/', search_view, name='search'),
]