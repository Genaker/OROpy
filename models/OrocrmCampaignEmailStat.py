from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmCampaignEmailStat(Base):
    __tablename__ = 'orocrm_campaign_email_stats'
    __table_args__ = (
        Index('orocrm_ec_litem_unq', 'email_campaign_id', 'marketing_list_item_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_campaign_email_stats_id_seq'::regclass)"))
    email_campaign_id = Column(ForeignKey('orocrm_campaign_email.id', ondelete='CASCADE'), nullable=False, index=True)
    marketing_list_item_id = Column(ForeignKey('orocrm_marketing_list_item.id', ondelete='CASCADE'), nullable=False, index=True)
    owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    open_count = Column(Integer)
    click_count = Column(Integer)
    bounce_count = Column(Integer)
    abuse_count = Column(Integer)
    unsubscribe_count = Column(Integer)
    serialized_data = Column(JSONB(astext_type=Text()))

    email_campaign = relationship('OrocrmCampaignEmail')
    marketing_list_item = relationship('OrocrmMarketingListItem')
    organization = relationship('OroOrganization')
    owner = relationship('OroUser')


