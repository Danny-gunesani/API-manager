# Generated by Django 5.1.6 on 2025-02-10 12:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apikey',
            name='user',
        ),
        migrations.AlterField(
            model_name='apikey',
            name='key',
            field=models.CharField(default=uuid.uuid4, max_length=50, unique=True),
        ),
    ]
