from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views import static
from rest_framework import routers

from catalog.branches.views import BranchViewSet
from catalog.personnels.views import PersonnelViewSet

router = routers.DefaultRouter()
router.register(r'personnels', PersonnelViewSet)
router.register(r'branches', BranchViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': False})
]
