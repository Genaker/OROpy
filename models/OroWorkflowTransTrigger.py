from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWorkflowTransTrigger(Base):
    __tablename__ = 'oro_workflow_trans_trigger'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_workflow_trans_trigger_id_seq'::regclass)"))
    workflow_name = Column(ForeignKey('oro_workflow_definition.name', ondelete='CASCADE'), nullable=False, index=True)
    entity_class = Column(String(255), server_default=text("NULL::character varying"))
    queued = Column(Boolean, nullable=False)
    transition_name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    type = Column(String(255), nullable=False)
    cron = Column(String(100), server_default=text("NULL::character varying"))
    filter = Column(Text)
    event = Column(String(255), server_default=text("NULL::character varying"))
    field = Column(String(150), server_default=text("NULL::character varying"))
    require = Column(Text)
    relation = Column(Text)

    oro_workflow_definition = relationship('OroWorkflowDefinition')


