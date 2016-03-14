from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .views import NotebookView


urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', NotebookView.as_view(),
        name='djangocms_nbrender-notebook'),
]
