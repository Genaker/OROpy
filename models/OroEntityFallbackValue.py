from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEntityFallbackValue(Base):
    __tablename__ = 'oro_entity_fallback_value'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_entity_fallback_value_id_seq'::regclass)"))
    fallback = Column(String(64), server_default=text("NULL::character varying"))
    scalar_value = Column(String(255), server_default=text("NULL::character varying"))
    array_value = Column(Text, comment='(DC2Type:array)(DC2Type:array)')


