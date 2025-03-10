from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroAudit(Base):
    __tablename__ = 'oro_audit'
    __table_args__ = (
        Index('idx_oro_audit_obj_by_type', 'object_id', 'object_class', 'type'),
        Index('idx_oro_audit_version', 'object_id', 'object_class', 'version', 'type', unique=True),
        Index('idx_oro_audit_transaction', 'object_id', 'object_class', 'transaction_id', 'type', unique=True)
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_audit_id_seq'::regclass)"))
    user_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    impersonation_id = Column(ForeignKey('oro_user_impersonation.id', ondelete='SET NULL'), index=True)
    action = Column(String(8), server_default=text("NULL::character varying"))
    logged_at = Column(TIMESTAMP(precision=0), index=True, server_default=text("NULL::timestamp without time zone"))
    object_id = Column(String(255), server_default=text("NULL::character varying"))
    object_class = Column(String(255), nullable=False, index=True)
    object_name = Column(String(255), server_default=text("NULL::character varying"))
    version = Column(Integer)
    type = Column(String(30), nullable=False, index=True)
    transaction_id = Column(String(36), nullable=False)
    owner_description = Column(String(255), index=True, server_default=text("NULL::character varying"))
    additional_fields = Column(Text, comment='(DC2Type:array)')
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='CASCADE'), index=True)

    customer_user = relationship('OroCustomerUser')
    impersonation = relationship('OroUserImpersonation')
    organization = relationship('OroOrganization')
    user = relationship('OroUser')


