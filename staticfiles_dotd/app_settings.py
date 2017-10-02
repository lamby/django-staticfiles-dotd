from django.conf import settings

RENDER_PIPELINE = getattr(settings, 'STATICFILES_DOTD_RENDER_PIPELINE', (
    'staticfiles_dotd.pipeline.read_file',
))

DIRECTORY_SUFFIX = getattr(
    settings,
    'STATICFILES_DOTD_DIRECTORY_SUFFIX',
    '.d',
)
