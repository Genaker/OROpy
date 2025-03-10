from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroMessageQueue(Base):
    __tablename__ = 'oro_message_queue'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_message_queue_id_seq'::regclass)"))
    body = Column(Text)
    headers = Column(Text)
    properties = Column(Text)
    consumer_id = Column(String(255), server_default=text("NULL::character varying"))
    redelivered = Column(Boolean)
    queue = Column(String(255), nullable=False)
    priority = Column(SmallInteger, nullable=False)
    delayed_until = Column(Integer)


