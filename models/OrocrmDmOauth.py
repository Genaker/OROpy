from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmDmOauth(Base):
    __tablename__ = 'orocrm_dm_oauth'
    __table_args__ = (
        Index('orocrm_dm_oauth_unq', 'channel_id', 'user_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_dm_oauth_id_seq'::regclass)"))
    channel_id = Column(ForeignKey('oro_integration_channel.id', ondelete='CASCADE'), index=True)
    user_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), index=True)
    refresh_token = Column(String(255), server_default=text("NULL::character varying"))

    channel = relationship('OroIntegrationChannel')
    user = relationship('OroUser')


