# Generated by Django 4.1.1 on 2022-09-29 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_my_bool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='my_bool',
            field=models.BooleanField(verbose_name='We use coockie on this site. I understand'),
        ),
    ]
