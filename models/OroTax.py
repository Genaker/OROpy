from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTax(Base):
    __tablename__ = 'oro_tax'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tax_id_seq'::regclass)"))
    code = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    rate = Column(Float(53), nullable=False, comment='(DC2Type:percent)(DC2Type:percent)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)


