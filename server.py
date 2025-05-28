from flask import Flask
import threading
import app  # starts your Telegram bot

flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return "Telegram bot is running"

def run_flask():
    flask_app.run(host='0.0.0.0', port=8000)

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
