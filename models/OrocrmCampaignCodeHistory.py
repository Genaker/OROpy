from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmCampaignCodeHistory(Base):
    __tablename__ = 'orocrm_campaign_code_history'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_campaign_code_history_id_seq'::regclass)"))
    campaign_id = Column(ForeignKey('orocrm_campaign.id', ondelete='CASCADE'), nullable=False, index=True)
    code = Column(String(255), nullable=False, unique=True)

    campaign = relationship('OrocrmCampaign')


