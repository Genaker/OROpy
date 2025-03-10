from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCmsTextContentVariant(Base):
    __tablename__ = 'oro_cms_text_content_variant'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cms_text_content_variant_id_seq'::regclass)"))
    content_block_id = Column(ForeignKey('oro_cms_content_block.id', ondelete='CASCADE'), index=True)
    content = Column(Text, comment='(DC2Type:wysiwyg)(DC2Type:wysiwyg)')
    content_style = Column(Text, comment='(DC2Type:wysiwyg_style)')
    content_properties = Column(JSON, comment='(DC2Type:wysiwyg_properties)')
    is_default = Column(Boolean, nullable=False, server_default=text("false"))

    content_block = relationship('OroCmsContentBlock')


