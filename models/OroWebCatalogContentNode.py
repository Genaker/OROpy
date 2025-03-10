from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWebCatalogContentNode(Base):
    __tablename__ = 'oro_web_catalog_content_node'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_web_catalog_content_node_id_seq'::regclass)"))
    parent_id = Column(ForeignKey('oro_web_catalog_content_node.id', ondelete='CASCADE'), index=True)
    web_catalog_id = Column(ForeignKey('oro_web_catalog.id', ondelete='CASCADE'), nullable=False, index=True)
    parent_scope_used = Column(Boolean, nullable=False, server_default=text("true"))
    rewrite_variant_title = Column(Boolean, nullable=False, server_default=text("true"))
    materialized_path = Column(String(1024), server_default=text("NULL::character varying"))
    tree_left = Column(Integer, nullable=False)
    tree_level = Column(Integer, nullable=False)
    tree_right = Column(Integer, nullable=False)
    tree_root = Column(Integer)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    parent = relationship('OroWebCatalogContentNode', remote_side=[id])
    web_catalog = relationship('OroWebCatalog')
    notes = relationship('OroNote', secondary='oro_rel_6f8f552a5b5187a347fdf8')
    scopes = relationship('OroScope', secondary='oro_web_catalog_node_scope')
    localizedfallbackvalues = relationship('OroFallbackLocalizationVal', secondary='oro_rel_5b5187a321a159aea3971e')
    localizedfallbackvalues1 = relationship('OroFallbackLocalizationVal', secondary='oro_rel_5b5187a321a159ae2725f3')
    localizedfallbackvalues2 = relationship('OroFallbackLocalizationVal', secondary='oro_rel_5b5187a321a159ae6e1a29')


