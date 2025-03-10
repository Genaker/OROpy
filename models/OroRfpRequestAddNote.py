from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroRfpRequestAddNote(Base):
    __tablename__ = 'oro_rfp_request_add_note'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_rfp_request_add_note_id_seq'::regclass)"))
    request_id = Column(ForeignKey('oro_rfp_request.id', ondelete='CASCADE'), index=True)
    type = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    user_id = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    request = relationship('OroRfpRequest')


