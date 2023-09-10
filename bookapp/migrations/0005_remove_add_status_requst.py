# Generated by Django 4.0.2 on 2022-06-23 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0004_add_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add',
            name='status',
        ),
        migrations.CreateModel(
            name='requst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='request', max_length=100)),
                ('aa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.add')),
                ('rr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.register')),
            ],
        ),
    ]
