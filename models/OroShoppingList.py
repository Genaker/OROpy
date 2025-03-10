from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroShoppingList(Base):
    __tablename__ = 'oro_shopping_list'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_shopping_list_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    customer_id = Column(ForeignKey('oro_customer.id', ondelete='SET NULL'), index=True)
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='CASCADE'), index=True)
    website_id = Column(ForeignKey('oro_website.id', ondelete='SET NULL'), index=True)
    label = Column(String(255), nullable=False)
    notes = Column(Text)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    currency = Column(String(3), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    customer = relationship('OroCustomer')
    customer_user = relationship('OroCustomerUser')
    organization = relationship('OroOrganization')
    user_owner = relationship('OroUser')
    website = relationship('OroWebsite')


t_oro_slug_scope = Table(
    'oro_slug_scope', metadata,
    Column('slug_id', ForeignKey('oro_redirect_slug.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('scope_id', ForeignKey('oro_scope.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_web_catalog_node_scope = Table(
    'oro_web_catalog_node_scope', metadata,
    Column('node_id', ForeignKey('oro_web_catalog_content_node.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('scope_id', ForeignKey('oro_scope.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_web_catalog_variant_scope = Table(
    'oro_web_catalog_variant_scope', metadata,
    Column('variant_id', ForeignKey('oro_web_catalog_variant.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('scope_id', ForeignKey('oro_scope.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


