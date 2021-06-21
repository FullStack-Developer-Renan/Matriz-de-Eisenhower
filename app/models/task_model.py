from sqlalchemy.sql.sqltypes import Text, VARCHAR
from app import db

from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, ForeignKey


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)

    name = Column(VARCHAR(100), nullable=False, unique=True)
    description = Column(Text)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)
    eisenhower_id = Column(
        Integer, ForeignKey("eisenhowers.id"), nullable=False
    )

    task = relationship("EisenhowerModel", backref=backref("eisenhower_list"))

    def __repr__(self):
        return f"{self.id}" + ',' + f"{self.name}" + ',' + f"{self.eisenhower_id}"