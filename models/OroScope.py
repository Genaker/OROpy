from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroScope(Base):
    __tablename__ = 'oro_scope'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_scope_id_seq'::regclass)"))
    row_hash = Column(String(32), unique=True, server_default=text("NULL::character varying"), comment='customer_id,customergroup_id,localization_id,organization_id,user_id,webcatalog_id,website_id')
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='CASCADE'), index=True)
    user_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), index=True)
    localization_id = Column(ForeignKey('oro_localization.id', ondelete='CASCADE'), index=True)
    website_id = Column(ForeignKey('oro_website.id', ondelete='CASCADE'), index=True)
    webcatalog_id = Column(ForeignKey('oro_web_catalog.id', ondelete='CASCADE'), index=True)
    customer_id = Column(ForeignKey('oro_customer.id', ondelete='CASCADE'), index=True)
    customergroup_id = Column(ForeignKey('oro_customer_group.id', ondelete='CASCADE'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    customer = relationship('OroCustomer')
    customergroup = relationship('OroCustomerGroup')
    localization = relationship('OroLocalization')
    organization = relationship('OroOrganization')
    user = relationship('OroUser')
    webcatalog = relationship('OroWebCatalog')
    website = relationship('OroWebsite')
    oro_workflow_definition = relationship('OroWorkflowDefinition', secondary='oro_workflow_scopes')
    search_terms = relationship('OroWebsiteSearchSearchTerm', secondary='oro_website_search_search_term_scopes')
    slugs = relationship('OroRedirectSlug', secondary='oro_slug_scope')
    variants = relationship('OroWebCatalogVariant', secondary='oro_web_catalog_variant_scope')
    variants1 = relationship('OroCmsTextContentVariant', secondary='oro_cms_txt_cont_variant_scope')


t_oro_ship_mtds_rule_website = Table(
    'oro_ship_mtds_rule_website', metadata,
    Column('oro_ship_mtds_cfgs_rl_id', ForeignKey('oro_ship_method_configs_rule.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('website_id', ForeignKey('oro_website.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


