from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

RESPONSES = [
    "Hello! I'm your SIAG Software chatbot demo 🤖",
    "I'm a simple example showing how dialogue systems work.",
    "Our AI tools can be integrated with any API or service you need!",
    "Automation + Intelligence = SIAG Software."
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    bot_msg = random.choice(RESPONSES)
    return jsonify({"reply": bot_msg})

if __name__ == "__main__":
    app.run(debug=True)
