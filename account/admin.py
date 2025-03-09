from django.contrib import admin

from account.models import Account, PrimaryAccess


# Register your models here.
@admin.register(PrimaryAccess)
class PrimaryAccessAdmin(admin.ModelAdmin):
    pass


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'first_name', 'last_name', 'phone', 'email', 'is_active', )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'patronymic', 'email',
                                         'phone', 'birth_date', 'gender')}),
        ('Security', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),

    )

