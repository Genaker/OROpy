from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmDmActivity(Base):
    __tablename__ = 'orocrm_dm_activity'
    __table_args__ = (
        Index('orocrm_dm_activity_unq', 'campaign_id', 'contact_id', 'channel_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_dm_activity_id_seq'::regclass)"))
    owner_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    channel_id = Column(ForeignKey('oro_integration_channel.id', ondelete='SET NULL'), index=True)
    campaign_id = Column(ForeignKey('orocrm_dm_campaign.id', ondelete='CASCADE'), nullable=False, index=True)
    contact_id = Column(ForeignKey('orocrm_dm_contact.id', ondelete='CASCADE'), nullable=False, index=True)
    email = Column(String(255), nullable=False, index=True)
    num_opens = Column(Integer)
    num_page_views = Column(Integer)
    num_clicks = Column(Integer)
    num_forwards = Column(Integer)
    num_estimated_forwards = Column(Integer)
    num_replies = Column(Integer)
    date_sent = Column(TIMESTAMP(precision=0), index=True, server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    date_first_opened = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    date_last_opened = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    first_open_ip = Column(String(255), server_default=text("NULL::character varying"))
    unsubscribed = Column(Boolean)
    soft_bounced = Column(Boolean)
    hard_bounced = Column(Boolean)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')

    campaign = relationship('OrocrmDmCampaign')
    channel = relationship('OroIntegrationChannel')
    contact = relationship('OrocrmDmContact')
    owner = relationship('OroOrganization')


