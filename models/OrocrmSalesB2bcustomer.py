from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmSalesB2bcustomer(Base):
    __tablename__ = 'orocrm_sales_b2bcustomer'
    __table_args__ = (
        Index('orocrm_b2bcustomer_name_idx', 'name', 'id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_sales_b2bcustomer_id_seq'::regclass)"))
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    billing_address_id = Column(ForeignKey('oro_address.id', ondelete='SET NULL'), index=True)
    shipping_address_id = Column(ForeignKey('oro_address.id', ondelete='SET NULL'), index=True)
    data_channel_id = Column(ForeignKey('orocrm_channel.id', ondelete='SET NULL'), index=True)
    account_id = Column(ForeignKey('orocrm_account.id', ondelete='CASCADE'), index=True)
    contact_id = Column(ForeignKey('orocrm_contact.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False)
    lifetime = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)')
    createdat = Column(TIMESTAMP(precision=0), nullable=False)
    updatedat = Column(TIMESTAMP(precision=0), nullable=False)
    website = Column(String(255), index=True, server_default=text("NULL::character varying"))
    employees = Column(Integer, index=True)
    ownership = Column(String(255), index=True, server_default=text("NULL::character varying"))
    ticker_symbol = Column(String(255), index=True, server_default=text("NULL::character varying"))
    rating = Column(String(255), index=True, server_default=text("NULL::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))
    ac_last_contact_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_in = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_out = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_contact_count = Column(Integer)
    ac_contact_count_in = Column(Integer)
    ac_contact_count_out = Column(Integer)

    account = relationship('OrocrmAccount')
    billing_address = relationship('OroAddres', primaryjoin='OrocrmSalesB2bcustomer.billing_address_id == OroAddres.id')
    contact = relationship('OrocrmContact')
    data_channel = relationship('OrocrmChannel')
    organization = relationship('OroOrganization')
    shipping_address = relationship('OroAddres', primaryjoin='OrocrmSalesB2bcustomer.shipping_address_id == OroAddres.id')
    user_owner = relationship('OroUser')
    emails = relationship('OroEmail', secondary='oro_rel_26535370e65dd9d390636c')
    calendarevents = relationship('OroCalendarEvent', secondary='oro_rel_46a29d19e65dd9d390636c')
    calls = relationship('OrocrmCall', secondary='oro_rel_6cbc8000e65dd9d390636c')
    tasks = relationship('OrocrmTask', secondary='oro_rel_f24c741be65dd9d390636c')


