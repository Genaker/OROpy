from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWorkflowEntityAcl(Base):
    __tablename__ = 'oro_workflow_entity_acl'
    __table_args__ = (
        Index('oro_workflow_acl_unique_idx', 'workflow_name', 'attribute', 'workflow_step_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_workflow_entity_acl_id_seq'::regclass)"))
    workflow_name = Column(ForeignKey('oro_workflow_definition.name', ondelete='CASCADE'), index=True, server_default=text("NULL::character varying"))
    workflow_step_id = Column(ForeignKey('oro_workflow_step.id', ondelete='CASCADE'), index=True)
    attribute = Column(String(255), nullable=False)
    entity_class = Column(String(255), nullable=False)
    updatable = Column(Boolean, nullable=False)
    deletable = Column(Boolean, nullable=False)

    oro_workflow_definition = relationship('OroWorkflowDefinition')
    workflow_step = relationship('OroWorkflowStep')


