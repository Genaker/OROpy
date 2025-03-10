from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailRecipient(Base):
    __tablename__ = 'oro_email_recipient'
    __table_args__ = (
        Index('email_id_type_idx', 'email_id', 'type'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_recipient_id_seq'::regclass)"))
    email_address_id = Column(ForeignKey('oro_email_address.id'), nullable=False, index=True)
    email_id = Column(ForeignKey('oro_email.id', ondelete='CASCADE'), index=True)
    name = Column(String(320), nullable=False)
    type = Column(String(3), nullable=False)

    email_address = relationship('OroEmailAddres')
    email = relationship('OroEmail')


