from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Settings(Base):
    __tablename__ = 'settings'

    id = Column(String, primary_key=True)
    user_id = Column(String)
    days_at_home = Column(String)
    days_at_work = Column(String)
    commute_time = Column(Integer) 
    commute_time_unit = Column(String) 
    start_time = Column(String) 
    end_time = Column(String) 
    work_time = Column(Integer)
    work_time_unit = Column(String) 
    work_percentage = Column(Integer)

    def __repr__(self):
        return "<Settings(id='%s', user_id='%s', days_at_home='%s', days_at_work='%s', commute_time='%s', commute_time_unit='%s', start_time='%s', end_time='%s', work_time='%s', work_time_unit='%s', work_percentage= %s')>" % (
            self.id, self.user_id, self.days_at_home, self.days_at_work, self.commute_time, self.commute_time_unit, self.start_time, self.end_time, self.work_time, self.work_time_unit, self.work_percentage)

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'days_at_home': self.days_at_home,
            'days_at_work': self.days_at_work,
            'commute_time': self.commute_time,
            'commute_time_unit': self.commute_time_unit,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'work_time': self.work_time,
            'work_time_unit': self.work_time_unit,
            'work_percentage': self.work_percentage
        }