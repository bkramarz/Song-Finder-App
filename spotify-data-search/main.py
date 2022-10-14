from spotify_search import SpotifySearch
from last_fm_search import LastFmSearch

spotify_search = SpotifySearch()

query = input("Enter an artist name:\n")

# spotify_similar_artist_list = spotify_search.get_related_artists(query)
# last_fm_similar_artist_list = last_fm_search.get_similar_artists(query)
#
# final_list = [artist for artist in last_fm_similar_artist_list if artist in spotify_similar_artist_list]
#
# print(final_list)

last_fm_top_tracks = LastFmSearch.get_top_tracks(query)
spotify_top_tracks = spotify_search.get_top_tracks(query)


print(last_fm_top_tracks)
print(spotify_top_tracks)
