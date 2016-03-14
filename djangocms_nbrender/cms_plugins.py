from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import NotebookViewerCMSPlugin


@plugin_pool.register_plugin
class NotebookViewerPlugin(CMSPluginBase):
    model = NotebookViewerCMSPlugin
    module = _("Notebook")
    name = _('Notebook Viewer')
    render_template = "djangocms_nbrender/plugins/notebookviewer.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        """
        Update the context with plugin's data
        """
        context['notebook'] = instance.notebook
        context['html'] = instance.notebook.get_html(start=instance.start,
                                                     count=instance.count)
        return context
