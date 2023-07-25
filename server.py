from flask import Flask, render_template, Response
import logging
import speakerSound


app = Flask(
    __name__, static_url_path="", static_folder="public", template_folder="public"
)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/audio")
def audio():
    return Response(speakerSound.getSpeakerSound())
