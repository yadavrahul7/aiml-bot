from flask import Flask, request, make_response
from lib.Chatbot import Chatbot

app = Flask(__name__)
chatbot = Chatbot()


@app.route('/', methods=["GET", "POST"])
def home():
    return {
        "message": "Welcome to Sheth L.U.J and Sir M.V College of Science, Commerce and Arts chatbot."
    }


@app.route("/message", methods=["POST"])
def parse_message():
    if request.method == "POST":
        message = request.json["message"]

        if message:
            return {"reponse": chatbot.respond(message)}
