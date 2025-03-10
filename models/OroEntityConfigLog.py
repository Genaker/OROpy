from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEntityConfigLog(Base):
    __tablename__ = 'oro_entity_config_log'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_entity_config_log_id_seq'::regclass)"))
    user_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), index=True)
    logged_at = Column(TIMESTAMP(precision=0), nullable=False)

    user = relationship('OroUser')


