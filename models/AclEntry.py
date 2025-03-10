from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class AclEntry(Base):
    __tablename__ = 'acl_entries'
    __table_args__ = (
        Index('uniq_46c8b806ea000b103d9ab4a64def17bce4289bf4', 'class_id', 'object_identity_id', 'field_name', 'ace_order', unique=True),
        Index('idx_46c8b806ea000b103d9ab4a6df9183c9', 'class_id', 'object_identity_id', 'security_identity_id')
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('acl_entries_id_seq'::regclass)"))
    class_id = Column(ForeignKey('acl_classes.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    object_identity_id = Column(ForeignKey('acl_object_identities.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    security_identity_id = Column(ForeignKey('acl_security_identities.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    field_name = Column(String(255), server_default=text("NULL::character varying"))
    ace_order = Column(SmallInteger, nullable=False)
    mask = Column(Integer, nullable=False)
    granting = Column(Boolean, nullable=False)
    granting_strategy = Column(String(30), nullable=False)
    audit_success = Column(Boolean, nullable=False)
    audit_failure = Column(Boolean, nullable=False)

    _class = relationship('AclClass')
    object_identity = relationship('AclObjectIdentity')
    security_identity = relationship('AclSecurityIdentity')


t_acl_object_identity_ancestors = Table(
    'acl_object_identity_ancestors', metadata,
    Column('object_identity_id', ForeignKey('acl_object_identities.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('ancestor_id', ForeignKey('acl_object_identities.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
)


