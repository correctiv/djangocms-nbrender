from django.contrib import admin

from .models import Notebook


class NotebookAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    actions = ['download']

    def download(self, request, queryset):
        for q in queryset:
            q.download_and_store()


admin.site.register(Notebook, NotebookAdmin)
