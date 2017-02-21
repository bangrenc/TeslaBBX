# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeslaApp', '0003_auto_20170218_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('File', models.FileField(upload_to='C:\\cbr\\Python\\eclipse\\TeslaBBX\\src')),
            ],
        ),
        migrations.RemoveField(
            model_name='data',
            name='File',
        ),
    ]
