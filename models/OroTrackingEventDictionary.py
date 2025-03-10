from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTrackingEventDictionary(Base):
    __tablename__ = 'oro_tracking_event_dictionary'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tracking_event_dictionary_id_seq'::regclass)"))
    website_id = Column(ForeignKey('oro_tracking_website.id', ondelete='CASCADE'), index=True)
    name = Column(String(255), nullable=False)

    website = relationship('OroTrackingWebsite')


