from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroRfpRequestProdItem(Base):
    __tablename__ = 'oro_rfp_request_prod_item'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_rfp_request_prod_item_id_seq'::regclass)"))
    product_unit_id = Column(ForeignKey('oro_product_unit.code', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    request_product_id = Column(ForeignKey('oro_rfp_request_product.id', ondelete='CASCADE'), index=True)
    quantity = Column(Float(53))
    product_unit_code = Column(String(255), nullable=False)
    value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    currency = Column(String(3), server_default=text("NULL::character varying"))
    checksum = Column(String(40), nullable=False, server_default=text("''::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    product_unit = relationship('OroProductUnit')
    request_product = relationship('OroRfpRequestProduct')


