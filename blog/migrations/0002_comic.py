# Generated by Django 4.0.6 on 2022-07-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('editorial', models.CharField(max_length=30)),
                ('anio', models.DateField(null=True)),
            ],
        ),
    ]
