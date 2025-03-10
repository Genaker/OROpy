from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroIntegrationChannel(Base):
    __tablename__ = 'oro_integration_channel'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_integration_channel_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    transport_id = Column(ForeignKey('oro_integration_transport.id'), unique=True)
    default_user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    default_business_unit_owner_id = Column(ForeignKey('oro_business_unit.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False, index=True)
    type = Column(String(255), nullable=False)
    connectors = Column(Text, nullable=False, comment='(DC2Type:array)(DC2Type:array)')
    synchronization_settings = Column(JSON, nullable=False, comment='(DC2Type:config_object)(DC2Type:config_object)')
    mapping_settings = Column(JSON, nullable=False, comment='(DC2Type:config_object)(DC2Type:config_object)')
    enabled = Column(Boolean)
    edit_mode = Column(Integer, nullable=False, server_default=text("3"))
    previously_enabled = Column(Boolean)

    default_business_unit_owner = relationship('OroBusinessUnit')
    default_user_owner = relationship('OroUser')
    organization = relationship('OroOrganization')
    transport = relationship('OroIntegrationTransport')


