from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': 'DJANGO_gdsfdsggdsgf23424344sdfgdsg',
}