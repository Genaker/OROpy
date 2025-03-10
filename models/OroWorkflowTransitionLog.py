from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWorkflowTransitionLog(Base):
    __tablename__ = 'oro_workflow_transition_log'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_workflow_transition_log_id_seq'::regclass)"))
    step_from_id = Column(ForeignKey('oro_workflow_step.id', ondelete='SET NULL'), index=True)
    step_to_id = Column(ForeignKey('oro_workflow_step.id', ondelete='SET NULL'), index=True)
    workflow_item_id = Column(ForeignKey('oro_workflow_item.id', ondelete='CASCADE'), index=True)
    transition = Column(String(255), server_default=text("NULL::character varying"))
    transition_date = Column(TIMESTAMP(precision=0), nullable=False)

    step_from = relationship('OroWorkflowStep', primaryjoin='OroWorkflowTransitionLog.step_from_id == OroWorkflowStep.id')
    step_to = relationship('OroWorkflowStep', primaryjoin='OroWorkflowTransitionLog.step_to_id == OroWorkflowStep.id')
    workflow_item = relationship('OroWorkflowItem')


