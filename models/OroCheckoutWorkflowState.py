from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCheckoutWorkflowState(Base):
    __tablename__ = 'oro_checkout_workflow_state'
    __table_args__ = (
        Index('oro_checkout_wf_state_uidx', 'entity_id', 'entity_class', 'token', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_checkout_workflow_state_id_seq'::regclass)"))
    token = Column(String(255), nullable=False)
    entity_id = Column(Integer, nullable=False)
    entity_class = Column(String(255), nullable=False)
    state_data = Column(Text, nullable=False, comment='(DC2Type:array)(DC2Type:array)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')


