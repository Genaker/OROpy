from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class AclClass(Base):
    __tablename__ = 'acl_classes'

    id = Column(Integer, primary_key=True, server_default=text("nextval('acl_classes_id_seq'::regclass)"))
    class_type = Column(String(200), nullable=False, unique=True)


