from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroMigration(Base):
    __tablename__ = 'oro_migrations'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_migrations_id_seq'::regclass)"))
    bundle = Column(String(250), nullable=False, index=True)
    version = Column(String(250), nullable=False)
    loaded_at = Column(TIMESTAMP(precision=0), nullable=False)


