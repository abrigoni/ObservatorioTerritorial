# Generated by Django 2.2.2 on 2019-06-07 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0005_auto_20190605_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researcher',
            name='institute',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='directory.Institute'),
        ),
    ]
