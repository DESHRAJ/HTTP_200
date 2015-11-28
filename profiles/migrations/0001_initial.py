# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
from django.contrib.auth.models import Group

def add_group(apps, schema_editor):
    group, created = Group.objects.get_or_create(name='StudentGroup')   

    group, created = Group.objects.get_or_create(name='FacultyGroup') 


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(add_group),

        migrations.CreateModel(
            name='Faculty1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('ph_no', models.PositiveIntegerField(null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('alternate_email', models.EmailField(max_length=254, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('univ_roll_no', models.PositiveIntegerField()),
                ('ph_no', models.PositiveIntegerField(null=True)),
                ('father_name', models.CharField(max_length=200, null=True)),
                ('mother_name', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('course', models.CharField(default=b'BT', max_length=3, choices=[(b'BT', b'B.Tech'), (b'MCA', b'MCA'), (b'MBA', b'MBA'), (b'OT', b'Others')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
