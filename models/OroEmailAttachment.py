from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailAttachment(Base):
    __tablename__ = 'oro_email_attachment'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_attachment_id_seq'::regclass)"))
    body_id = Column(ForeignKey('oro_email_body.id', ondelete='CASCADE'), index=True)
    file_id = Column(ForeignKey('oro_attachment_file.id', ondelete='SET NULL'), index=True)
    file_name = Column(String(255), nullable=False)
    content_type = Column(String(100), nullable=False)
    embedded_content_id = Column(String(255), server_default=text("NULL::character varying"))

    body = relationship('OroEmailBody')
    file = relationship('OroAttachmentFile')


