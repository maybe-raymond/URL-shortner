from flask import render_template, request, jsonify, redirect
from main import app, db
from main.models import URL
from main.utils import add_Url_to_database, randomSringGenerator, is_in_database


domain = "127.0.0.1:5000/"


@app.route("/")
def home():
    return render_template("index.html")



#Api implemtation
@app.route("/shorten", methods=["POST"])
def Shoterned_Url():
    data = request.get_json()
    new_url = randomSringGenerator(3)
    check = is_in_database(new_url)
    while(check):
        print("hello")
        new_url = randomSringGenerator(3)
        check = is_in_database(new_url)
    add_Url_to_database(data, new_url)
    return {
        "url": f"{domain}{new_url}"
    }


@app.route("/<used_url>", methods=["GET"])
def go_To_Url(used_url):
    p = URL.query.filter_by(new_link=used_url).first()
    return redirect(p.orginal_link)



