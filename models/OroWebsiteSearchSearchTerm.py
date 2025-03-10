from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWebsiteSearchSearchTerm(Base):
    __tablename__ = 'oro_website_search_search_term'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_website_search_search_term_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    business_unit_owner_id = Column(ForeignKey('oro_business_unit.id', ondelete='SET NULL'), index=True)
    phrases = Column(Text, nullable=False)
    action_type = Column(String(128), nullable=False)
    modify_action_type = Column(String(128), server_default=text("NULL::character varying"))
    redirect_action_type = Column(String(128), server_default=text("NULL::character varying"))
    redirect_uri = Column(Text)
    redirect_system_page = Column(Text)
    redirect_301 = Column(Boolean, nullable=False, server_default=text("false"))
    partial_match = Column(Boolean, nullable=False, server_default=text("false"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    redirectcontentnode_id = Column(ForeignKey('oro_web_catalog_content_node.id', ondelete='SET NULL'), index=True)
    redirectproduct_id = Column(ForeignKey('oro_product.id', ondelete='SET NULL'), index=True)
    productcollectionsegment_id = Column(ForeignKey('oro_segment.id', ondelete='SET NULL'), index=True)
    redirectcategory_id = Column(ForeignKey('oro_catalog_category.id', ondelete='SET NULL'), index=True)
    contentblock_id = Column(ForeignKey('oro_cms_content_block.id', ondelete='SET NULL'), index=True)
    redirectcmspage_id = Column(ForeignKey('oro_cms_page.id', ondelete='SET NULL'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    business_unit_owner = relationship('OroBusinessUnit')
    contentblock = relationship('OroCmsContentBlock')
    organization = relationship('OroOrganization')
    productcollectionsegment = relationship('OroSegment')
    redirectcategory = relationship('OroCatalogCategory')
    redirectcmspage = relationship('OroCmsPage')
    redirectcontentnode = relationship('OroWebCatalogContentNode')
    redirectproduct = relationship('OroProduct')


