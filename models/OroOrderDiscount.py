from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroOrderDiscount(Base):
    __tablename__ = 'oro_order_discount'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_order_discount_id_seq'::regclass)"))
    order_id = Column(ForeignKey('oro_order.id', ondelete='CASCADE'), nullable=False, index=True)
    description = Column(Text)
    type = Column(String(255), server_default=text("NULL::character varying"))
    percent = Column(Float(53), comment='(DC2Type:percent)(DC2Type:percent)')
    amount = Column(Numeric(19, 4), nullable=False, comment='(DC2Type:money)(DC2Type:money)')

    order = relationship('OroOrder')


