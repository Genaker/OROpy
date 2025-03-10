from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWebsiteSearchResultHistory(Base):
    __tablename__ = 'oro_website_search_result_history'

    id = Column(UUID, primary_key=True)
    website_id = Column(ForeignKey('oro_website.id', ondelete='CASCADE'), nullable=False, index=True)
    localization_id = Column(ForeignKey('oro_localization.id', ondelete='SET NULL'), index=True)
    customer_id = Column(ForeignKey('oro_customer.id', ondelete='SET NULL'), index=True)
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='SET NULL'), index=True)
    business_unit_owner_id = Column(ForeignKey('oro_business_unit.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    normalized_search_term_hash = Column(String(32), nullable=False, index=True)
    result_type = Column(String(32), nullable=False)
    results_count = Column(Integer, nullable=False)
    search_session = Column(String(36), unique=True, server_default=text("NULL::character varying"))
    search_term = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    customer_visitor_id = Column(Integer)
    serialized_data = Column(JSONB(astext_type=Text()))

    business_unit_owner = relationship('OroBusinessUnit')
    customer = relationship('OroCustomer')
    customer_user = relationship('OroCustomerUser')
    localization = relationship('OroLocalization')
    organization = relationship('OroOrganization')
    website = relationship('OroWebsite')


t_oro_website_search_search_term_scopes = Table(
    'oro_website_search_search_term_scopes', metadata,
    Column('search_term_id', ForeignKey('oro_website_search_search_term.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('scope_id', ForeignKey('oro_scope.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_workflow_scopes = Table(
    'oro_workflow_scopes', metadata,
    Column('workflow_name', ForeignKey('oro_workflow_definition.name', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('scope_id', ForeignKey('oro_scope.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


