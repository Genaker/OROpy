from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroMigrationsDatum(Base):
    __tablename__ = 'oro_migrations_data'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_migrations_data_id_seq'::regclass)"))
    class_name = Column(String(255), nullable=False)
    loaded_at = Column(TIMESTAMP(precision=0), nullable=False)
    version = Column(String(255), server_default=text("NULL::character varying"))


