# Generated by Django 4.1.2 on 2022-10-31 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacation_management_app', '0008_alter_vacationrequest_reason_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationrequest',
            name='finish_date',
            field=models.DateField(verbose_name='Finish date'),
        ),
        migrations.AlterField(
            model_name='vacationrequest',
            name='reason',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Reason'),
        ),
        migrations.AlterField(
            model_name='vacationrequest',
            name='start_date',
            field=models.DateField(verbose_name='Start date'),
        ),
    ]