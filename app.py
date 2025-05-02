from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = '''
<!DOCTYPE html>
<html>
<head><title>Birthday Surprise</title></head>
<body style="font-family: sans-serif; text-align: center; padding-top: 50px;">
    <h2>Enter your friend's name:</h2>
    <form method="post">
        <input type="text" name="name" required>
        <button type="submit">Surprise!</button>
    </form>
</body>
</html>
'''

HTML_MESSAGE = '''
<!DOCTYPE html>
<html>
<head><title>Surprise!</title></head>
<body style="font-family: sans-serif; text-align: center; padding-top: 50px;">
    <h1>🎉🎂 Happy Birthday, {{ name }} Bhaiya! 🎂🎉</h1>
    <p>Wishing you a day filled with love, laughter, and cake! 🍰🥳</p>
    <p>Have an amazing year ahead! 🚀✨</p>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def birthday():
    if request.method == "POST":
        name = request.form["name"]
        return render_template_string(HTML_MESSAGE, name=name)
    return HTML_FORM

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)