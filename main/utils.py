from main.models import URL
from string import ascii_letters, digits
from random import randint
from main import db



def add_Url_to_database(orginal_link, new_url):
    U = URL(orginal_link = orginal_link,  new_link=new_url)
    db.session.add(U)
    db.session.commit()


def is_in_database(url):
    data = URL.query.filter_by(new_link=url)
    if data is None:
        return True
    return False
    


# functions and stuff
def randomSringGenerator(length):
    value = ""
    for _ in range(length):
        n = randint(0, 9)
        l = randint(0, 25)
        value = f"{value}{ascii_letters[l]}{digits[n]}"
    return value
