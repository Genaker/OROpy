from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroOauth2AccessToken(Base):
    __tablename__ = 'oro_oauth2_access_token'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_oauth2_access_token_id_seq'::regclass)"))
    client_id = Column(ForeignKey('oro_oauth2_client.id', ondelete='CASCADE'), index=True)
    identifier = Column(String(80), nullable=False, unique=True)
    expires_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    scopes = Column(Text, comment='(DC2Type:simple_array)(DC2Type:simple_array)')
    user_identifier = Column(String(128), server_default=text("NULL::character varying"))
    revoked = Column(Boolean, nullable=False, server_default=text("false"))

    client = relationship('OroOauth2Client')


