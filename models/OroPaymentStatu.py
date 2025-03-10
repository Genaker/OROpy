from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPaymentStatu(Base):
    __tablename__ = 'oro_payment_status'
    __table_args__ = (
        Index('oro_payment_status_unique', 'entity_class', 'entity_identifier', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_payment_status_id_seq'::regclass)"))
    entity_class = Column(String(255), nullable=False)
    entity_identifier = Column(Integer, nullable=False)
    payment_status = Column(String(255), nullable=False)


