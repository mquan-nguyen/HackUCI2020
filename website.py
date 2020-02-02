
from flask import Flask, redirect, render_template, request
import createtest
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

client_credentials_manager = SpotifyClientCredentials("ea0c656488584306a06112ac850edf72",
                                                      "024e189e36c74097a1c054bbe97eb433")

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False

@app.route("/")
def home():
    """endpoint for landing page"""

    return render_template("frontpage.html")


@app.route("/", methods=['POST'])
def results():
    """redirects to created playlist based on tracks that have attributes given by template sliders"""

    genre = request.form['genre']
    dance = request.form['danceability']
    energy = request.form['energy']
    instru = request.form['instrumentalness']
    valence = request.form['valence']
    tempo = request.form['tempo']

    tracks = sp.recommendations(seed_genres=[genre], limit=100, target_danceability=dance,
                                target_energy=energy, target_instrumentalness=instru,
                                target_valence=valence, target_tempo=tempo)

    url = createtest.create(tracks, genre)

    return redirect("https://open.spotify.com/playlist/" + url)


if __name__ == "__main__":
    app.run()
