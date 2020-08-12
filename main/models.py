from main import db


class URL(db.Model):
    __tablename__ = "links"
    id = db.Column(db.Integer, primary_key= True)
    orginal_link =db.Column(db.String(350), nullable=False)
    new_link = db.Column(db.String(200), unique= True, nullable= False)

    def __repr__(self):
        return f"URL ('{self.orginal_link}', '{self.new_link}' )"
