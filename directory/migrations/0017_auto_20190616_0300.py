# Generated by Django 2.2 on 2019-06-16 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0016_auto_20190615_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorPublication', to='directory.Publication'),
        ),
        migrations.AlterField(
            model_name='author',
            name='researcher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorResearcher', to='directory.Researcher'),
        ),
    ]
