from django.db import models
from django.utils.translation import ugettext_lazy as _


class Personnel(models.Model):
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    position = models.CharField(_('position'), max_length=30, blank=True)

    REQUIRED_FIELDS = []

    objects = models.Manager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('personnel')
        verbose_name_plural = _('personnels')
