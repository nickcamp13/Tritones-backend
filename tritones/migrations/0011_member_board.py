# Generated by Django 4.2.3 on 2023-09-16 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tritones', '0010_tritonespotifytrack'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='board',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]