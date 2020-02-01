import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials("46ac1119a48245408a9d9c5742ae50f5",
                                                      "7d33323ef7e8420b8a022d0515eca711")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False


def results(genre: list, dance: float, energy: float, instru: float, valence: float, tempo: int):
    count = 1
    tracks = sp.recommendations(seed_genres=genre, limit=100, target_danceability=dance, target_energy=energy,
                                target_instrumentalness=instru, target_valence=valence, target_tempo=tempo)
    for track in tracks['tracks']:
        print(str(count) + ".", track['name'], '-', track['artists'][0]['name'])
        count += 1


def search():
    genres = ["alt-rock", "alternative", "ambient",
              "anime", "blues", "bossanova", "children", "chill",
              "classical", "club", "country", "dance", "deep-house",
              "disco", "disney", "dubstep", "edm", "electro", "electronic",
              "folk", "funk", "groove", "guitar", "happy", "hardcore",
              "heavy-metal", "hip-hop", "holidays", "house",
              "indie", "indie-pop", "j-dance", "j-pop", "j-rock",
              "jazz", "k-pop", "kids", "latin", "metal", "metalcore",
              "new-release", "opera", "party", "piano",
              "pop", "punk", "punk-rock", "r-n-b", "rainy-day",
              "reggae", "road-trip", "rock", "rock-n-roll",
              "romance", "sad", "salsa", "sleep", "soul", "spanish",
              "study", "summer", "synth-pop", "tango", "techno",
              "trance", "work-out"]

    genchoice = input("Please select a genre to search through, -1 to stop: ")
    if genchoice not in genres:
        while genchoice not in genres:
            genchoice = input("That genre does not exist, enter another: ")

    genre = [genchoice]
    dance = float(input("What danceability do you want?: "))
    energy = float(input("What energy do you want?: "))
    instrument = float(input("What instrumentalness do you want?: "))
    valence = float(input("what valence do you want?: "))
    tempo = int(input("what tempo do you want?: "))

    results(genre, dance, energy, instrument, valence, tempo)


if __name__ == "__main__":
    search()
