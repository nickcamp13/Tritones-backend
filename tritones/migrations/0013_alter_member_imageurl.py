# Generated by Django 4.2.3 on 2023-09-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tritones', '0012_delete_boardmember_member_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='imageUrl',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]