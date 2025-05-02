from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is the deployed Flask app!"

if __name__ == '__main__':
    # Get the PORT from environment or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Bind to 0.0.0.0 so it works on Render
    app.run(host='0.0.0.0', port=port, debug=True)