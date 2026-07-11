from flask import Flask, render_template
from piecharts import generate_pie
from bargraphs import generate_bar

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/graph")
def graph():
    print("Before generate_pie()")
    generate_pie()
    print("After generate_pie()")
    return render_template("pie.html")

print(app.url_map)

@app.route("/bargraph")
def bargraph():
    generate_bar()
    return render_template("bargraph.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/tech")
def tech():
    return render_template("tech.html")

@app.route("/toppers")
def toppers():
    return render_template("toppers.html")

if __name__ == "__main__":
    app.run(debug=True)