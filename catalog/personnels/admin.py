from django.contrib import admin
from django import forms

# Register your models here.
from catalog.personnels.models import Personnel


class PersonnelAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'position')
    search_fields = ['first_name', 'last_name']

    class form(forms.ModelForm):
        class Meta:
            widgets = {}


admin.site.register(Personnel, PersonnelAdmin)

