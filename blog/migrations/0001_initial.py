# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 21:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Başlık')),
                ('slug', models.SlugField(max_length=200, verbose_name='Yazı Url')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Kategori Adı')),
                ('statement', models.TextField(max_length=200, verbose_name='Kategori Açıklaması')),
                ('slug', models.SlugField(max_length=200, verbose_name='Kategori Url')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='topic_name',
            field=models.ForeignKey(default='SOME STRING', on_delete=django.db.models.deletion.CASCADE, to='blog.Topic'),
        ),
    ]
