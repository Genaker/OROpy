from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroConfigValue(Base):
    __tablename__ = 'oro_config_value'
    __table_args__ = (
        Index('config_value_uq_entity', 'name', 'section', 'config_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_config_value_id_seq'::regclass)"))
    config_id = Column(ForeignKey('oro_config.id', ondelete='CASCADE'), index=True)
    name = Column(String(255), nullable=False)
    section = Column(String(50), server_default=text("NULL::character varying"))
    text_value = Column(Text)
    object_value = Column(Text, comment='(DC2Type:object)(DC2Type:object)')
    array_value = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    type = Column(String(20), nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)

    config = relationship('OroConfig')


