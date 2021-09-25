from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(String)
    guests = Column(String)
    description = Column(String)
    duration = Column(Integer)
    duration_unit = Column(String)
    visibility = Column(String)
    location = Column(String)
    priority = Column(Integer)

    def __repr__(self):
        return "<Task(id='%s', user_id='%s', name='%s', guests='%s', " \
               "description='%s', duration='%s', duration_unit='%s', " \
               "visibility='%s', location='%s', priority='%s')>" % \
               (
                   self.id, self.user_id, self.name, self.id, self.guests,
                   self.description, self.duration, self.duration_unit,
                   self.visibility, self.location, self.priority
               )
