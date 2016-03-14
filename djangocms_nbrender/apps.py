from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class NotebookConfig(AppConfig):
    name = 'djangocms_nbrender'
    verbose_name = _('Notebook')
