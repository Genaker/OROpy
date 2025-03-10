from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroConfig(Base):
    __tablename__ = 'oro_config'
    __table_args__ = (
        Index('config_uq_entity', 'entity', 'record_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_config_id_seq'::regclass)"))
    entity = Column(String(255), server_default=text("NULL::character varying"))
    record_id = Column(Integer)


