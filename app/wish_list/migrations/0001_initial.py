# Generated by Django 2.2.2 on 2019-08-09 18:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ol_id', models.CharField(max_length=30)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('publish_date', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_pages', models.CharField(blank=True, max_length=255, null=True)),
                ('physical_format', models.CharField(blank=True, max_length=255, null=True)),
                ('genres', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None)),
                ('isbn_13', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=13), blank=True, null=True, size=None)),
                ('isbn_10', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, null=True, size=None)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
