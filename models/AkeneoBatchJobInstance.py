from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class AkeneoBatchJobInstance(Base):
    __tablename__ = 'akeneo_batch_job_instance'

    id = Column(Integer, primary_key=True, server_default=text("nextval('akeneo_batch_job_instance_id_seq'::regclass)"))
    code = Column(String(100), nullable=False, unique=True)
    label = Column(String(255), server_default=text("NULL::character varying"))
    alias = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)
    connector = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    rawconfiguration = Column(Text, nullable=False, comment='(DC2Type:array)(DC2Type:array)')


