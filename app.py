from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🎉 Welcome to the Birthday Surprise App!"

if __name__ == '__main__':
    app.run(debug=True)
