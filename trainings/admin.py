from django.contrib import admin

from trainings.models import Training, RememberItem


# Register your models here.
class RememberItemInline(admin.TabularInline):
    model = RememberItem
    extra = 0
    fields = ['remember', 'index', ]
    readonly_fields = ['created', 'updated', ]
    ordering = ['index', ]

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['account', 'is_active', 'id', 'created', 'updated', ]
    list_filter = ['is_active',]
    search_fields = ['account__username', ]
    readonly_fields = ['created', 'updated', ]
    inlines = [RememberItemInline, ]
