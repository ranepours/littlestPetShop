from flask import Flask, render_template, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, connect_db, db
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

connect_db(app)
db.create_all()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'KEY'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def render_home():
    """RENDER HOME PAGE"""
    pets=Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=["POST","GET"])
def add_pet():
    """RENDER & VALIDATE ADD PET FORM"""
    form = AddPetForm()
    if form.validate_on_submit():
        data={k:v for k,v in form.data.items() if k!="csrf_token"}
        new_pet=Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('render_home'))
    else:  
        return render_template('add.html',form=form)


@app.route("/<int:pet_id>", methods=["POST", "GET"])
def update_pet(pet_id):
    """RENDER & VALIDATE UPDATE PET FORM"""
    pet=Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.available=form.available.data
        pet.notes=form.notes.data
        pet.photo_url=form.photo_url.data
        db.session.commit()
        return redirect(url_for('render_home'))
    else:  
        return render_template('update.html',form=form,pet=pet)