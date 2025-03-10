from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCatalogCategory(Base):
    __tablename__ = 'oro_catalog_category'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_catalog_category_id_seq'::regclass)"))
    parent_id = Column(ForeignKey('oro_catalog_category.id', ondelete='CASCADE'), index=True)
    default_product_options_id = Column(ForeignKey('oro_category_def_prod_opts.id', ondelete='SET NULL'), unique=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    tree_left = Column(Integer, nullable=False)
    tree_level = Column(Integer, nullable=False)
    tree_right = Column(Integer, nullable=False)
    tree_root = Column(Integer)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    materialized_path = Column(String(255), server_default=text("NULL::character varying"))
    title = Column(String(255), nullable=False, index=True)
    largeimage_id = Column(ForeignKey('oro_attachment_file.id', ondelete='SET NULL'), index=True)
    smallimage_id = Column(ForeignKey('oro_attachment_file.id', ondelete='SET NULL'), index=True)
    manageinventory_id = Column(ForeignKey('oro_entity_fallback_value.id', ondelete='SET NULL'), index=True)
    highlightlowinventory_id = Column(ForeignKey('oro_entity_fallback_value.id', ondelete='SET NULL'), index=True)
    inventorythreshold_id = Column(ForeignKey('oro_entity_fallback_value.id', ondelete='SET NULL'), index=True)
    lowinventorythreshold_id = Column(ForeignKey('oro_entity_fallback_value.id', ondelete='SET NULL'), index=True)
    minimumquantitytoorder_id = Column(ForeignKey('oro_entity_fallback_value.id', ondelete='SET NULL'), index=True)
    maximumquantitytoorder_id = Column(ForeignKey('oro_entity_fallback_value.id', ondelete='SET NULL'), index=True)
    decrementquantity_id = Column(ForeignKey('oro_entity_fallback_value.id', ondelete='SET NULL'), index=True)
    backorder_id = Column(ForeignKey('oro_entity_fallback_value.id', ondelete='SET NULL'), index=True)
    isupcoming_id = Column(ForeignKey('oro_entity_fallback_value.id', ondelete='SET NULL'), index=True)
    availability_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    serialized_data = Column(JSONB(astext_type=Text()))

    backorder = relationship('OroEntityFallbackValue', primaryjoin='OroCatalogCategory.backorder_id == OroEntityFallbackValue.id')
    decrementquantity = relationship('OroEntityFallbackValue', primaryjoin='OroCatalogCategory.decrementquantity_id == OroEntityFallbackValue.id')
    default_product_options = relationship('OroCategoryDefProdOpt')
    highlightlowinventory = relationship('OroEntityFallbackValue', primaryjoin='OroCatalogCategory.highlightlowinventory_id == OroEntityFallbackValue.id')
    inventorythreshold = relationship('OroEntityFallbackValue', primaryjoin='OroCatalogCategory.inventorythreshold_id == OroEntityFallbackValue.id')
    isupcoming = relationship('OroEntityFallbackValue', primaryjoin='OroCatalogCategory.isupcoming_id == OroEntityFallbackValue.id')
    largeimage = relationship('OroAttachmentFile', primaryjoin='OroCatalogCategory.largeimage_id == OroAttachmentFile.id')
    lowinventorythreshold = relationship('OroEntityFallbackValue', primaryjoin='OroCatalogCategory.lowinventorythreshold_id == OroEntityFallbackValue.id')
    manageinventory = relationship('OroEntityFallbackValue', primaryjoin='OroCatalogCategory.manageinventory_id == OroEntityFallbackValue.id')
    maximumquantitytoorder = relationship('OroEntityFallbackValue', primaryjoin='OroCatalogCategory.maximumquantitytoorder_id == OroEntityFallbackValue.id')
    minimumquantitytoorder = relationship('OroEntityFallbackValue', primaryjoin='OroCatalogCategory.minimumquantitytoorder_id == OroEntityFallbackValue.id')
    organization = relationship('OroOrganization')
    parent = relationship('OroCatalogCategory', remote_side=[id])
    smallimage = relationship('OroAttachmentFile', primaryjoin='OroCatalogCategory.smallimage_id == OroAttachmentFile.id')
    notes = relationship('OroNote', secondary='oro_rel_6f8f552aff3a7b97ec3308')
    slugs = relationship('OroRedirectSlug', secondary='oro_catalog_cat_slug')
    localized_values = relationship('OroFallbackLocalizationVal', secondary='oro_catalog_cat_slug_prototype')
    localizedfallbackvalues = relationship('OroFallbackLocalizationVal', secondary='oro_rel_ff3a7b9721a159aea3971e')
    localizedfallbackvalues1 = relationship('OroFallbackLocalizationVal', secondary='oro_rel_ff3a7b9721a159ae2725f3')
    localizedfallbackvalues2 = relationship('OroFallbackLocalizationVal', secondary='oro_rel_ff3a7b9721a159ae6e1a29')


