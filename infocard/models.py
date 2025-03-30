from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from common.models import AbsCreated, AbsActive


# Create your models here.
class Tag(AbsCreated, AbsActive):
    title = models.CharField('Название', max_length=100, unique=True)
    account = models.ForeignKey('account.Account', verbose_name='Пользователь', related_name='tags',
                                on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class InfoCard(AbsCreated, AbsActive):
    question = RichTextUploadingField('Вопрос')
    answer = RichTextUploadingField('Ответ')
    account = models.ForeignKey('account.Account', verbose_name='Пользователь', related_name='info_cards',
                                on_delete=models.CASCADE)
    tags_text = models.CharField('Теги', max_length=255)
    closed = models.BooleanField('Закрыто', default=True)

    def update_tags_text(self):
        self.tags_text = '>'.join([tag_item.tag.title
                            for tag_item in
                            self.tag_items.prefetch_related('tag').order_by('-tag_id')])

    def update_closed(self):
        last_remember = self.remembers.order_by('-date').first()
        if last_remember is not None:
            if last_remember.status == Remember.STATUS_TRUE:
                self.closed = True
            elif last_remember.status == Remember.STATUS_NEW:
                self.closed = False

    def __str__(self):
        return self.question[:7]

    class Meta:
        verbose_name = 'Информационная карточка'
        verbose_name_plural = 'Информационные карточки'


class InfoCardTag(AbsCreated):
    info_card = models.ForeignKey('infocard.InfoCard', related_name='tag_items', on_delete=models.CASCADE)
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
    real_answer = RichTextUploadingField('Реальный ответ')
    status = models.CharField('Статус', choices=STATUSES, default=STATUS_NEW, max_length=20)

    def __str__(self):
        return f'{self.date}, {self.info_card}, {self.status}'

    def get_question(self) -> str:
        return self.info_card.question

    def get_answer(self) -> str:
        return self.info_card.answer

    class Meta:
        verbose_name = 'Повторение'
        verbose_name_plural = 'Повторения'

