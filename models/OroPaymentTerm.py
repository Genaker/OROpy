from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPaymentTerm(Base):
    __tablename__ = 'oro_payment_term'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_payment_term_id_seq'::regclass)"))
    label = Column(String(255), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))


