from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroShipMethodPostalCode(Base):
    __tablename__ = 'oro_ship_method_postal_code'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_ship_method_postal_code_id_seq'::regclass)"))
    destination_id = Column(ForeignKey('oro_shipping_rule_destination.id', ondelete='CASCADE'), nullable=False, index=True)
    name = Column(String(255), nullable=False)

    destination = relationship('OroShippingRuleDestination')


