# Generated by Django 4.1.4 on 2023-01-16 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_registration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='password2',
        ),
        migrations.AddField(
            model_name='registration',
            name='username',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
