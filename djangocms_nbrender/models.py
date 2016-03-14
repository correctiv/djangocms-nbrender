try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.files.base import ContentFile

from cms.models import CMSPlugin

import nbformat
from nbconvert import HTMLExporter

from .utils import OverwriteStorage


def get_notebook_filename(instance, filename):
    return '%s/%s/%s' % ('notebooks', instance.slug, 'notebook.ipynb')


@python_2_unicode_compatible
class Notebook(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    web = models.URLField(blank=True)
    url = models.URLField(blank=True)
    notebook = models.FileField(blank=True, upload_to=get_notebook_filename,
                                            storage=OverwriteStorage())

    class Meta:
        verbose_name = _('Notebook')
        verbose_name_plural = _('Notebooks')
        ordering = ('name',)

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('djangocms_nbrender:djangocms_nbrender-notebook', (),
                {'slug': self.slug})

    def download_and_store(self):
        if self.url:
            self.notebook.save('temp.ipynb', ContentFile(self.get_url()))

    def get_url(self):
        return urlopen(self.url).read()

    def get_html_export(self, nb):
        exporter = HTMLExporter()
        exporter.template_file = 'basic'
        return exporter.from_notebook_node(nb)

    def get_html(self, start=None, count=None):
        if start is None:
            start = 0
        nb = nbformat.read(self.notebook, as_version=4)
        if count is None:
            count = len(nb['cells'])
        nb['cells'] = nb['cells'][start:(start + count)]
        html, resources = self.get_html_export(nb)
        return html


@python_2_unicode_compatible
class NotebookViewerCMSPlugin(CMSPlugin):
    notebook = models.ForeignKey(Notebook)

    start = models.IntegerField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return 'Notebook Viewer %s' % self.notebook
