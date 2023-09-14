# Generated by Django 4.2.5 on 2023-09-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tritones', '0002_rename_year_released_tritonespotifytrack_release_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tritonespotifytrack',
            name='spotify_url',
            field=models.URLField(default='https://open.spotify.com/artist/1eohVzWa5vbk54pmWcFQar?si=71AoLgjKRSWHbcCmXVJ4RA'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tritonespotifytrack',
            name='release_year',
            field=models.IntegerField(),
        ),
    ]