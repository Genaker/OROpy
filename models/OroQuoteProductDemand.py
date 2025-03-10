from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroQuoteProductDemand(Base):
    __tablename__ = 'oro_quote_product_demand'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_quote_product_demand_id_seq'::regclass)"))
    quote_demand_id = Column(ForeignKey('oro_quote_demand.id', ondelete='CASCADE'), index=True)
    quote_product_offer_id = Column(ForeignKey('oro_sale_quote_prod_offer.id', ondelete='CASCADE'), index=True)
    quantity = Column(Float(53), nullable=False)
    checksum = Column(String(40), nullable=False, server_default=text("''::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    quote_demand = relationship('OroQuoteDemand')
    quote_product_offer = relationship('OroSaleQuoteProdOffer')


