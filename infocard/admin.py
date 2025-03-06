from django.contrib import admin

from infocard.models import Tag, InfoCardTag, Remember, InfoCard


# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', ]
    list_filter = ['is_active', ]
    search_fields = ['title', ]
    fieldsets = (
        (None, {'fields': ('title',)}),
        ('Дополнительно', {'fields': ('is_active', )}),
    )
    readonly_fields = ['created', 'updated', ]
    date_hierarchy = 'created'
    ordering = ['title', ]
    actions = ['make_active', 'make_inactive', ]

    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    make_active.short_description = 'Пометить выбранные теги как активные'

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_inactive.short_description = 'Пометить выбранные теги как неактивные'


class InlineTagAdmin(admin.TabularInline):
    model = InfoCardTag
    extra = 0
    fields = ['tag', ]


class InlineRememberAdmin(admin.TabularInline):
    model = Remember
    extra = 0
    fields = ['date', 'status', ]
    readonly_fields = ['created', 'updated', ]
    ordering = ['date', ]
    actions = ['make_active', 'make_inactive', ]

    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    make_active.short_description = 'Пометить выбранные записи как активные'

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_inactive.short_description = 'Пометить выбранные записи как неактивные'


@admin.register(InfoCard)
class InfoCardAdmin(admin.ModelAdmin):
    list_display = ['is_active', ]
    list_filter = ['is_active',]
    fieldsets = (
        (None, {'fields': ('question', 'answer', 'is_active',)}),
    )
    readonly_fields = ['created', 'updated', ]
    date_hierarchy = 'created'
    inlines = [InlineTagAdmin, InlineRememberAdmin, ]

    actions = ['make_active', 'make_inactive', ]

    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    make_active.short_description = 'Пометить выбранные записи как активные'

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_inactive.short_description = 'Пометить выбранные записи как неактивные'

