from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCheckoutSubtotal(Base):
    __tablename__ = 'oro_checkout_subtotal'
    __table_args__ = (
        Index('unique_checkout_currency', 'checkout_id', 'currency', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_checkout_subtotal_id_seq'::regclass)"))
    checkout_id = Column(ForeignKey('oro_checkout.id', ondelete='CASCADE'), nullable=False, index=True)
    combined_price_list_id = Column(ForeignKey('oro_price_list_combined.id', ondelete='SET NULL'), index=True)
    price_list_id = Column(ForeignKey('oro_price_list.id', ondelete='SET NULL'), index=True)
    currency = Column(String(255), nullable=False)
    value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    is_valid = Column(Boolean, nullable=False, index=True)

    checkout = relationship('OroCheckout')
    combined_price_list = relationship('OroPriceListCombined')
    price_list = relationship('OroPriceList')


