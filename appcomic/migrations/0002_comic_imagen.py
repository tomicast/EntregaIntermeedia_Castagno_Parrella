# Generated by Django 4.0.5 on 2022-08-02 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcomic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='comics'),
        ),
    ]
