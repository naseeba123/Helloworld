# Generated by Django 4.0.2 on 2022-06-15 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
