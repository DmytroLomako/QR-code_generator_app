# Generated by Django 5.1.4 on 2025-02-26 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_qr_code', '0011_remove_qrcodes_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcodes',
            name='desktop',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='qrcodes',
            name='date',
            field=models.DateField(default=datetime.date(2025, 2, 26)),
        ),
    ]
