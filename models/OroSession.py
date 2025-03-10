from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroSession(Base):
    __tablename__ = 'oro_session'

    id = Column(String(128), primary_key=True)
    sess_data = Column(LargeBinary, nullable=False)
    sess_time = Column(Integer, nullable=False)
    sess_lifetime = Column(Integer, nullable=False)


