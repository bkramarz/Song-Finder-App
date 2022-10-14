import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIPY_CLIENT_ID = "63a4bee8ef494519b4b94df8a05aa3e2"
SPOTIFY_CLIENT_SECRET = "0100d66e1c9a4df98fd2535262602c86"
scope = "user-library-read"


class SpotifySearch(spotipy.Spotify):

    def __init__(self):
        super().__init__()
        self.scope = "user-library-read"
        self.auth_manager = SpotifyOAuth(scope=self.scope,
                                         client_secret=SPOTIFY_CLIENT_SECRET,
                                         client_id=SPOTIPY_CLIENT_ID,
                                         redirect_uri="https://localhost:8888/callback")

    def get_artist_uri(self, artist_name):
        return self.search(q=f"artist: {artist_name}")["tracks"]["items"][0]["artists"][0]["uri"]

    def get_related_artists(self, artist_name):
        artist_uri = self.get_artist_uri(artist_name)
        related_artists = [artist["name"] for artist in self.artist_related_artists(artist_uri)["artists"]]
        return related_artists

    def get_top_tracks(self, artist_name):
        top_tracks = [track["name"] for track in self.artist_top_tracks(self.get_artist_uri(artist_name), country='US')["tracks"]]
        return top_tracks

