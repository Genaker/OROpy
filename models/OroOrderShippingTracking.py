from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroOrderShippingTracking(Base):
    __tablename__ = 'oro_order_shipping_tracking'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_order_shipping_tracking_id_seq'::regclass)"))
    order_id = Column(ForeignKey('oro_order.id', ondelete='CASCADE'), nullable=False, index=True)
    method = Column(String(255), server_default=text("NULL::character varying"))
    number = Column(String(255), server_default=text("NULL::character varying"))

    order = relationship('OroOrder')


