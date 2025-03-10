from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCmsContentBlock(Base):
    __tablename__ = 'oro_cms_content_block'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cms_content_block_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    business_unit_owner_id = Column(ForeignKey('oro_business_unit.id', ondelete='SET NULL'), index=True)
    alias = Column(String(100), nullable=False, unique=True)
    enabled = Column(Boolean, nullable=False, server_default=text("true"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    business_unit_owner = relationship('OroBusinessUnit')
    organization = relationship('OroOrganization')
    localized_values = relationship('OroFallbackLocalizationVal', secondary='oro_cms_content_block_title')
    scopes = relationship('OroScope', secondary='oro_cms_content_block_scope')


