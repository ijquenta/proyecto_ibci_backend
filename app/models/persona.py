from . import db

class Persona(db.Model):
    __tablename__ = 'persona'
    __table_args__ = {'schema': 'academico'}
    perid = db.Column(db.Integer, primary_key=True)
    pernomcompleto = db.Column(db.String)
    pernombres = db.Column(db.String(100), nullable=False)
    perapepat = db.Column(db.String(100))
    perapemat = db.Column(db.String(100))
    pertipodoc = db.Column(db.Integer)
    pernrodoc = db.Column(db.Integer)
    perfecnac = db.Column(db.Date)
    perdirec = db.Column(db.Text)
    peremail = db.Column(db.String(100))
    percelular = db.Column(db.String(20))
    pertelefono = db.Column(db.String(20))
    perpais = db.Column(db.Integer)
    perciudad = db.Column(db.Integer)
    pergenero = db.Column(db.Integer)
    perestcivil = db.Column(db.Integer)
    perfoto = db.Column(db.String)
    perestado = db.Column(db.SmallInteger, default=1)
    perobservacion = db.Column(db.String(255))
    perusureg = db.Column(db.String(50))
    perfecreg = db.Column(db.TIMESTAMP, default=db.func.now())
    perusumod = db.Column(db.String(50))
    perfecmod = db.Column(db.TIMESTAMP)