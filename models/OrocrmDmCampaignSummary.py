from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmDmCampaignSummary(Base):
    __tablename__ = 'orocrm_dm_campaign_summary'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_dm_campaign_summary_id_seq'::regclass)"))
    owner_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    channel_id = Column(ForeignKey('oro_integration_channel.id', ondelete='SET NULL'), index=True)
    campaign_id = Column(ForeignKey('orocrm_dm_campaign.id', ondelete='CASCADE'), nullable=False, unique=True)
    date_sent = Column(TIMESTAMP(precision=0), index=True, server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    num_unique_opens = Column(Integer)
    num_unique_text_opens = Column(Integer)
    num_total_unique_opens = Column(Integer)
    num_opens = Column(Integer)
    num_text_opens = Column(Integer)
    num_total_opens = Column(Integer)
    num_clicks = Column(Integer)
    num_text_clicks = Column(Integer)
    num_total_clicks = Column(Integer)
    num_page_views = Column(Integer)
    num_total_page_views = Column(Integer)
    num_text_page_views = Column(Integer)
    num_forwards = Column(Integer)
    num_text_forwards = Column(Integer)
    num_estimated_forwards = Column(Integer)
    num_text_estimated_forwards = Column(Integer)
    num_total_estimated_forwards = Column(Integer)
    num_replies = Column(Integer)
    num_text_replies = Column(Integer)
    num_total_replies = Column(Integer)
    num_hard_bounces = Column(Integer)
    num_text_hard_bounces = Column(Integer)
    num_total_hard_bounces = Column(Integer)
    num_soft_bounces = Column(Integer)
    num_text_soft_bounces = Column(Integer)
    num_total_soft_bounces = Column(Integer)
    num_unsubscribes = Column(Integer)
    num_text_unsubscribes = Column(Integer)
    num_total_unsubscribes = Column(Integer)
    num_isp_complaints = Column(Integer)
    num_text_isp_complaints = Column(Integer)
    num_total_isp_complaints = Column(Integer)
    num_mail_blocks = Column(Integer)
    num_text_mail_blocks = Column(Integer)
    num_total_mail_blocks = Column(Integer)
    num_sent = Column(Integer)
    num_text_sent = Column(Integer)
    num_total_sent = Column(Integer)
    num_recipients_clicked = Column(Integer)
    num_delivered = Column(Integer)
    num_text_delivered = Column(Integer)
    num_total_delivered = Column(Integer)
    percentage_delivered = Column(Float(53))
    percentage_unique_opens = Column(Float(53))
    percentage_opens = Column(Float(53))
    percentage_unsubscribes = Column(Float(53))
    percentage_replies = Column(Float(53))
    percentage_hard_bounces = Column(Float(53))
    percentage_soft_bounces = Column(Float(53))
    percentage_users_clicked = Column(Float(53))
    percentage_clicks_to_opens = Column(Float(53))
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')

    campaign = relationship('OrocrmDmCampaign', primaryjoin='OrocrmDmCampaignSummary.campaign_id == OrocrmDmCampaign.id')
    channel = relationship('OroIntegrationChannel')
    owner = relationship('OroOrganization')


