from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEntityConfigIndexValue(Base):
    __tablename__ = 'oro_entity_config_index_value'
    __table_args__ = (
        Index('idx_entity_config_index_entity', 'scope', 'code', 'value', 'entity_id'),
        Index('idx_entity_config_index_field', 'scope', 'code', 'value', 'field_id')
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_entity_config_index_value_id_seq'::regclass)"))
    field_id = Column(ForeignKey('oro_entity_config_field.id', ondelete='CASCADE'), index=True)
    entity_id = Column(ForeignKey('oro_entity_config.id', ondelete='CASCADE'), index=True)
    code = Column(String(255), nullable=False)
    scope = Column(String(255), nullable=False)
    value = Column(String(255), server_default=text("NULL::character varying"))

    entity = relationship('OroEntityConfig')
    field = relationship('OroEntityConfigField')


