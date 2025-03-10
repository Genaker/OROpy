from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPromotionAppliedDiscount(Base):
    __tablename__ = 'oro_promotion_applied_discount'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_promotion_applied_discount_id_seq'::regclass)"))
    line_item_id = Column(ForeignKey('oro_order_line_item.id', ondelete='CASCADE'), index=True)
    applied_promotion_id = Column(ForeignKey('oro_promotion_applied.id', ondelete='CASCADE'), nullable=False, index=True)
    amount = Column(Numeric(19, 4), nullable=False, comment='(DC2Type:money_value)(DC2Type:money_value)')
    currency = Column(String(3), nullable=False, comment='(DC2Type:currency)(DC2Type:currency)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    applied_promotion = relationship('OroPromotionApplied')
    line_item = relationship('OroOrderLineItem')


