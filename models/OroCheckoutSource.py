from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCheckoutSource(Base):
    __tablename__ = 'oro_checkout_source'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_checkout_source_id_seq'::regclass)"))
    order_id = Column(ForeignKey('oro_order.id', ondelete='SET NULL'), index=True)
    deleted = Column(Boolean, nullable=False, server_default=text("false"))
    quotedemand_id = Column(ForeignKey('oro_quote_demand.id', ondelete='SET NULL'), index=True)
    shoppinglist_id = Column(ForeignKey('oro_shopping_list.id', ondelete='SET NULL'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    order = relationship('OroOrder')
    quotedemand = relationship('OroQuoteDemand')
    shoppinglist = relationship('OroShoppingList')


