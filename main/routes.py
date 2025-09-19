from flask import render_template, request, redirect, abort
from main import application, db
from main.models import URL
from urllib.parse import urlparse
from main.utils import add_Url_to_database, randomSringGenerator, is_in_database, is_url_in_DB
import os 



@application.cli.command('create-db')
def create_database():
    """ Create the database if it does not exist."""
    if not os.path.exists('database.db'):  # Adjust for other DB types if needed
        db.create_all()
        print("Database created successfully!")
    else:
        print("Database already exists.")



def is_valid_url(url):
    try:
        parsed = urlparse(url)
        # Check if the scheme and netloc are present
        return all([parsed.scheme, parsed.netloc])
    except Exception:
        return False


@application.route("/", methods=["GET", "POST"])
def index():
    """
    Shows the homepage form
    """
    return render_template("index.html", form_data=None, error=None)


@application.route("/", methods=["POST"])
def link_shorten_form():
    """
    Handles form submissions for inputting links 
    """
    form_data = request.form.get("links")
        
    if not is_valid_url(form_data):
        return render_template("index.html", form_data=None, error="Not a valid URL")

    db_url = is_url_in_DB(form_data)
    if  db_url:
        # returns a URL already in the DB 
        link = f"{request.scheme}://{request.host}/{db_url.new_link}"
        return render_template("index.html", form_data=link, error=None)

    # when a new link needs to be generated 
    link = generate_new_link(form_data)
    if link:
        link = f"{request.scheme}://{request.host}/{link}"
        return render_template("index.html", form_data=link, error=None)

    return render_template("index.html", form_data=None, error="Cannot shorten link")


def generate_new_link(url: str) -> str:
    """
    Creates a string of length 5 
    checks if it is in the db and has 5 attempts until failure
    It then adds it to the DB 
    """
    new_url = randomSringGenerator(5)
    check = is_in_database(new_url)
    for _ in range(10):
        new_url = randomSringGenerator(5)
        check = is_in_database(new_url)

        if not check:
            add_Url_to_database(url, new_url)
            return new_url
    return "false"




@application.route("/<used_url>", methods=["GET"])
def go_To_Url(used_url):
    """
    Goes to the link if it is in the database
    """
    p = URL.query.filter_by(new_link=used_url).first()
    print(p)
    if p is None or p.orginal_link is None:
        abort(400)
    return redirect(p.orginal_link)


@application.errorhandler(400)
def page_not_found(e):
    return render_template("404.html")
