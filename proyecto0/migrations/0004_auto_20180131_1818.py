# Generated by Django 2.0.1 on 2018-01-31 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto0', '0003_auto_20180131_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha_fin',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_inicio',
            field=models.CharField(max_length=100),
        ),
    ]
