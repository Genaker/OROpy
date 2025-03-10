from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPriceListCombined(Base):
    __tablename__ = 'oro_price_list_combined'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_price_list_combined_id_seq'::regclass)"))
    name = Column(String(255), nullable=False)
    is_enabled = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    is_prices_calculated = Column(Boolean, nullable=False)


