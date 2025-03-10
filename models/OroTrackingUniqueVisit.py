from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTrackingUniqueVisit(Base):
    __tablename__ = 'oro_tracking_unique_visit'
    __table_args__ = (
        Index('uvisit_user_by_date_idx', 'user_identifier', 'action_date'),
        Index('uvisit_action_date_idx', 'website_id', 'action_date')
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tracking_unique_visit_id_seq'::regclass)"))
    website_id = Column(ForeignKey('oro_tracking_website.id', ondelete='CASCADE'), index=True)
    visit_count = Column(Integer, nullable=False)
    user_identifier = Column(String(32), nullable=False)
    action_date = Column(Date, nullable=False)

    website = relationship('OroTrackingWebsite')


