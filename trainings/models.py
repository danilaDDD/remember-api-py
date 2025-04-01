from django.db import models

from common.models import AbsCreated


# Create your models here.
class Training(AbsCreated):
    limit = models.PositiveIntegerField(verbose_name='Максимальное количество карточек')
    account = models.ForeignKey('account.Account', verbose_name='Пользователь',
                                related_name='trainings', blank=True, null=True,
                                on_delete=models.SET_NULL)
    remember_count = models.PositiveIntegerField(verbose_name='Количество повторений на сегодня')
    