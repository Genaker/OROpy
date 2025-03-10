from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCmsTabbedContentItem(Base):
    __tablename__ = 'oro_cms_tabbed_content_item'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cms_tabbed_content_item_id_seq'::regclass)"))
    content_widget_id = Column(ForeignKey('oro_cms_content_widget.id', ondelete='CASCADE'), nullable=False, index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    title = Column(String(255), nullable=False)
    item_order = Column(Integer, nullable=False, server_default=text("0"))
    content = Column(Text, comment='(DC2Type:wysiwyg)(DC2Type:wysiwyg)')
    content_style = Column(Text, comment='(DC2Type:wysiwyg_style)')
    content_properties = Column(JSON, comment='(DC2Type:wysiwyg_properties)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    content_widget = relationship('OroCmsContentWidget')
    organization = relationship('OroOrganization')


