from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCategoryVisibility(Base):
    __tablename__ = 'oro_category_visibility'
    __table_args__ = (
        Index('oro_ctgr_vis_uidx', 'category_id', 'scope_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_category_visibility_id_seq'::regclass)"))
    category_id = Column(ForeignKey('oro_catalog_category.id', ondelete='CASCADE'), index=True)
    scope_id = Column(ForeignKey('oro_scope.id', ondelete='CASCADE'), nullable=False, index=True)
    visibility = Column(String(255), server_default=text("NULL::character varying"))

    category = relationship('OroCatalogCategory')
    scope = relationship('OroScope')


t_oro_cms_content_block_scope = Table(
    'oro_cms_content_block_scope', metadata,
    Column('content_block_id', ForeignKey('oro_cms_content_block.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('scope_id', ForeignKey('oro_scope.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_cms_txt_cont_variant_scope = Table(
    'oro_cms_txt_cont_variant_scope', metadata,
    Column('variant_id', ForeignKey('oro_cms_text_content_variant.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('scope_id', ForeignKey('oro_scope.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


