from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWorkflowItem(Base):
    __tablename__ = 'oro_workflow_item'
    __table_args__ = (
        Index('oro_workflow_item_entity_definition_unq', 'entity_id', 'workflow_name', unique=True),
        Index('oro_workflow_item_entity_idx', 'entity_class', 'entity_id')
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_workflow_item_id_seq'::regclass)"))
    current_step_id = Column(ForeignKey('oro_workflow_step.id', ondelete='SET NULL'), index=True)
    workflow_name = Column(ForeignKey('oro_workflow_definition.name', ondelete='CASCADE'), nullable=False, index=True)
    entity_id = Column(String(255), server_default=text("NULL::character varying"))
    entity_class = Column(String(255), server_default=text("NULL::character varying"))
    created = Column(TIMESTAMP(precision=0), nullable=False)
    updated = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    data = Column(Text)
    serialized_data = Column(JSONB(astext_type=Text()))

    current_step = relationship('OroWorkflowStep')
    oro_workflow_definition = relationship('OroWorkflowDefinition')


