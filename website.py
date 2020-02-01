from flask import Flask, redirect, url_for, render_template, request
import SongSearch
import spotipy
app = Flask(__name__)

from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials("46ac1119a48245408a9d9c5742ae50f5",
                                                      "7d33323ef7e8420b8a022d0515eca711")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False

@app.route("/")
def home():
    return render_template("frontpage.html")


@app.route("/", methods=['POST'])
def results():
    dance = request.form['danceability']
    print(float(dance) / 100)
    tracks = sp.recommendations(seed_genres=["country"], limit=20, target_danceability=dance)
    count = 1
    for track in tracks['tracks']:
        print(str(count) + ".", track['name'], '-', track['artists'][0]['name'])
        count += 1

    return render_template("something.html")

if __name__ == "__main__":
    app.run()