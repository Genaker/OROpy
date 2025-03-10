from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroDigitalAsset(Base):
    __tablename__ = 'oro_digital_asset'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_digital_asset_id_seq'::regclass)"))
    source_file_id = Column(ForeignKey('oro_attachment_file.id', ondelete='CASCADE'), nullable=False, unique=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, index=True, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    source_file = relationship('OroAttachmentFile', primaryjoin='OroDigitalAsset.source_file_id == OroAttachmentFile.id')
    user_owner = relationship('OroUser')
    localized_values = relationship('OroFallbackLocalizationVal', secondary='oro_digital_asset_title')


