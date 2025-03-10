from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroUpsShippingService(Base):
    __tablename__ = 'oro_ups_shipping_service'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_ups_shipping_service_id_seq'::regclass)"))
    country_code = Column(ForeignKey('oro_dictionary_country.iso2_code'), nullable=False, index=True)
    code = Column(String(10), nullable=False)
    description = Column(String(255), nullable=False)

    oro_dictionary_country = relationship('OroDictionaryCountry')
    transports = relationship('OroIntegrationTransport', secondary='oro_ups_transport_ship_service')


t_oro_user_access_role = Table(
    'oro_user_access_role', metadata,
    Column('user_id', ForeignKey('oro_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('role_id', ForeignKey('oro_access_role.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


