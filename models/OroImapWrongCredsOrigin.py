from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroImapWrongCredsOrigin(Base):
    __tablename__ = 'oro_imap_wrong_creds_origin'

    origin_id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, index=True)


