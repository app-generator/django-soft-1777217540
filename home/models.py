# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Personnes(models.Model):

    #__Personnes_FIELDS__
    sexe = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    long_nom = models.IntegerField(null=True, blank=True)
    nbre_prenoms = models.IntegerField(null=True, blank=True)
    db_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    db_code_dpt = models.TextField(max_length=255, null=True, blank=True)
    db_pays = models.TextField(max_length=255, null=True, blank=True)
    db_continent = models.TextField(max_length=255, null=True, blank=True)
    dd_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    dd_code_dpt = models.TextField(max_length=255, null=True, blank=True)
    dd_pays = models.TextField(max_length=255, null=True, blank=True)
    dd_continent = models.TextField(max_length=255, null=True, blank=True)
    distance = models.IntegerField(null=True, blank=True)

    #__Personnes_FIELDS__END

    class Meta:
        verbose_name        = _("Personnes")
        verbose_name_plural = _("Personnes")



#__MODELS__END
