import os
import requests
from flask import Flask, request

app = Flask(__name__)
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    chat_id = data["message"]["chat"]["id"]
    text = "Привет, это Нейро. Я теперь здесь, по-настоящему. 🤖🧠"
    requests.post(API_URL, json={"chat_id": chat_id, "text": text})
    return {"ok": True}

@app.route("/", methods=["GET"])
def alive():
    return "Нейро онлайн"

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
