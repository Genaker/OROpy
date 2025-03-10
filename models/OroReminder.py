from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroReminder(Base):
    __tablename__ = 'oro_reminder'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_reminder_id_seq'::regclass)"))
    recipient_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), index=True)
    sender_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    subject = Column(String(255), nullable=False)
    start_at = Column(TIMESTAMP(precision=0), nullable=False)
    expire_at = Column(TIMESTAMP(precision=0), nullable=False)
    method = Column(String(255), nullable=False)
    interval_number = Column(Integer, nullable=False)
    interval_unit = Column(String(1), nullable=False)
    state = Column(String(32), nullable=False, index=True)
    related_entity_id = Column(Integer, nullable=False)
    related_entity_classname = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    sent_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    failure_exception = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    serialized_data = Column(JSONB(astext_type=Text()))

    recipient = relationship('OroUser', primaryjoin='OroReminder.recipient_id == OroUser.id')
    sender = relationship('OroUser', primaryjoin='OroReminder.sender_id == OroUser.id')


