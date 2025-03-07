# Generated by Django 5.0.6 on 2024-05-20 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kafedra', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='information',
            options={'verbose_name': 'Информация', 'verbose_name_plural': 'Информация'},
        ),
        migrations.AlterField(
            model_name='information',
            name='page_type',
            field=models.IntegerField(blank=True, choices=[(1, 'MAIN_PAGE'), (2, 'FACULTY_HISTORY_PAGE'), (3, 'RESEARCH_WORK_PAGE'), (4, 'INTERNATIONAL_COOPERATION_PAGE'), (5, 'EMPLOYMENT_PAGE')], null=True),
        ),
    ]
