from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from common.models import AbsCreated, AbsActive


# Create your models here
class PrimaryAccess(AbsCreated, AbsActive):
    owner = models.CharField('Владелец', max_length=50)
    token = models.CharField('Токен', max_length=250)

    def __str__(self):
        return self.owner

    class Meta:
        verbose_name = 'Токен доступа'
        verbose_name_plural = 'Токены доступа'


class Account(AbstractUser, AbsCreated):
    NONE_GENDER = 'none'
    MALE_GENDER = 'male'
    FEMALE_GENDER = 'female'
    GENDERS = (
        (NONE_GENDER, 'Не указан'),
        (MALE_GENDER, 'Мужской'),
        (FEMALE_GENDER, 'Женский')
    )

    patronymic = models.CharField('Отчество', max_length=50, blank=True)
    phone = models.CharField('Номер телефона', max_length=50, blank=True)
    email = models.EmailField('Email', unique=True)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    gender = models.CharField('Пол', max_length=20, choices=GENDERS, default=NONE_GENDER)
    chat_id = models.CharField('ID чата', max_length=50, blank=True)
    groups = models.ManyToManyField(blank=True,
                                      help_text='Группы, к которым принадлежит данный пользователь. Пользователь получает все разрешения, предоставленные каждой из его групп.',
                                      related_name='user_set', related_query_name='user', to='auth.Group',
                                      verbose_name='Группы пользователей'),
    user_permissions = models.ManyToManyField(blank=True, help_text='Особые разрешения для этого пользователя.', related_name='user_set',
                                            to='auth.Permission', verbose_name='Права пользователя'),

    objects = UserManager()
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
