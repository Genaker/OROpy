from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWorkflowStep(Base):
    __tablename__ = 'oro_workflow_step'
    __table_args__ = (
        Index('oro_workflow_step_unique_idx', 'workflow_name', 'name', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_workflow_step_id_seq'::regclass)"))
    workflow_name = Column(ForeignKey('oro_workflow_definition.name', ondelete='CASCADE'), index=True, server_default=text("NULL::character varying"))
    name = Column(String(255), nullable=False, index=True)
    label = Column(String(255), nullable=False)
    step_order = Column(Integer, nullable=False)
    is_final = Column(Boolean, nullable=False)

    oro_workflow_definition = relationship('OroWorkflowDefinition', primaryjoin='OroWorkflowStep.workflow_name == OroWorkflowDefinition.name')


