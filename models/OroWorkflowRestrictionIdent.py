from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWorkflowRestrictionIdent(Base):
    __tablename__ = 'oro_workflow_restriction_ident'
    __table_args__ = (
        Index('oro_workflow_restr_ident_unique_idx', 'workflow_restriction_id', 'entity_id', 'workflow_item_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_workflow_restriction_ident_id_seq'::regclass)"))
    workflow_restriction_id = Column(ForeignKey('oro_workflow_restriction.id', ondelete='CASCADE'), index=True)
    workflow_item_id = Column(ForeignKey('oro_workflow_item.id', ondelete='CASCADE'), nullable=False, index=True)
    entity_id = Column(Integer, nullable=False, index=True)

    workflow_item = relationship('OroWorkflowItem')
    workflow_restriction = relationship('OroWorkflowRestriction')


