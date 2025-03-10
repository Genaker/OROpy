from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCusGrpCtgrVsbResolv(Base):
    __tablename__ = 'oro_cus_grp_ctgr_vsb_resolv'

    category_id = Column(ForeignKey('oro_catalog_category.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    scope_id = Column(ForeignKey('oro_scope.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    source_category_visibility = Column(ForeignKey('oro_cus_grp_ctgr_visibility.id', ondelete='CASCADE'), index=True)
    visibility = Column(SmallInteger)
    source = Column(SmallInteger)

    category = relationship('OroCatalogCategory')
    scope = relationship('OroScope')
    oro_cus_grp_ctgr_visibility = relationship('OroCusGrpCtgrVisibility')


