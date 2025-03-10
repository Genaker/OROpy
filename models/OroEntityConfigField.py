from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEntityConfigField(Base):
    __tablename__ = 'oro_entity_config_field'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_entity_config_field_id_seq'::regclass)"))
    entity_id = Column(ForeignKey('oro_entity_config.id', ondelete='CASCADE'), index=True)
    field_name = Column(String(255), nullable=False)
    type = Column(String(60), nullable=False)
    created = Column(TIMESTAMP(precision=0), nullable=False)
    updated = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    mode = Column(String(8), nullable=False)
    data = Column(Text, comment='(DC2Type:array)(DC2Type:array)')

    entity = relationship('OroEntityConfig')


