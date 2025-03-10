from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroProductCollectionSortOrder(Base):
    __tablename__ = 'oro_product_collection_sort_order'
    __table_args__ = (
        Index('product_segment_sort_uniq_idx', 'product_id', 'segment_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_product_collection_sort_order_id_seq'::regclass)"))
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)
    segment_id = Column(ForeignKey('oro_segment.id', ondelete='CASCADE'), nullable=False, index=True)
    sort_order = Column(Float(53))
    serialized_data = Column(JSONB(astext_type=Text()))

    product = relationship('OroProduct')
    segment = relationship('OroSegment')


