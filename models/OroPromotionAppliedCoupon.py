from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPromotionAppliedCoupon(Base):
    __tablename__ = 'oro_promotion_applied_coupon'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_promotion_applied_coupon_id_seq'::regclass)"))
    applied_promotion_id = Column(ForeignKey('oro_promotion_applied.id', ondelete='CASCADE'), unique=True)
    order_id = Column(ForeignKey('oro_order.id', ondelete='CASCADE'), index=True)
    checkout_id = Column(ForeignKey('oro_checkout.id', ondelete='CASCADE'), index=True)
    coupon_code = Column(String(255), nullable=False)
    source_promotion_id = Column(Integer, nullable=False)
    source_coupon_id = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    applied_promotion = relationship('OroPromotionApplied')
    checkout = relationship('OroCheckout')
    order = relationship('OroOrder')


