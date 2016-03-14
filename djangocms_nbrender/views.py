from django.views.generic.detail import DetailView

from .models import Notebook


class NotebookView(DetailView):
    model = Notebook
