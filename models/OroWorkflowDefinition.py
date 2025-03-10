from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWorkflowDefinition(Base):
    __tablename__ = 'oro_workflow_definition'

    name = Column(String(255), primary_key=True)
    start_step_id = Column(ForeignKey('oro_workflow_step.id', ondelete='SET NULL'), index=True)
    label = Column(String(255), nullable=False)
    related_entity = Column(String(255), nullable=False)
    entity_attribute_name = Column(String(255), nullable=False)
    steps_display_ordered = Column(Boolean, nullable=False)
    system = Column(Boolean, nullable=False)
    active = Column(Boolean, nullable=False, server_default=text("false"))
    priority = Column(Integer, nullable=False, server_default=text("0"))
    configuration = Column(Text, nullable=False, comment='(DC2Type:array)(DC2Type:array)')
    exclusive_active_groups = Column(Text, comment='(DC2Type:simple_array)(DC2Type:simple_array)')
    exclusive_record_groups = Column(Text, comment='(DC2Type:simple_array)(DC2Type:simple_array)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    applications = Column(Text, nullable=False, comment='(DC2Type:simple_array)(DC2Type:simple_array)')

    start_step = relationship('OroWorkflowStep', primaryjoin='OroWorkflowDefinition.start_step_id == OroWorkflowStep.id')


