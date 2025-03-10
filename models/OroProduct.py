from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroProduct(Base):
    __tablename__ = 'oro_product'
    __table_args__ = (
        Index('idx_oro_product_sku_id_organization', 'sku', 'id', 'organization_id'),
        Index('idx_oro_product_created_at_id_organization', 'created_at', 'id', 'organization_id'),
        Index('idx_oro_product_status_id_organization', 'status', 'id', 'organization_id'),
        Index('idx_oro_product_id_updated_at', 'id', 'updated_at'),
        Index('idx_oro_product_updated_at_id_organization', 'updated_at', 'id', 'organization_id'),
        Index('uidx_oro_product_sku_organization', 'sku', 'organization_id', unique=True)
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_product_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    business_unit_owner_id = Column(ForeignKey('oro_business_unit.id', ondelete='SET NULL'), index=True)
    primary_unit_precision_id = Column(ForeignKey('oro_product_unit_precision.id', ondelete='SET NULL'), unique=True)
    brand_id = Column(ForeignKey('oro_brand.id', ondelete='SET NULL'), index=True)
    inventory_status_id = Column(ForeignKey('oro_enum_prod_inventory_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    attribute_family_id = Column(ForeignKey('oro_attribute_family.id', ondelete='RESTRICT'), index=True)
    sku = Column(String(255), nullable=False, index=True)
    sku_uppercase = Column(String(255), index=True, server_default=text("NULL::character varying"))
    name = Column(String(255), nullable=False, index=True)
    name_uppercase = Column(String(255), nullable=False, index=True)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    variant_fields = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    status = Column(String(16), nullable=False, index=True)
    type = Column(String(32), nullable=False)
    is_featured = Column(Boolean, nullable=False, index=True, server_default=text("false"))
    is_new_arrival = Column(Boolean, nullable=False, index=True, server_default=text("false"))
    pagetemplate_id = Column(ForeignKey('oro_entity_fallback_value.id', ondelete='SET NULL'), index=True)
    category_id = Column(ForeignKey('oro_catalog_category.id', ondelete='SET NULL'), index=True)
    category_sort_order = Column(Float(53))
    taxcode_id = Column(ForeignKey('oro_tax_product_tax_code.id', ondelete='SET NULL'), index=True)
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

    attribute_family = relationship('OroAttributeFamily')
    backorder = relationship('OroEntityFallbackValue', primaryjoin='OroProduct.backorder_id == OroEntityFallbackValue.id')
    brand = relationship('OroBrand')
    business_unit_owner = relationship('OroBusinessUnit')
    category = relationship('OroCatalogCategory')
    decrementquantity = relationship('OroEntityFallbackValue', primaryjoin='OroProduct.decrementquantity_id == OroEntityFallbackValue.id')
    highlightlowinventory = relationship('OroEntityFallbackValue', primaryjoin='OroProduct.highlightlowinventory_id == OroEntityFallbackValue.id')
    inventory_status = relationship('OroEnumProdInventoryStatu')
    inventorythreshold = relationship('OroEntityFallbackValue', primaryjoin='OroProduct.inventorythreshold_id == OroEntityFallbackValue.id')
    isupcoming = relationship('OroEntityFallbackValue', primaryjoin='OroProduct.isupcoming_id == OroEntityFallbackValue.id')
    lowinventorythreshold = relationship('OroEntityFallbackValue', primaryjoin='OroProduct.lowinventorythreshold_id == OroEntityFallbackValue.id')
    manageinventory = relationship('OroEntityFallbackValue', primaryjoin='OroProduct.manageinventory_id == OroEntityFallbackValue.id')
    maximumquantitytoorder = relationship('OroEntityFallbackValue', primaryjoin='OroProduct.maximumquantitytoorder_id == OroEntityFallbackValue.id')
    minimumquantitytoorder = relationship('OroEntityFallbackValue', primaryjoin='OroProduct.minimumquantitytoorder_id == OroEntityFallbackValue.id')
    organization = relationship('OroOrganization')
    pagetemplate = relationship('OroEntityFallbackValue', primaryjoin='OroProduct.pagetemplate_id == OroEntityFallbackValue.id')
    primary_unit_precision = relationship('OroProductUnitPrecision', primaryjoin='OroProduct.primary_unit_precision_id == OroProductUnitPrecision.id')
    taxcode = relationship('OroTaxProductTaxCode')
    slugs = relationship('OroRedirectSlug', secondary='oro_product_slug')
    product_tax_codes = relationship('OroTaxProductTaxCode', secondary='oro_tax_prod_tax_code_prod')


