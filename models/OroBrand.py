from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroBrand(Base):
    __tablename__ = 'oro_brand'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_brand_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    business_unit_owner_id = Column(ForeignKey('oro_business_unit.id', ondelete='SET NULL'), index=True)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    status = Column(String(16), nullable=False)
    default_title = Column(String(255), nullable=False, index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    business_unit_owner = relationship('OroBusinessUnit')
    organization = relationship('OroOrganization')
    localized_values = relationship('OroFallbackLocalizationVal', secondary='oro_brand_description')
    localized_values1 = relationship('OroFallbackLocalizationVal', secondary='oro_brand_name')
    localized_values2 = relationship('OroFallbackLocalizationVal', secondary='oro_brand_short_desc')
    slugs = relationship('OroRedirectSlug', secondary='oro_brand_slug')
    localized_values3 = relationship('OroFallbackLocalizationVal', secondary='oro_brand_slug_prototype')
    localizedfallbackvalues = relationship('OroFallbackLocalizationVal', secondary='oro_rel_dd93d65c21a159aea3971e')
    localizedfallbackvalues1 = relationship('OroFallbackLocalizationVal', secondary='oro_rel_dd93d65c21a159ae2725f3')
    localizedfallbackvalues2 = relationship('OroFallbackLocalizationVal', secondary='oro_rel_dd93d65c21a159ae6e1a29')


