from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroRule(Base):
    __tablename__ = 'oro_rule'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_rule_id_seq'::regclass)"))
    name = Column(Text, nullable=False)
    enabled = Column(Boolean, nullable=False, server_default=text("true"))
    sort_order = Column(Integer, nullable=False)
    stop_processing = Column(Boolean, nullable=False, server_default=text("false"))
    expression = Column(Text)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    serialized_data = Column(JSONB(astext_type=Text()))


