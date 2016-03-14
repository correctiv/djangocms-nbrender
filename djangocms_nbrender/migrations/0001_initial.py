# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_nbrender.utils
import djangocms_nbrender.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('url', models.URLField(blank=True)),
                ('notebook', models.FileField(storage=djangocms_nbrender.utils.OverwriteStorage(), upload_to=djangocms_nbrender.models.get_notebook_filename, blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Notebook',
                'verbose_name_plural': 'Notebooks',
            },
        ),
        migrations.CreateModel(
            name='NotebookViewerCMSPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('start', models.IntegerField(null=True, blank=True)),
                ('count', models.IntegerField(null=True, blank=True)),
                ('notebook', models.ForeignKey(to='djangocms_nbrender.Notebook')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
