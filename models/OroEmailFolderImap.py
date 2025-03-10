from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailFolderImap(Base):
    __tablename__ = 'oro_email_folder_imap'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_folder_imap_id_seq'::regclass)"))
    folder_id = Column(ForeignKey('oro_email_folder.id', ondelete='CASCADE'), nullable=False, unique=True)
    uid_validity = Column(Integer, nullable=False)
    last_uid = Column(Integer)

    folder = relationship('OroEmailFolder')


