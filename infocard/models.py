from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from common.models import AbsCreated, AbsActive


# Create your models here.
class Tag(AbsCreated, AbsActive):
    title = models.CharField('Название', max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class InfoCard(AbsCreated, AbsActive):
    question = RichTextUploadingField('Вопрос')
    answer = RichTextUploadingField('Ответ')

    def __str__(self):
        return self.question[:7]

    class Meta:
        verbose_name = 'Информационная карточка'
        verbose_name_plural = 'Информационные карточки'


class InfoCardTag(AbsCreated):
    info_card = models.ForeignKey('infocard.InfoCard', related_name='info_card_items', on_delete=models.CASCADE)
    tag = models.ForeignKey('infocard.Tag', related_name='tag_items', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.info_card}, {self.tag}'

    class Meta:
        verbose_name = 'Информационная карта - тег'
        verbose_name_plural = 'Информационная карта - тег'


class Remember(AbsCreated, AbsActive):
    STATUS_NEW = 'new'
    STATUS_SENT = 'sent'
    STATUS_TRUE = 'true'
    STATUS_FALSE ='false'
    STATUS_NO_ANSWER = 'no_answer'
    STATUSES = (
        (STATUS_NEW, 'Новый'),
        (STATUS_SENT, 'Отправлен'),
        (STATUS_TRUE, 'Отвечен правильно'),
        (STATUS_FALSE, 'Отвечен неправильно'),
        (STATUS_NO_ANSWER, 'Не отвечен'),
    )

    date = models.DateTimeField('Время')
    info_card = models.ForeignKey('infocard.InfoCard', verbose_name='Карточка', related_name='remembers',
                                  on_delete=models.CASCADE)
    status = models.CharField('Статус', choices=STATUSES, default=STATUS_NEW, max_length=20)

    def __str__(self):
        return f'{self.date}, {self.info_card}, {self.status}'

    class Meta:
        verbose_name = 'Повторение'
        verbose_name_plural = 'Повторения'

