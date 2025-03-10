from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroProcessTrigger(Base):
    __tablename__ = 'oro_process_trigger'
    __table_args__ = (
        Index('process_trigger_unique_idx', 'event', 'field', 'definition_name', 'cron', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_process_trigger_id_seq'::regclass)"))
    definition_name = Column(ForeignKey('oro_process_definition.name', ondelete='CASCADE'), index=True, server_default=text("NULL::character varying"))
    event = Column(String(255), server_default=text("NULL::character varying"))
    field = Column(String(150), server_default=text("NULL::character varying"))
    queued = Column(Boolean, nullable=False)
    time_shift = Column(Integer)
    cron = Column(String(100), server_default=text("NULL::character varying"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    priority = Column(SmallInteger, nullable=False)

    oro_process_definition = relationship('OroProcessDefinition')


