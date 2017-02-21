# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeslaApp', '0002_auto_20170218_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('File', models.FileField(upload_to='C:\\cbr\\Python\\eclipse\\TeslaBBX\\src')),
                ('PN', models.CharField(max_length=30)),
                ('SN', models.CharField(max_length=30)),
                ('ECC', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
