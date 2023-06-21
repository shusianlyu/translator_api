from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>/")
def translator(word):
    definition = word.upper()
    res = {"definition": definition,
           "word": word}
    return res


if __name__ == '__main__':
    app.run(debug=True, port=5001)
