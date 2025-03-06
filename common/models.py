from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class AbsCreated(models.Model):
    """
    Модель, помогающая отследить дату создания и изменения объекта.
    """
    
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        abstract = True

class AbsActive(models.Model):
    """
    Модель, помогающая отследить активность объекта.
    """

    is_active = models.BooleanField('Активность', default=True)

    class Meta:
        abstract = True