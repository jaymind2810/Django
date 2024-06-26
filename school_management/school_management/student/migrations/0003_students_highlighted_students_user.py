# Generated by Django 4.2.11 on 2024-04-08 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0002_students_available_join'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='highlighted',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
