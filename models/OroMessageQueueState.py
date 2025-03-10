from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroMessageQueueState(Base):
    __tablename__ = 'oro_message_queue_state'

    id = Column(String(15), primary_key=True)
    updated_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))


