from flask import Flask
from threading import Thread
import app  # this starts the Telegram bot (make sure app.py auto-starts the bot logic)

app_flask = Flask(__name__)

@app_flask.route('/')
def index():
    return "Bot is running!", 200

def run_flask():
    app_flask.run(host='0.0.0.0', port=8000)

if __name__ == '__main__':
    # Run Flask in a separate thread so the Telegram bot doesn't block it
    Thread(target=run_flask).start()
    # Start the Telegram bot (already started by importing app.py)
