from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroSecurityPermission(Base):
    __tablename__ = 'oro_security_permission'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_security_permission_id_seq'::regclass)"))
    name = Column(String(255), nullable=False, unique=True)
    label = Column(String(255), nullable=False)
    description = Column(String(255), server_default=text("NULL::character varying"))
    is_apply_to_all = Column(Boolean, nullable=False)
    group_names = Column(Text, nullable=False, comment='(DC2Type:array)(DC2Type:array)')


