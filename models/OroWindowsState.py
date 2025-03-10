from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWindowsState(Base):
    __tablename__ = 'oro_windows_state'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_windows_state_id_seq'::regclass)"))
    user_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), nullable=False, index=True)
    data = Column(JSON, nullable=False, comment='(DC2Type:json_array)(DC2Type:json_array)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)

    user = relationship('OroUser')


