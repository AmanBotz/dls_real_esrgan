from flask import Flask
import app  # Starts your Telegram bot

flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return "Bot is running"

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=8000)
