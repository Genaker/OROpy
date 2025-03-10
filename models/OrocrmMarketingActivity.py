from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmMarketingActivity(Base):
    __tablename__ = 'orocrm_marketing_activity'
    __table_args__ = (
        Index('idx_marketing_activity_entity', 'entity_id', 'entity_class'),
        Index('idx_marketing_activity_related_campaign', 'related_campaign_id', 'related_campaign_class')
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_marketing_activity_id_seq'::regclass)"))
    owner_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    campaign_id = Column(ForeignKey('orocrm_campaign.id', ondelete='SET NULL'), index=True)
    type_id = Column(ForeignKey('oro_enum_ma_type.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    entity_id = Column(Integer, nullable=False)
    entity_class = Column(String(255), nullable=False)
    related_campaign_id = Column(Integer)
    related_campaign_class = Column(String(255), server_default=text("NULL::character varying"))
    details = Column(Text)
    action_date = Column(TIMESTAMP(precision=0), nullable=False, index=True, comment='(DC2Type:datetime)')
    serialized_data = Column(JSONB(astext_type=Text()))

    campaign = relationship('OrocrmCampaign')
    owner = relationship('OroOrganization')
    type = relationship('OroEnumMaType')


