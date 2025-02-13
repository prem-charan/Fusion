# Generated by Django 3.1.5 on 2024-03-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_procedures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistantshipclaim',
            name='year',
            field=models.IntegerField(choices=[(2024, 2024), (2023, 2023)]),
        ),
        migrations.AlterField(
            model_name='course_registration',
            name='working_year',
            field=models.IntegerField(blank=True, choices=[(2024, 2024), (2023, 2023)], null=True),
        ),
        migrations.AlterField(
            model_name='finalregistrations',
            name='batch',
            field=models.IntegerField(default=2024),
        ),
        migrations.AlterField(
            model_name='messdue',
            name='year',
            field=models.IntegerField(choices=[(2024, 2024), (2023, 2023)]),
        ),
        migrations.AlterField(
            model_name='register',
            name='year',
            field=models.IntegerField(default=2024),
        ),
    ]
