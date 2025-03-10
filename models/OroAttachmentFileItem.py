from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroAttachmentFileItem(Base):
    __tablename__ = 'oro_attachment_file_item'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_attachment_file_item_id_seq'::regclass)"))
    file_id = Column(ForeignKey('oro_attachment_file.id', ondelete='CASCADE'), unique=True)
    sort_order = Column(Integer, nullable=False, server_default=text("0"))
    serialized_data = Column(JSONB(astext_type=Text()))

    file = relationship('OroAttachmentFile')


