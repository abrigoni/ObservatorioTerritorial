# Generated by Django 2.2 on 2019-06-15 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0012_auto_20190614_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researcher',
            name='experience',
        ),
    ]
