from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmChannelEntityName(Base):
    __tablename__ = 'orocrm_channel_entity_name'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_channel_entity_name_id_seq'::regclass)"))
    channel_id = Column(ForeignKey('orocrm_channel.id', ondelete='CASCADE'), index=True)
    name = Column(String(255), nullable=False)

    channel = relationship('OrocrmChannel')


