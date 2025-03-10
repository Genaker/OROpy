from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPriceRule(Base):
    __tablename__ = 'oro_price_rule'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_price_rule_id_seq'::regclass)"))
    product_unit_id = Column(ForeignKey('oro_product_unit.code', ondelete='CASCADE'), index=True, server_default=text("NULL::character varying"))
    price_list_id = Column(ForeignKey('oro_price_list.id', ondelete='CASCADE'), nullable=False, index=True)
    currency = Column(String(3), server_default=text("NULL::character varying"))
    quantity = Column(Float(53))
    rule_condition = Column(Text)
    rule = Column(Text, nullable=False)
    priority = Column(Integer, nullable=False)
    quantity_expression = Column(Text)
    currency_expression = Column(Text)
    product_unit_expression = Column(Text)

    price_list = relationship('OroPriceList')
    product_unit = relationship('OroProductUnit')


