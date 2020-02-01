import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials("46ac1119a48245408a9d9c5742ae50f5",
                                                      "7d33323ef7e8420b8a022d0515eca711")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False


def results(genre: list, dance: float, energy: float, valence: float):
    count = 1
    tracks = sp.recommendations(seed_genres=genre, limit=100, min_danceability=dance, min_energy=energy,
                                min_valence=valence)
    for track in tracks['tracks']:
        print(str(count) + ".", track['name'], '-', track['artists'][0]['name'])
        count += 1


def search():
    genres = ["acoustic", "afrobeat", "alt-rock", "alternative", "ambient",
              "anime", "black-metal", "bluegrass", "blues", "bossanova",
              "brazil", "breakbeat", "british", "cantopop", "chicago-house",
              "children", "chill", "classical", "club", "comedy",
              "country", "dance", "dancehall", "death-metal", "deep-house",
              "detroit-techno", "disco", "disney", "drum-and-bass", "dub",
              "dubstep", "edm", "electro", "electronic", "emo",
              "folk", "forro", "french", "funk", "garage",
              "german", "gospel", "goth", "grindcore", "groove",
              "grunge", "guitar", "happy", "hard-rock", "hardcore",
              "hardstyle", "heavy-metal", "hip-hop", "holidays", "honky-tonk",
              "house", "idm", "indian", "indie", "indie-pop", "industrial",
              "iranian", "j-dance", "j-idol", "j-pop", "j-rock",
              "jazz", "k-pop", "kids", "latin", "latino",
              "malay", "mandopop", "metal", "metal-misc", "metalcore",
              "minimal-techno", "movies", "mpb", "new-age", "new-release",
              "opera", "pagode", "party", "philippines-opm", "piano",
              "pop", "pop-film", "post-dubstep", "power-pop", "progressive-house",
              "psych-rock", "punk", "punk-rock", "r-n-b", "rainy-day",
              "reggae", "reggaeton", "road-trip", "rock", "rock-n-roll",
              "rockabilly", "romance", "sad", "salsa", "samba",
              "sertanejo", "show-tunes", "singer-songwriter", "ska", "sleep",
              "songwriter", "soul", "soundtracks", "spanish", "study",
              "summer", "swedish", "synth-pop", "tango", "techno",
              "trance", "trip-hop", "turkish", "work-out", "world-music"]

    genchoice = input("Please select a genre to search through: ")
    if genchoice not in genres:
        while genchoice not in genres:
            genchoice = input("That genre does not exist, enter another: ")

    genre = [genchoice]
    dance = float(input("What danceability do you want?: "))
    # acoustic = float(input("What acousticness do you want?: "))
    energy = float(input("What energy do you want?: "))
    # instrument = float(input("What instrumentalness do you want?: "))
    valence = float(input("what valence do you want?: "))
    # tempo = float(input("what tempo do you want?: "))

    results(genre, dance, energy, valence)


if __name__ == "__main__":
    search()
