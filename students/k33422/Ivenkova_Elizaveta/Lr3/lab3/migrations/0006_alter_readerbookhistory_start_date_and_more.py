# Generated by Django 4.1 on 2023-12-01 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0005_alter_readerbookhistory_book_instance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readerbookhistory',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='readerroomhistory',
            name='start_date',
            field=models.DateField(),
        ),
    ]
