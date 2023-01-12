# Generated by Django 4.1.2 on 2022-10-31 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacation_management_app', '0010_vacationrequest_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]