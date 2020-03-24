from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


class Trait(models.Model):
	title = models.CharField(max_length=120)
	is_mapped = models.BooleanField()
	mapped_to_url = models.CharField(max_length=500, default='Not yet mapped')
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now_add=True)

	curator = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
		)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('trait_detail', args=[str(self.id)])



class Reviews(models.Model):
	trait = models.ForeignKey(Trait, on_delete=models.CASCADE)
	review = models.CharField(max_length=200)
	curator = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)

	def __str__(self):
		return self.review

	def get_absolute_url(self):
		return reverse('trait_list')