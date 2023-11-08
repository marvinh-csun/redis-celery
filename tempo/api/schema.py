from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from models import Business,User

class UserSchema(SQLAlchemySchema):
    class Meta:
        model =  User
        load_instance = True
    id=auto_field()
    name=auto_field()
    email=auto_field()

class BusinessSchema(SQLAlchemySchema):
    class Meta:
        model = Business
        load_instance = True  # Optional: deserialize to model instances

    business_id = auto_field()
    name = auto_field()
    address = auto_field()
    city = auto_field()
    state = auto_field()
    postal_code = auto_field()
    stars = auto_field()
    review_count = auto_field()
    is_open = auto_field()
    categories = auto_field()
