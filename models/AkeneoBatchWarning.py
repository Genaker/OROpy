from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class AkeneoBatchWarning(Base):
    __tablename__ = 'akeneo_batch_warning'

    id = Column(Integer, primary_key=True, server_default=text("nextval('akeneo_batch_warning_id_seq'::regclass)"))
    step_execution_id = Column(ForeignKey('akeneo_batch_step_execution.id', ondelete='CASCADE'), index=True)
    name = Column(String(100), server_default=text("NULL::character varying"))
    reason = Column(Text)
    reason_parameters = Column(Text, nullable=False, comment='(DC2Type:array)(DC2Type:array)')
    item = Column(Text, nullable=False, comment='(DC2Type:array)(DC2Type:array)')

    step_execution = relationship('AkeneoBatchStepExecution')


