# Generated by Django 4.2.5 on 2023-10-12 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
        ),
    ]
