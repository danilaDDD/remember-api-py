LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
RENDER_TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True
gettext_noop = lambda s: s
LANGUAGES = (
    ('ru', gettext_noop('Russian')),
    ('en', gettext_noop('English')),
)
LANGUAGES_ADMIN = {
    'ru': 'Russian',
    'en': 'English',
}
