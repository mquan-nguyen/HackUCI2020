from flask import Flask, redirect, url_for, render_template, request

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

client_credentials_manager = SpotifyClientCredentials("46ac1119a48245408a9d9c5742ae50f5",
                                                      "7d33323ef7e8420b8a022d0515eca711")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False


@app.route("/")
def home():
    return render_template("frontpage.html")


@app.route("/", methods=['POST'])
def results():
    genre = request.form['genre']
    dance = request.form['danceability']
    energy = request.form['energy']
    instru = request.form['instrumentalness']
    valence = request.form['valence']
    tempo = request.form['tempo']
    print(float(dance) / 100)
    print(float(energy) / 100)
    print(float(instru) / 100)
    print(float(valence) / 100)
    print(int(tempo))
    tracks = sp.recommendations(seed_genres=[genre], limit=100, target_danceability=dance,
                                target_energy=energy, target_instrumentalness=instru,
                                target_valence=valence, target_tempo=tempo)

    return render_template("test.html"  , tracks=tracks)


if __name__ == "__main__":
    app.run()
