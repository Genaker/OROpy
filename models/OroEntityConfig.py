from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEntityConfig(Base):
    __tablename__ = 'oro_entity_config'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_entity_config_id_seq'::regclass)"))
    class_name = Column(String(255), nullable=False, unique=True)
    created = Column(TIMESTAMP(precision=0), nullable=False)
    updated = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    mode = Column(String(8), nullable=False)
    data = Column(Text, comment='(DC2Type:array)(DC2Type:array)')


