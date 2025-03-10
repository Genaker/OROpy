from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailImap(Base):
    __tablename__ = 'oro_email_imap'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_imap_id_seq'::regclass)"))
    email_id = Column(ForeignKey('oro_email.id', ondelete='CASCADE'), nullable=False, index=True)
    imap_folder_id = Column(ForeignKey('oro_email_folder_imap.id', ondelete='CASCADE'), nullable=False, index=True)
    uid = Column(Integer, nullable=False, index=True)

    email = relationship('OroEmail')
    imap_folder = relationship('OroEmailFolderImap')


