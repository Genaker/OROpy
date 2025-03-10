from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmCampaignEmail(Base):
    __tablename__ = 'orocrm_campaign_email'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_campaign_email_id_seq'::regclass)"))
    campaign_id = Column(ForeignKey('orocrm_campaign.id', ondelete='SET NULL'), index=True)
    transport_settings_id = Column(ForeignKey('orocrm_cmpgn_transport_stngs.id', ondelete='SET NULL'), unique=True)
    marketing_list_id = Column(ForeignKey('orocrm_marketing_list.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    is_sent = Column(Boolean, nullable=False)
    schedule = Column(String(255), nullable=False)
    scheduled_for = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    sender_email = Column(String(255), server_default=text("NULL::character varying"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    sent_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    sender_name = Column(String(255), server_default=text("NULL::character varying"))
    transport = Column(String(255), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    campaign = relationship('OrocrmCampaign')
    marketing_list = relationship('OrocrmMarketingList')
    organization = relationship('OroOrganization')
    owner = relationship('OroUser')
    transport_settings = relationship('OrocrmCmpgnTransportStng')


t_orocrm_contactus_req_emails = Table(
    'orocrm_contactus_req_emails', metadata,
    Column('request_id', ForeignKey('orocrm_contactus_request.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


