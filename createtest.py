import spotipy
import spotipy.util as util

username = "1rgrrmjxxy8r0amznrm1el0sb"
clientID = "ea0c656488584306a06112ac850edf72"
clientSecret = "024e189e36c74097a1c054bbe97eb433"
scope = "playlist-modify-public"
redirectURI = "http://localhost/"

token = util.prompt_for_user_token(username=username, scope=scope, client_id=clientID, client_secret=clientSecret,
                                   redirect_uri=redirectURI)
def create(tracks, genre):
    """creates playlist based on generated tracks and genre"""

    sp = spotipy.Spotify(auth=token)
    sp.trace = False

    newplist = sp.user_playlist_create(user=username, name=genre.capitalize())


    playlist = []
    for track in tracks['tracks']:
        playlist.append(track['uri'])

    sp.user_playlist_add_tracks(user=username, playlist_id=newplist['uri'], tracks=playlist)
    url = newplist['id']

    return url


if __name__ == "__main__":
    create()