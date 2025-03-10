from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmCampaignTeSummary(Base):
    __tablename__ = 'orocrm_campaign_te_summary'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_campaign_te_summary_id_seq'::regclass)"))
    website_id = Column(ForeignKey('oro_tracking_website.id', ondelete='CASCADE'), index=True)
    name = Column(String(255), nullable=False, index=True)
    code = Column(String(255), index=True, server_default=text("NULL::character varying"))
    visit_count = Column(Integer, nullable=False, index=True)
    logged_at = Column(Date, nullable=False, index=True)

    website = relationship('OroTrackingWebsite')


