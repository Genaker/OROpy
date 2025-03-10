from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWebCatalogVariant(Base):
    __tablename__ = 'oro_web_catalog_variant'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_web_catalog_variant_id_seq'::regclass)"))
    node_id = Column(ForeignKey('oro_web_catalog_content_node.id', ondelete='CASCADE'), index=True)
    type = Column(String(255), nullable=False)
    system_page_route = Column(String(255), server_default=text("NULL::character varying"))
    override_variant_configuration = Column(Boolean, nullable=False, server_default=text("false"))
    do_not_render_title = Column(Boolean, nullable=False, server_default=text("false"))
    is_default = Column(Boolean, nullable=False, server_default=text("false"))
    product_page_product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), index=True)
    product_collection_segment_id = Column(ForeignKey('oro_segment.id', ondelete='CASCADE'), index=True)
    category_page_category_id = Column(ForeignKey('oro_catalog_category.id', ondelete='CASCADE'), index=True)
    exclude_subcategories = Column(Boolean)
    cms_page_id = Column(ForeignKey('oro_cms_page.id', ondelete='CASCADE'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    category_page_category = relationship('OroCatalogCategory')
    cms_page = relationship('OroCmsPage')
    node = relationship('OroWebCatalogContentNode')
    product_collection_segment = relationship('OroSegment')
    product_page_product = relationship('OroProduct')
    slugs = relationship('OroRedirectSlug', secondary='oro_web_catalog_variant_slug')


