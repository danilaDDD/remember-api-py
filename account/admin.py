from django.contrib import admin

from account.models import Account, PrimaryAccess


# Register your models here.
@admin.register(PrimaryAccess)
class PrimaryAccessAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated',]


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'email', 'is_active', 'created', 'updated',)
    readonly_fields = ['created', 'updated',]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'patronymic', 'email',
                                         'phone', 'birth_date', 'gender', 'created', 'updated',)}),
        ('Security', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),

    )

