from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWorkflowRestriction(Base):
    __tablename__ = 'oro_workflow_restriction'
    __table_args__ = (
        Index('oro_workflow_restriction_idx', 'workflow_name', 'workflow_step_id', 'field', 'entity_class', 'mode', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_workflow_restriction_id_seq'::regclass)"))
    workflow_name = Column(ForeignKey('oro_workflow_definition.name', ondelete='CASCADE'), nullable=False, index=True)
    workflow_step_id = Column(ForeignKey('oro_workflow_step.id', ondelete='CASCADE'), index=True)
    attribute = Column(String(255), nullable=False)
    field = Column(String(150), nullable=False)
    entity_class = Column(String(255), nullable=False)
    mode = Column(String(8), nullable=False)
    mode_values = Column(JSON, comment='(DC2Type:json_array)(DC2Type:json_array)')

    oro_workflow_definition = relationship('OroWorkflowDefinition')
    workflow_step = relationship('OroWorkflowStep')


