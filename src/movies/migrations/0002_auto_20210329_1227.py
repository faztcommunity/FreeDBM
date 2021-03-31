# Generated by Django 3.1.7 on 2021-03-29 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='fullname',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='fullname',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='gener',
            name='genere_name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
