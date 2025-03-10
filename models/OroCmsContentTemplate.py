from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCmsContentTemplate(Base):
    __tablename__ = 'oro_cms_content_template'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cms_content_template_id_seq'::regclass)"))
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False)
    enabled = Column(Boolean, nullable=False, server_default=text("true"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    previewimage_id = Column(ForeignKey('oro_attachment_file.id', ondelete='SET NULL'), index=True)
    content = Column(Text, comment='(DC2Type:wysiwyg)(DC2Type:wysiwyg)')
    content_style = Column(Text, comment='(DC2Type:wysiwyg_style)')
    content_properties = Column(JSON, comment='(DC2Type:wysiwyg_properties)')
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    previewimage = relationship('OroAttachmentFile')
    user_owner = relationship('OroUser')


