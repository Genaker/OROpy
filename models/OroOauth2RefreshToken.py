from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroOauth2RefreshToken(Base):
    __tablename__ = 'oro_oauth2_refresh_token'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_oauth2_refresh_token_id_seq'::regclass)"))
    access_token_id = Column(ForeignKey('oro_oauth2_access_token.id', ondelete='CASCADE'), index=True)
    identifier = Column(String(80), nullable=False, unique=True)
    expires_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    revoked = Column(Boolean, nullable=False, server_default=text("false"))

    access_token = relationship('OroOauth2AccessToken')


