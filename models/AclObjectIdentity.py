from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class AclObjectIdentity(Base):
    __tablename__ = 'acl_object_identities'
    __table_args__ = (
        Index('uniq_9407e5494b12ad6ea000b10', 'object_identifier', 'class_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('acl_object_identities_id_seq'::regclass)"))
    parent_object_identity_id = Column(ForeignKey('acl_object_identities.id'), index=True)
    class_id = Column(Integer, nullable=False)
    object_identifier = Column(String(100), nullable=False)
    entries_inheriting = Column(Boolean, nullable=False)

    parent_object_identity = relationship('AclObjectIdentity', remote_side=[id])
    object_identitys = relationship(
        'AclObjectIdentity',
        secondary='acl_object_identity_ancestors',
        primaryjoin='AclObjectIdentity.id == acl_object_identity_ancestors.c.ancestor_id',
        secondaryjoin='AclObjectIdentity.id == acl_object_identity_ancestors.c.object_identity_id'
    )


