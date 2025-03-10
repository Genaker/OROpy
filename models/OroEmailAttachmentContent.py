from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailAttachmentContent(Base):
    __tablename__ = 'oro_email_attachment_content'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_attachment_content_id_seq'::regclass)"))
    attachment_id = Column(ForeignKey('oro_email_attachment.id', ondelete='CASCADE'), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    content_transfer_encoding = Column(String(20), nullable=False)

    attachment = relationship('OroEmailAttachment')


