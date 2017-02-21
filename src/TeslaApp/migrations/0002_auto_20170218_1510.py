# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeslaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='File',
            field=models.FileField(upload_to='C:\\cbr\\Python\\eclipse\\TeslaBBX\\src'),
        ),
    ]
