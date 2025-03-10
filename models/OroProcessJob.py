from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroProcessJob(Base):
    __tablename__ = 'oro_process_job'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_process_job_id_seq'::regclass)"))
    process_trigger_id = Column(ForeignKey('oro_process_trigger.id', ondelete='CASCADE'), index=True)
    entity_id = Column(Integer)
    entity_hash = Column(String(255), index=True, server_default=text("NULL::character varying"))
    serialized_data = Column(Text)

    process_trigger = relationship('OroProcessTrigger')


