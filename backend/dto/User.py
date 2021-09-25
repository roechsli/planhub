from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    def __repr__(self):
        return "<User(id='%s', first_name='%s', last_name='%s', email='%s')>" % (
            self.id, self.first_name, self.last_name, self.email)
    
    def json(self):
        return {'id': self.id, 'first_name': self.first_name, 'last_name': self.last_name, 'email': self.email}
    
