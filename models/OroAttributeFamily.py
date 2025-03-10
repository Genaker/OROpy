from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroAttributeFamily(Base):
    __tablename__ = 'oro_attribute_family'
    __table_args__ = (
        Index('oro_attribute_family_code_org_uidx', 'code', 'organization_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_attribute_family_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    image_id = Column(ForeignKey('oro_attachment_file.id', ondelete='SET NULL'), index=True)
    code = Column(String(255), nullable=False)
    entity_class = Column(String(255), nullable=False)
    is_enabled = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    image = relationship('OroAttachmentFile')
    organization = relationship('OroOrganization')
    localized_values = relationship('OroFallbackLocalizationVal', secondary='oro_attribute_family_label')


