from rest_framework import serializers
from .models import TritoneSpotifyTrack

class tritoneSpotifyTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TritoneSpotifyTrack
        fields = ('name', 'artist', 'album', 'release_year', 'image_url', 'spotify_url', 'spotify_id')