from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPriceListSchedule(Base):
    __tablename__ = 'oro_price_list_schedule'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_price_list_schedule_id_seq'::regclass)"))
    price_list_id = Column(ForeignKey('oro_price_list.id', ondelete='CASCADE'), index=True)
    active_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    deactivate_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))

    price_list = relationship('OroPriceList')


