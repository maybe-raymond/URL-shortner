from flask import render_template, request, jsonify, redirect, abort
from main import application, db
from main.config import Development as d
from main.models import URL
from main.utils import add_Url_to_database, randomSringGenerator, is_in_database


domain = d.Domain

@application.route("/")
def home():
    return render_template("index.html")



#Api implemtation
@application.route("/shorten", methods=["POST"])
def Shoterned_Url():
    data = request.get_json()
    new_url = randomSringGenerator(3)
    check = is_in_database(new_url)
    while(check):
        new_url = randomSringGenerator(3)
        check = is_in_database(new_url)
    add_Url_to_database(data, new_url)
    print(data, new_url)
    return {
        "url": f"{domain}{new_url}"
    }


@application.route("/<used_url>", methods=["GET"])
def go_To_Url(used_url):
    p = URL.query.filter_by(new_link=used_url).first()
    print(p.orginal_link)
    if p is None or p.orginal_link is None:
        abort(400)
    return redirect(p.orginal_link)


@application.errorhandler(400)
def page_not_found(e):
    return render_template("404.html")
