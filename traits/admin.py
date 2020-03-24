from django.contrib import admin

# Register your models here.

from .models import Trait

class TraitAdmin(admin.ModelAdmin):
    class Meta:
	    model = Trait

admin.site.register(Trait,TraitAdmin)