from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroUserImpersonation(Base):
    __tablename__ = 'oro_user_impersonation'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_user_impersonation_id_seq'::regclass)"))
    user_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), nullable=False, index=True)
    token = Column(String(255), nullable=False, index=True)
    expire_at = Column(TIMESTAMP(precision=0), nullable=False)
    login_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    notify = Column(Boolean, nullable=False, server_default=text("false"))
    ip_address = Column(String(255), nullable=False, index=True, server_default=text("'127.0.0.1'::character varying"))

    user = relationship('OroUser')


