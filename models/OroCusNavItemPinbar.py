from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCusNavItemPinbar(Base):
    __tablename__ = 'oro_cus_nav_item_pinbar'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cus_nav_item_pinbar_id_seq'::regclass)"))
    item_id = Column(ForeignKey('oro_cus_navigation_item.id', ondelete='CASCADE'), nullable=False, unique=True)
    title = Column(String(255), nullable=False)
    title_short = Column(String(255), nullable=False)
    maximized = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))

    item = relationship('OroCusNavigationItem')


