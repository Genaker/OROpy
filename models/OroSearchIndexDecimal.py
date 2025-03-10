from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroSearchIndexDecimal(Base):
    __tablename__ = 'oro_search_index_decimal'
    __table_args__ = (
        Index('oro_search_index_decimal_item_field_idx', 'item_id', 'field'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_search_index_decimal_id_seq'::regclass)"))
    item_id = Column(ForeignKey('oro_search_item.id', ondelete='CASCADE'), nullable=False, index=True)
    field = Column(String(250), nullable=False, index=True)
    value = Column(Numeric(21, 6), nullable=False)

    item = relationship('OroSearchItem')


