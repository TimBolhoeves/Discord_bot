# Generated by Django 4.1.2 on 2022-10-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discordbot',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
