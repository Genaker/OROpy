from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmDmCampaign(Base):
    __tablename__ = 'orocrm_dm_campaign'
    __table_args__ = (
        Index('orocrm_dm_campaign_unq', 'origin_id', 'channel_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_dm_campaign_id_seq'::regclass)"))
    owner_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    channel_id = Column(ForeignKey('oro_integration_channel.id', ondelete='SET NULL'), index=True)
    email_campaign_id = Column(ForeignKey('orocrm_campaign_email.id', ondelete='SET NULL'), unique=True)
    campaign_summary_id = Column(ForeignKey('orocrm_dm_campaign_summary.id', ondelete='SET NULL'), unique=True)
    reply_action_id = Column(ForeignKey('oro_enum_dm_cmp_reply_action.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    status_id = Column(ForeignKey('oro_enum_dm_cmp_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    origin_id = Column(BigInteger)
    name = Column(String(255), nullable=False)
    subject = Column(String(255), server_default=text("NULL::character varying"))
    from_name = Column(String(255), server_default=text("NULL::character varying"))
    from_address = Column(String(255), server_default=text("NULL::character varying"))
    html_content = Column(Text)
    plain_text_content = Column(Text)
    reply_to_address = Column(String(255), server_default=text("NULL::character varying"))
    is_split_test = Column(Boolean)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    is_deleted = Column(Boolean, nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    campaign_summary = relationship('OrocrmDmCampaignSummary', primaryjoin='OrocrmDmCampaign.campaign_summary_id == OrocrmDmCampaignSummary.id')
    channel = relationship('OroIntegrationChannel')
    email_campaign = relationship('OrocrmCampaignEmail')
    owner = relationship('OroOrganization')
    reply_action = relationship('OroEnumDmCmpReplyAction')
    status = relationship('OroEnumDmCmpStatu')


