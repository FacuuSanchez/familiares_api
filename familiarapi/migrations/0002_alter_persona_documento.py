# Generated by Django 4.0.5 on 2022-06-11 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiarapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='documento',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]