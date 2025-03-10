from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWebsiteSearchSuggestionProduct(Base):
    __tablename__ = 'oro_website_search_suggestion_product'
    __table_args__ = (
        Index('product_suggestion_unique', 'suggestion_id', 'product_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_website_search_suggestion_product_id_seq'::regclass)"))
    suggestion_id = Column(ForeignKey('oro_website_search_suggestion.id', ondelete='CASCADE'), nullable=False, index=True)
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    product = relationship('OroProduct')
    suggestion = relationship('OroWebsiteSearchSuggestion')


