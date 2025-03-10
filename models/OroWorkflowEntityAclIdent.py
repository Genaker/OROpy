from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWorkflowEntityAclIdent(Base):
    __tablename__ = 'oro_workflow_entity_acl_ident'
    __table_args__ = (
        Index('oro_workflow_entity_acl_identity_idx', 'entity_id', 'entity_class'),
        Index('oro_workflow_entity_acl_identity_unique_idx', 'workflow_entity_acl_id', 'entity_id', 'workflow_item_id', unique=True)
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_workflow_entity_acl_ident_id_seq'::regclass)"))
    workflow_entity_acl_id = Column(ForeignKey('oro_workflow_entity_acl.id', ondelete='CASCADE'), index=True)
    workflow_item_id = Column(ForeignKey('oro_workflow_item.id', ondelete='CASCADE'), index=True)
    entity_class = Column(String(255), nullable=False)
    entity_id = Column(Integer, nullable=False)

    workflow_entity_acl = relationship('OroWorkflowEntityAcl')
    workflow_item = relationship('OroWorkflowItem')


