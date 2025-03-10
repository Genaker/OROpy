from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCalendarRecurrence(Base):
    __tablename__ = 'oro_calendar_recurrence'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_calendar_recurrence_id_seq'::regclass)"))
    recurrence_type = Column(String(16), nullable=False)
    interval = Column(Integer, nullable=False)
    instance = Column(Integer)
    day_of_week = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    day_of_month = Column(Integer)
    month_of_year = Column(Integer)
    start_time = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    end_time = Column(TIMESTAMP(precision=0), index=True, server_default=text("NULL::timestamp without time zone"))
    calculated_end_time = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    occurrences = Column(Integer)
    timezone = Column(String(255), nullable=False)


