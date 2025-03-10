from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroConsent(Base):
    __tablename__ = 'oro_consent'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_consent_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    content_node_id = Column(ForeignKey('oro_web_catalog_content_node.id', ondelete='SET NULL'), index=True)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    mandatory = Column(Boolean, nullable=False, server_default=text("true"))
    declined_notification = Column(Boolean, nullable=False, server_default=text("true"))
    serialized_data = Column(JSONB(astext_type=Text()))

    content_node = relationship('OroWebCatalogContentNode')
    organization = relationship('OroOrganization')
    user_owner = relationship('OroUser')
    localized_values = relationship('OroFallbackLocalizationVal', secondary='oro_consent_name')


