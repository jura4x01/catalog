from django.contrib.gis.geos import Point
from django.db import models
from django.contrib.gis.db import models as gmodels
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from catalog import settings
from catalog.personnels.models import Personnel


class Branch(models.Model):
    name = models.CharField(_('branch name'), max_length=30, blank=True)
    facade = models.ImageField(upload_to='facades/', null=True, blank=True)
    latitude = models.DecimalField(max_digits=16, decimal_places=14, null=True, blank=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=14, null=True, blank=True)
    point = gmodels.PointField(
        null=True, blank=True, help_text="Example: SRID=4326;POINT (76.56249397744735 52.91331451667325)")

    personnels = models.ManyToManyField(
        Personnel,
        verbose_name=_('personnels'),
        blank=True,
        help_text=_(
            'Personnels, registered in this branch.'
        ),
        related_name="branch_set",
        related_query_name="branch",
    )
    REQUIRED_FIELDS = []

    objects = models.Manager()

    def image_tag(self):
        return mark_safe(f'<img src="{settings.MEDIA_URL}{self.facade}" height=100 />')

    image_tag.short_description = 'Facade image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.point:
            self.latitude = self.point.y
            self.longitude = self.point.x
        elif self.latitude and self.longitude:
            self.point = Point((self.longitude, self.latitude))
        super(Branch, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('branch')
        verbose_name_plural = _('branches')
        permissions = (
            ("change_coordinates", "Can change coordinates"),
        )
