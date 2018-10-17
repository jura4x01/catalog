from django.contrib.gis import admin

from catalog.branches.models import Branch
from catalog.settings import STATIC_URL


@admin.register(Branch)
class BranchAdmin(admin.GeoModelAdmin):

    extra_js = [
        '//code.jquery.com/jquery-1.11.0.min.js',
        f'{STATIC_URL}js/geo_binding.js'
    ]

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if request.user.has_perm('branches.change_coordinates'):
            self.fields = ('name', 'personnels', 'latitude', 'longitude', 'point', 'facade', 'image_tag')
            self.readonly_fields = ('image_tag',)
        else:
            self.fields = ('name', 'personnels', 'latitude', 'longitude', 'facade', 'image_tag')
            self.readonly_fields = ('image_tag', 'latitude', 'longitude')
        return super().change_view(request, object_id, form_url, extra_context)
