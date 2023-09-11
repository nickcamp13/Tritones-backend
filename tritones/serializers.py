from rest_framework import serializers
from .models import TritonesSpotifyTrack

class tritoneSpotifyTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TritonesSpotifyTrack
        fields = ('name', 'artist', 'album', 'release_year', 'image_url', 'spotify_url', 'spotify_id')