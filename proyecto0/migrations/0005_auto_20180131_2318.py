# Generated by Django 2.0.1 on 2018-02-01 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto0', '0004_auto_20180131_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='categoria',
            field=models.CharField(choices=[('Conferencia', 'Conferencia'), ('Seminario', 'Seminario'), ('Congreso', 'Congreso'), ('Curso', 'Curso')], max_length=100),
        ),
        migrations.AlterField(
            model_name='evento',
            name='modalidad',
            field=models.CharField(choices=[('Presencial', 'Presencial'), ('Virtual', 'Virtual')], max_length=100),
        ),
    ]