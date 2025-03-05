CKEDITOR_UPLOAD_PATH = 'redactor/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_Custom': [
            ['Format'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Bold', 'Italic', 'Underline', 'Strike'],
            ['TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList', 'Blockquote'],
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['Link', 'Unlink', 'Anchor'],
            '/',
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
            ['Scayt'],
            ['Maximize'],
            ['RemoveFormat', 'Source'],
        ],
        'toolbar': 'Custom',
        # 'toolbar': 'full',
        'removePlugins': 'stylesheetparser',
        'allowedContent': True,
        'forcePasteAsPlainText': True,
        'width': 950,
    },
}
