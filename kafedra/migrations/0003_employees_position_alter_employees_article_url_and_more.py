# Generated by Django 5.0.6 on 2024-05-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kafedra', '0002_alter_information_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='article_url',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='contact',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
