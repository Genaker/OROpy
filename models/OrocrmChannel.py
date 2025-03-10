from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmChannel(Base):
    __tablename__ = 'orocrm_channel'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_channel_id_seq'::regclass)"))
    organization_owner_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    data_source_id = Column(ForeignKey('oro_integration_channel.id', ondelete='SET NULL'), unique=True)
    name = Column(String(255), nullable=False, index=True)
    status = Column(Boolean, nullable=False, index=True)
    channel_type = Column(String(255), nullable=False, index=True)
    data = Column(JSON, comment='(DC2Type:json_array)(DC2Type:json_array)')
    customer_identity = Column(String(255), nullable=False)
    createdat = Column(TIMESTAMP(precision=0), nullable=False)
    updatedat = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))

    data_source = relationship('OroIntegrationChannel')
    organization_owner = relationship('OroOrganization')


t_orocrm_contact_adr_to_adr_type = Table(
    'orocrm_contact_adr_to_adr_type', metadata,
    Column('contact_address_id', ForeignKey('orocrm_contact_address.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('type_name', ForeignKey('oro_address_type.name'), primary_key=True, nullable=False, index=True)
)


