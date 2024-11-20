from flask import render_template, request, redirect, abort
from main import application, db
from main.models import URL
from urllib.parse import urlparse
from main.utils import add_Url_to_database, randomSringGenerator, is_in_database, is_url_in_DB
import os 



@application.cli.command('create-db')
def create_database():
    """Create the database if it does not exist."""
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
    new_link = None
    error  = None

    if request.method == "POST":
        form_data = request.form.get("links")
        if is_valid_url(form_data):
            check  = is_url_in_DB(form_data)
            if check:
                new_link = f"{request.scheme}://{request.host}/{check.new_link}"
            else:
                link = generate_new_link(form_data)
                if link:
                    new_link = f"{request.scheme}://{request.host}/{link}"
                else:
                    error = "Cannot shorten link"
        else:
            error = "Not a valid URL"
    return render_template("index.html", form_data=new_link, error=error)


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
    Goes to the link if it is in the databse
    """
    p = URL.query.filter_by(new_link=used_url).first()
    if p is None or p.orginal_link is None:
        abort(400)
    return redirect(p.orginal_link)


@application.errorhandler(400)
def page_not_found(e):
    return render_template("404.html")