from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class RemembermeToken(Base):
    __tablename__ = 'rememberme_token'

    series = Column(CHAR(88), primary_key=True)
    value = Column(String(88), nullable=False)
    lastused = Column(TIMESTAMP(precision=0), nullable=False)
    _class = Column('class', String(255), nullable=False)
    username = Column(String(255), nullable=False)


