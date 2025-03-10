from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroSaleQuoteProdRequest(Base):
    __tablename__ = 'oro_sale_quote_prod_request'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_sale_quote_prod_request_id_seq'::regclass)"))
    product_unit_id = Column(ForeignKey('oro_product_unit.code', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    request_product_item_id = Column(ForeignKey('oro_rfp_request_prod_item.id', ondelete='CASCADE'), index=True)
    quote_product_id = Column(ForeignKey('oro_sale_quote_product.id', ondelete='CASCADE'), index=True)
    product_unit_code = Column(String(255), nullable=False)
    quantity = Column(Float(53))
    value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    currency = Column(String(255), server_default=text("NULL::character varying"))
    checksum = Column(String(40), nullable=False, server_default=text("''::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    product_unit = relationship('OroProductUnit')
    quote_product = relationship('OroSaleQuoteProduct')
    request_product_item = relationship('OroRfpRequestProdItem')


