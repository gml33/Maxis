# Generated by Django 4.2.2 on 2023-06-20 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='apellido',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
