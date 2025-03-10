from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmDmAbContact(Base):
    __tablename__ = 'orocrm_dm_ab_contact'
    __table_args__ = (
        Index('idx_marketing_list_item_class_id', 'marketing_list_item_class', 'marketing_list_item_id'),
        Index('orocrm_dm_ab_cnt_unq', 'address_book_id', 'contact_id', unique=True)
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_dm_ab_contact_id_seq'::regclass)"))
    contact_id = Column(ForeignKey('orocrm_dm_contact.id', ondelete='CASCADE'), nullable=False, index=True)
    channel_id = Column(ForeignKey('oro_integration_channel.id', ondelete='SET NULL'), index=True)
    address_book_id = Column(ForeignKey('orocrm_dm_address_book.id', ondelete='CASCADE'), nullable=False, index=True)
    status_id = Column(ForeignKey('oro_enum_dm_cnt_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    unsubscribed_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    marketing_list_item_id = Column(Integer)
    marketing_list_item_class = Column(String(255), server_default=text("NULL::character varying"))
    scheduled_for_export = Column(Boolean, nullable=False)
    export_id = Column(String(36), index=True, server_default=text("NULL::character varying"))
    new_entity = Column(Boolean)
    entity_updated = Column(Boolean)
    scheduled_for_fields_update = Column(Boolean)
    exportoperationtype_id = Column(ForeignKey('oro_enum_dm_ab_cnt_exp_type.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    address_book = relationship('OrocrmDmAddressBook')
    channel = relationship('OroIntegrationChannel')
    contact = relationship('OrocrmDmContact')
    exportoperationtype = relationship('OroEnumDmAbCntExpType')
    status = relationship('OroEnumDmCntStatu')


t_orocrm_dm_campaign_to_ab = Table(
    'orocrm_dm_campaign_to_ab', metadata,
    Column('campaign_id', ForeignKey('orocrm_dm_campaign.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('address_book_id', ForeignKey('orocrm_dm_address_book.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


