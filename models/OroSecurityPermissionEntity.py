from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroSecurityPermissionEntity(Base):
    __tablename__ = 'oro_security_permission_entity'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_security_permission_entity_id_seq'::regclass)"))
    name = Column(String(255), nullable=False, unique=True)

    permissions = relationship('OroSecurityPermission', secondary='oro_security_perm_excl_entity')
    permissions1 = relationship('OroSecurityPermission', secondary='oro_security_perm_apply_entity')


