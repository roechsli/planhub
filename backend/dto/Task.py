from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(String, primary_key=True)
    user_id = Column(String)
    name = Column(String)
    description = Column(String)
    duration = Column(Integer)
    duration_unit = Column(String)
    visibility = Column(String)
    location = Column(String)
    priority = Column(Integer)
    recurrence_id = Column(String)
    milestone_id = Column(String)
    start_time = Column(DateTime)
    guests = Column(String)
    status = Column(String)

    def __repr__(self):
        return "<Task(id='%s', user_id='%s', name='%s', guests='%s', " \
               "description='%s', duration='%s', duration_unit='%s', " \
               "visibility='%s', location='%s', priority='%s' " \
               "recurrence_id='%s', milestone_id='%s', start_time='%s', guests='%s', status='%s')>" % \
               (
                   self.id, self.user_id, self.name, self.id, self.guests,
                   self.description, self.duration, self.duration_unit,
                   self.visibility, self.location, self.priority,
                   self.recurrence_id, self.milestone_id, self.start_time, self.guests, self.status
                   )

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'id': self.id,
            'guests': self.guests,
            'description': self.description,
            'duration': self.duration,
            'duration_unit': self.duration_unit,
            'visibility': self.visibility,
            'location': self.location,
            'priority': self.priority,
            'recurrence_id': self.recurrence_id,
            'milestone_id': self.milestone_id,
            'start_time': self.start_time,
            'guests': self.guests,
            'status': self.status
        }
    
