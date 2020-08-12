from flask import render_template, redirect, url_for, request
from main import app, db
from main.forms import Url_form
from string import ascii_letters, digits
from random import randint
from main.models import URL


domain = "127.0.0.1:5000/"
@app.route("/", methods=["POST", "GET"])
def home():
    form = Url_form()
    if form.validate_on_submit():
        new = f"{randomSringGenerator(5)}"
        U = URL(orginal_link =form.url.data,  new_link=new)
        db.session.add(U)
        db.session.commit()
        return redirect (url_for("New_url", new=new))
    return render_template("home.html", form=form)



@app.route("/New url/", methods=["POST", "GET"])
def New_url():
    form = Url_form()
    new = request.args.get("new")
    form.url.data = f"{domain}{new}"
    return render_template("r.html", form=form)


@app.route("/<used_url>", methods=["POST", "GET"])
def go_To_Url(used_url):
    print("hello")
    p = URL.query.filter_by(new_link=used_url).first()
    return redirect(p.orginal_link)


def randomSringGenerator(length):
    value =""
    for i in range(length):
        n = randint(0,9)
        l = randint(0, 25)
        value = f"{value}{ascii_letters[l]}{digits[n]}"
    return value
