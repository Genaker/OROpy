from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroFedexShippingService(Base):
    __tablename__ = 'oro_fedex_shipping_service'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_fedex_shipping_service_id_seq'::regclass)"))
    rule_id = Column(ForeignKey('oro_fedex_ship_service_rule.id'), nullable=False, index=True)
    code = Column(String(200), nullable=False)
    description = Column(String(200), nullable=False)

    rule = relationship('OroFedexShipServiceRule')
    transports = relationship('OroIntegrationTransport', secondary='oro_fedex_transp_ship_service')


