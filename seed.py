from models import Pet, db
from app import app

db.drop_all()
db.create_all()

p1 = Pet(name="Daisy",species="Dog",photo_url="https://static.wikia.nocookie.net/animalcrossing/images/9/96/Daisy_NH.png/revision/latest?cb=20200802135104",notes="normal type",available=False)
p2 = Pet(name="Drift",species="Frog",photo_url="https://static.wikia.nocookie.net/animalcrossing/images/a/ac/Drift_NH.png/revision/latest?cb=20200802144841",notes="jock type",available=False)
p3 = Pet(name="Roswell",species="Alligator",photo_url="https://static.wikia.nocookie.net/animalcrossing/images/6/66/Roswell_NH.png/revision/latest?cb=20211020143906",notes="smug type",available=True)
p4 = Pet(name="Ozzie",species="Koala",photo_url="https://static.wikia.nocookie.net/animalcrossing/images/3/3a/Ozzie_NH.png/revision/latest/scale-to-width-down/350?cb=20200821055122",notes="lazy type",available=True)
p5 = Pet(name="Shino",species="Deer",photo_url="https://static.wikia.nocookie.net/animalcrossing/images/b/b0/Shino_NH.png/revision/latest?cb=20211020110951",notes="peppy type",available=False)
p6 = Pet(name="Paolo",species="Elephant",photo_url="https://static.wikia.nocookie.net/animalcrossing/images/5/59/Paolo_NH.png/revision/latest/scale-to-width-down/350?cb=20200728213208",notes="lazy type",available=False)

db.session.add_all([p1,p2,p3,p4,p5,p6])
db.session.commit()