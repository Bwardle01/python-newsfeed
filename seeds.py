from app.models import User
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

#insert users
db.add_all([
  User(username='jimmy', email="jimmy@abc.com", password="password123"),
  User(username='bobby', email="bobby@abc.com", password="password123"),
  User(username='slobby', email="slobby@abc.com", password="password123"),
  User(username='tobby', email="tobby@abc.com", password="password123"),
  User(username='yobby', email="yobby@abc.com", password="password123"),
])

db.commit()

db.close()