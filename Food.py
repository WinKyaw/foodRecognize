from .db import db

class food(db.Document)
    food_id = db.StringField(required=True, unique=True)
    food_name = db.StringField(required=True)
    
