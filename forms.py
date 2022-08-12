from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, URL, Optional, NumberRange

class AddPetForm(FlaskForm):
    """add pet"""
    name = StringField("Pet Name", 
            validators=[InputRequired()])
    age=IntegerField("Age", 
            validators=[Optional()])
    notes=TextAreaField("Comments", 
            validators=[Optional(), Length(min=20), NumberRange(min=0,max=30)])
    photo_url=StringField("Photo URL", 
            validators=[Optional(), URL()])
    species = SelectField("Species", 
            choices=[('alligator','alligator'),
                    ('anteater','anteater'),
                    ('bear','bear'),
                    ('bird','bird'),
                    ('bull','bull'),
                    ('cat','cat'),
                    ('chicken','chicken'),
                    ('cow','cow'),
                    ('cub','cub'),
                    ('deer','deer'),
                    ('dog','dog'),
                    ('duck','duck'),
                    ('eagle','eagle'),
                    ('elephant','elephant'),
                    ('frog','frog'),
                    ('goat','goat'),
                    ('gorilla','gorilla'),
                    ('hamster','hamster'),
                    ('hippo','hippo'),
                    ('horse','horse'),
                    ('kangaroo','kangaroo'),
                    ('koala','koala'),
                    ('lion','lion'),
                    ('mouse','mouse'),
                    ('monkey','monkey'),
                    ('octopus','octopus'),
                    ('ostrich','ostrich'),
                    ('penguin','penguin'),
                    ('pig','pig'),
                    ("rabbit",'rabbit'),
                    ('rhino','rhino'),
                    ('sheep','sheep'),
                    ('squirrel','squirrel'),
                    ('tiger','tiger'),
                    ('wolf','wolf')])

class EditPetForm(FlaskForm):
    """edit pet"""
    photo_url=StringField("Photo URL", validators=[Optional(), URL()])
    notes=TextAreaField("Comments", validators=[Optional(), Length(min=20)])
    available=BooleanField("Available")