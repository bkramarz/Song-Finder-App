import requests

API_KEY = "60d577a5b9c0d79dd292f3dc28b2c4a1"
SHARED_SECRET = "9e061f357bf0947de8b56a1e625b99d3"
API_ROOT_URL = "http://ws.audioscrobbler.com/2.0"


class LastFmSearch:

    @staticmethod
    def get_similar_artists(artist_name):
        response = requests.get(f"http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist={artist_name}"
                                f"&api_key={API_KEY}&format=json").json()
        artist_list = [artist['name'] for artist in response['similarartists']['artist']]
        return artist_list

    @staticmethod
    def get_top_tracks(artist_name):
        response = requests.get(f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist_name}"
                                f"&api_key={API_KEY}&format=json").json()
        top_tracks = [track['name'] for track in response['toptracks']['track']]
        return top_tracks

