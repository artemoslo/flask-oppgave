from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    navn = "Artem"
    elever = ["Ola", "Kari", "Per", "Fatima"]
    return render_template("index.html", navn=navn, elever=elever)
@app.route("/om")
def om():
    return '<h1>Om meg</h1><a href="/">Forside</a>'
@app.route("/kontakt")
def kontakt():
    return '<h1>Kontakt</h1><a href="/">Forside</a>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)