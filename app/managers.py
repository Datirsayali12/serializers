from django.db import models


class CustomManager(models.Manager):
    def get_name(self,name):
        return super().get_queryset().filter(name__icontains=name)