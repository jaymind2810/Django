# Generated by Django 4.2.11 on 2024-04-03 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='name',
            new_name='email',
        ),
    ]
