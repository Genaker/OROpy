from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTrackingDatum(Base):
    __tablename__ = 'oro_tracking_data'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tracking_data_id_seq'::regclass)"))
    event_id = Column(ForeignKey('oro_tracking_event.id', ondelete='CASCADE'), unique=True)
    data = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)

    event = relationship('OroTrackingEvent')


