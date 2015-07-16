# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 7, 15, 9, 40, 17, 611963, tzinfo=utc), max_length=42),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 7, 15, 9, 40, 41, 51631, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
