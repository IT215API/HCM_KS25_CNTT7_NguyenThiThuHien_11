from database import Base
from sqlalchemy import Column, Integer, String

class MeetingModel(Base):
    __tablename__ = "meeting_rooms"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    room_name = Column(String(200), nullable=False)
    floor = Column(String(200), nullable=False)
    capacity = Column(Integer, nullable=False)
    status = Column(String(200), nullable=False)