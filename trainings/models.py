from django.db import models

from common.models import AbsCreated, AbsActive


# Create your models here.
class Training(AbsCreated, AbsActive):
    limit = models.PositiveIntegerField(verbose_name='Максимальное количество карточек')
    account = models.ForeignKey('account.Account', verbose_name='Пользователь',
                                related_name='trainings', blank=True, null=True,
                                on_delete=models.SET_NULL)
    remember_count = models.PositiveIntegerField(verbose_name='Количество повторений на сегодня')

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'


class RememberItem(AbsCreated, AbsActive):
    training = models.ForeignKey(Training, verbose_name='Тренировка',
                                 related_name='items', on_delete=models.CASCADE)
    remember = models.ForeignKey('infocard.Remember', verbose_name='Повторение',
                                 related_name='training_items', on_delete=models.CASCADE)
    index = models.PositiveIntegerField('Индекс', default=0, db_index=True)

    class Meta:
        verbose_name = 'Повторение'
        verbose_name_plural = 'Повторения'



    