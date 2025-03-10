from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmDmAddressBook(Base):
    __tablename__ = 'orocrm_dm_address_book'
    __table_args__ = (
        Index('orocrm_dm_address_book_unq', 'origin_id', 'channel_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_dm_address_book_id_seq'::regclass)"))
    owner_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    channel_id = Column(ForeignKey('oro_integration_channel.id', ondelete='SET NULL'), index=True)
    marketing_list_id = Column(ForeignKey('orocrm_marketing_list.id', ondelete='SET NULL'), unique=True)
    visibility_id = Column(ForeignKey('oro_enum_dm_ab_visibility.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    origin_id = Column(BigInteger)
    name = Column(String(255), nullable=False)
    contact_count = Column(Integer)
    last_exported_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    last_imported_at = Column(TIMESTAMP(precision=0), index=True, server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    create_entities = Column(Boolean)
    syncstatus_id = Column(ForeignKey('oro_enum_dm_import_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    channel = relationship('OroIntegrationChannel')
    marketing_list = relationship('OrocrmMarketingList')
    owner = relationship('OroOrganization')
    syncstatus = relationship('OroEnumDmImportStatu')
    visibility = relationship('OroEnumDmAbVisibility')
    campaigns = relationship('OrocrmDmCampaign', secondary='orocrm_dm_campaign_to_ab')


