# Generated by Django 2.2 on 2019-06-05 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0004_project_background'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
        migrations.AddField(
            model_name='publication',
            name='authors',
            field=models.ManyToManyField(to='directory.Author'),
        ),
    ]
