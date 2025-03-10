from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class AkeneoBatchStepExecution(Base):
    __tablename__ = 'akeneo_batch_step_execution'

    id = Column(Integer, primary_key=True, server_default=text("nextval('akeneo_batch_step_execution_id_seq'::regclass)"))
    job_execution_id = Column(ForeignKey('akeneo_batch_job_execution.id', ondelete='CASCADE'), index=True)
    step_name = Column(String(100), server_default=text("NULL::character varying"))
    status = Column(Integer, nullable=False)
    read_count = Column(Integer, nullable=False)
    write_count = Column(Integer, nullable=False)
    start_time = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    end_time = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    exit_code = Column(String(255), server_default=text("NULL::character varying"))
    exit_description = Column(Text)
    terminate_only = Column(Boolean)
    failure_exceptions = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    errors = Column(Text, nullable=False, comment='(DC2Type:array)(DC2Type:array)')
    summary = Column(Text, nullable=False, comment='(DC2Type:array)(DC2Type:array)')

    job_execution = relationship('AkeneoBatchJobExecution')


