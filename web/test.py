from app import db
from models import *

t = Post("Hello 3")
db.session.add(t)
db.session.commit()
