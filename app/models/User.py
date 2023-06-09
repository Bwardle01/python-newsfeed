# from app.db import Base
# from sqlalchemy import Column, Integer, String

# # class User(Base):
# #   # name is users 
# #   __tablename__ = 'users'
# #   # creating Id column that is a number and is primary 
# #   id = Column(Integer, primary_key=True)
# #   # Creating a username column that is a string of 50 char and cant be nothing
# #   username = Column(String(50), nullable=False)
# #   # Creating a email column that is a string of 50 char. Cant be nothing. Has to be unique and cant match any other email
# #   email = Column(String(50), nullable=False, unique=True)
# #   # createing a password column that is a string of 50 char. Cant be the same as any other password
# #   password = Column(String(100), nullable=False) 

from app.db import Base
from sqlalchemy import Column, Integer, String

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)