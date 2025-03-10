from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class AkeneoBatchJobExecution(Base):
    __tablename__ = 'akeneo_batch_job_execution'

    id = Column(Integer, primary_key=True, server_default=text("nextval('akeneo_batch_job_execution_id_seq'::regclass)"))
    job_instance_id = Column(ForeignKey('akeneo_batch_job_instance.id', ondelete='CASCADE'), nullable=False, index=True)
    status = Column(Integer, nullable=False)
    start_time = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    end_time = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    create_time = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    updated_time = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    exit_code = Column(String(255), server_default=text("NULL::character varying"))
    exit_description = Column(Text)
    failure_exceptions = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    log_file = Column(String(255), server_default=text("NULL::character varying"))
    pid = Column(Integer)
    user = Column(String(255), server_default=text("NULL::character varying"))

    job_instance = relationship('AkeneoBatchJobInstance')


