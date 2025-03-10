from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmTaskPriority(Base):
    __tablename__ = 'orocrm_task_priority'

    name = Column(String(32), primary_key=True)
    label = Column(String(255), nullable=False, unique=True)
    order = Column(Integer, nullable=False)


