from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroGridViewUserRel(Base):
    __tablename__ = 'oro_grid_view_user_rel'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_grid_view_user_rel_id_seq'::regclass)"))
    user_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    grid_view_id = Column(ForeignKey('oro_grid_view.id', ondelete='CASCADE'), index=True)
    alias = Column(String(255), nullable=False)
    grid_name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False, index=True)
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='SET NULL'), index=True)

    customer_user = relationship('OroCustomerUser')
    grid_view = relationship('OroGridView')
    user = relationship('OroUser')


