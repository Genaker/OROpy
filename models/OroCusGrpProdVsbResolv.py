from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCusGrpProdVsbResolv(Base):
    __tablename__ = 'oro_cus_grp_prod_vsb_resolv'

    scope_id = Column(ForeignKey('oro_scope.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    source_product_visibility = Column(ForeignKey('oro_cus_grp_prod_visibility.id', ondelete='CASCADE'), index=True)
    category_id = Column(ForeignKey('oro_catalog_category.id', ondelete='CASCADE'), index=True)
    visibility = Column(SmallInteger)
    source = Column(SmallInteger)

    category = relationship('OroCatalogCategory')
    product = relationship('OroProduct')
    scope = relationship('OroScope')
    oro_cus_grp_prod_visibility = relationship('OroCusGrpProdVisibility')


