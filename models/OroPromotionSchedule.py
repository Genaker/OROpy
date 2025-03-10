from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPromotionSchedule(Base):
    __tablename__ = 'oro_promotion_schedule'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_promotion_schedule_id_seq'::regclass)"))
    promotion_id = Column(ForeignKey('oro_promotion.id', ondelete='CASCADE'), index=True)
    active_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    deactivate_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))

    promotion = relationship('OroPromotion')


