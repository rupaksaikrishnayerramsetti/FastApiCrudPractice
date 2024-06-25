from sqlalchemy import Boolean, Column, Integer, String, VARCHAR

from Config.database import Base

class Student(Base):
    __tablename__ = "students"
    reg_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50), index=True)
    email = Column(VARCHAR(100), index=True)
    branch = Column(VARCHAR(50), index=True)
    section = Column(VARCHAR(3), index=True)
    is_deleted = Column(Boolean, default=False)
