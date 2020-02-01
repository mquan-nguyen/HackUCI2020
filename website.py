from flask import Flask, redirect, url_for, render_template
import SongSearch
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results")
def results():
    return render_template("results.html")





if __name__ == "__main__":
    app.run()