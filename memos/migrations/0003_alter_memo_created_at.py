# Generated by Django 4.2.1 on 2023-05-21 13:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('memos', '0002_alter_memo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
