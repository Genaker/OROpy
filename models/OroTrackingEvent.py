from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTrackingEvent(Base):
    __tablename__ = 'oro_tracking_event'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tracking_event_id_seq'::regclass)"))
    website_id = Column(ForeignKey('oro_tracking_website.id', ondelete='CASCADE'), index=True)
    name = Column(String(255), nullable=False, index=True)
    value = Column(Float(53))
    user_identifier = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    logged_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    url = Column(Text, nullable=False)
    title = Column(Text)
    code = Column(String(255), index=True, server_default=text("NULL::character varying"))
    parsed = Column(Boolean, nullable=False, index=True, server_default=text("false"))
    serialized_data = Column(JSONB(astext_type=Text()))

    website = relationship('OroTrackingWebsite')


