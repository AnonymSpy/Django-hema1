# Generated by Django 4.2.2 on 2023-06-30 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_delete_userinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.RemoveField(
            model_name='user',
            name='c_time',
        ),
    ]
