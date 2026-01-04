from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # lab.html browser me show hoga

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/membership")
def membership():
    return render_template("membership.html")


app.run(debug=True)
