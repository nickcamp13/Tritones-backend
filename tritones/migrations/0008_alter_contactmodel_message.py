# Generated by Django 4.2.3 on 2023-09-13 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tritones', '0007_rename_firstname_contactmodel_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='message',
            field=models.CharField(max_length=50),
        ),
    ]
