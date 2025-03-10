from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroSaleQuoteProduct(Base):
    __tablename__ = 'oro_sale_quote_product'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_sale_quote_product_id_seq'::regclass)"))
    product_id = Column(ForeignKey('oro_product.id', ondelete='SET NULL'), index=True)
    product_replacement_id = Column(ForeignKey('oro_product.id', ondelete='SET NULL'), index=True)
    quote_id = Column(ForeignKey('oro_sale_quote.id', ondelete='CASCADE'), index=True)
    product_sku = Column(String(255), server_default=text("NULL::character varying"))
    product_replacement_sku = Column(String(255), server_default=text("NULL::character varying"))
    type = Column(SmallInteger)
    free_form_product = Column(String(255), server_default=text("NULL::character varying"))
    free_form_product_replacement = Column(String(255), server_default=text("NULL::character varying"))
    comment = Column(Text)
    comment_customer = Column(Text)
    serialized_data = Column(JSONB(astext_type=Text()))

    product = relationship('OroProduct', primaryjoin='OroSaleQuoteProduct.product_id == OroProduct.id')
    product_replacement = relationship('OroProduct', primaryjoin='OroSaleQuoteProduct.product_replacement_id == OroProduct.id')
    quote = relationship('OroSaleQuote')


