from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCommerceMenuUpd(Base):
    __tablename__ = 'oro_commerce_menu_upd'
    __table_args__ = (
        Index('oro_commerce_menu_upd_uidx', 'key', 'scope_id', 'menu', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_commerce_menu_upd_id_seq'::regclass)"))
    scope_id = Column(ForeignKey('oro_scope.id'), nullable=False, index=True)
    content_node_id = Column(ForeignKey('oro_web_catalog_content_node.id', ondelete='CASCADE'), index=True)
    image_id = Column(ForeignKey('oro_attachment_file.id', ondelete='SET NULL'), index=True)
    key = Column(String(100), nullable=False)
    parent_key = Column(String(100), server_default=text("NULL::character varying"))
    uri = Column(String(8190), server_default=text("NULL::character varying"))
    menu = Column(String(100), nullable=False)
    icon = Column(String(150), server_default=text("NULL::character varying"))
    is_active = Column(Boolean, nullable=False)
    is_divider = Column(Boolean, nullable=False)
    is_custom = Column(Boolean, nullable=False)
    is_synthetic = Column(Boolean, nullable=False, server_default=text("false"))
    priority = Column(Integer)
    condition = Column(String(512), server_default=text("NULL::character varying"))
    screens = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    system_page_route = Column(String(255), server_default=text("NULL::character varying"))
    link_target = Column(SmallInteger, nullable=False, server_default=text("1"))
    menu_template = Column(String(255), server_default=text("NULL::character varying"))
    max_traverse_level = Column(SmallInteger)
    category_id = Column(ForeignKey('oro_catalog_category.id', ondelete='CASCADE'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    category = relationship('OroCatalogCategory')
    content_node = relationship('OroWebCatalogContentNode')
    image = relationship('OroAttachmentFile')
    scope = relationship('OroScope')


