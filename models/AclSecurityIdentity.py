from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class AclSecurityIdentity(Base):
    __tablename__ = 'acl_security_identities'
    __table_args__ = (
        Index('uniq_8835ee78772e836af85e0677', 'identifier', 'username', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('acl_security_identities_id_seq'::regclass)"))
    identifier = Column(String(200), nullable=False)
    username = Column(Boolean, nullable=False)


