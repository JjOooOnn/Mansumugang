# Generated by Django 3.2.9 on 2021-11-25 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nhis', '0002_alter_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
