import requests

API_KEY = XXXXX
SHARED_SECRET = XXXXX
API_ROOT_URL = XXXXX


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

