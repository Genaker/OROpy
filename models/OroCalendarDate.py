from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCalendarDate(Base):
    __tablename__ = 'oro_calendar_date'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_calendar_date_id_seq'::regclass)"))
    date = Column(Date, nullable=False, unique=True, comment='(DC2Type:date)')


