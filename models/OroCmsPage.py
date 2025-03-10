from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCmsPage(Base):
    __tablename__ = 'oro_cms_page'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cms_page_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    draft_project_id = Column(ForeignKey('oro_draft_project.id', ondelete='CASCADE'), index=True)
    draft_source_id = Column(ForeignKey('oro_cms_page.id', ondelete='CASCADE'), index=True)
    draft_owner_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), index=True)
    content = Column(Text, comment='(DC2Type:wysiwyg)(DC2Type:wysiwyg)')
    content_style = Column(Text, comment='(DC2Type:wysiwyg_style)')
    content_properties = Column(JSON, comment='(DC2Type:wysiwyg_properties)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    draft_uuid = Column(UUID)
    do_not_render_title = Column(Boolean, nullable=False, server_default=text("false"))
    serialized_data = Column(JSONB(astext_type=Text()))

    draft_owner = relationship('OroUser')
    draft_project = relationship('OroDraftProject')
    draft_source = relationship('OroCmsPage', remote_side=[id])
    organization = relationship('OroOrganization')
    slugs = relationship('OroRedirectSlug', secondary='oro_cms_page_to_slug')


