from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroSearchIndexText(Base):
    __tablename__ = 'oro_search_index_text'
    __table_args__ = (
        Index('oro_search_index_text_item_field_idx', 'item_id', 'field'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_search_index_text_id_seq'::regclass)"))
    item_id = Column(ForeignKey('oro_search_item.id'), nullable=False, index=True)
    field = Column(String(250), nullable=False, index=True)
    value = Column(Text, nullable=False)

    item = relationship('OroSearchItem')


t_oro_security_perm_apply_entity = Table(
    'oro_security_perm_apply_entity', metadata,
    Column('permission_id', ForeignKey('oro_security_permission.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('permission_entity_id', ForeignKey('oro_security_permission_entity.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_security_perm_excl_entity = Table(
    'oro_security_perm_excl_entity', metadata,
    Column('permission_id', ForeignKey('oro_security_permission.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('permission_entity_id', ForeignKey('oro_security_permission_entity.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


