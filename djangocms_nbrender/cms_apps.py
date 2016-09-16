from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class NotebookApp(CMSApp):
    name = _('Notebook App')
    app_name = 'djangocms_nbrender'
    urls = ['djangocms_nbrender.urls']


apphook_pool.register(NotebookApp)
