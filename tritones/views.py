from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TritoneSpotifyTrack
from .config import sp
from .serializers import tritoneSpotifyTrackSerializer

def get_track_data(request):
    data = TritoneSpotifyTrack.objects.all()
    if request.method == 'GET':
        serializer = tritoneSpotifyTrackSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

# Create your views here.
def view_home(request):
    the_tritones_artist_id = "1eohVzWa5vbk54pmWcFQar"
    fetch_and_store_tracks(the_tritones_artist_id)
    return HttpResponse("Hello, Tritones!")

def fetch_and_store_tracks(artist_spotify_id):
    # Fetch the top tracks of the artist
    top_tracks = sp.artist_top_tracks(artist_spotify_id)

    # Process and store the fetched tracks in the database
    for track_data in top_tracks['tracks']:
        # Extract relevant information from the track data
        name = track_data['name']
        album = track_data['album']['name']
        spotify_id = track_data['id']

        # Fetch additional details for the track
        track_details = sp.track(spotify_id)

        # Extract the track image URL, track name, and year of release
        image_url = track_details['album']['images'][0]['url']  # URL of the first image
        release_year = track_details['album']['release_date'].split('-')[0]  # Extract year from release_date
        spotify_url = track_details['external_urls']['spotify']  # Spotify URL

        # Create or update the SpotifyTrack model instance with the additional details
        track, created = TritoneSpotifyTrack.objects.get_or_create(
            spotify_id=spotify_id,
            defaults={'name': name, 'album': album, 'image_url': image_url, 'release_year': release_year, 'spotify_url': spotify_url}
        )

    # Optionally, you can return the fetched tracks or a success message
    return "Data fetched and stored successfully."
    

def view_about_us(request):
    return HttpResponse("Hello, About Us!")

def view_auditions(request):
    return HttpResponse("Hello, Auditions!")

def view_photos(request):
    return HttpResponse("Hello, Photos!")

def view_bookings(request):
    return HttpResponse("Hello, Bookings!")

def view_contact_us(request):
    return HttpResponse("Hello, Contact Us!")
