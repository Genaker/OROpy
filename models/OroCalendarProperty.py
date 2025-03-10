from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCalendarProperty(Base):
    __tablename__ = 'oro_calendar_property'
    __table_args__ = (
        Index('oro_calendar_prop_uq', 'calendar_alias', 'calendar_id', 'target_calendar_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_calendar_property_id_seq'::regclass)"))
    target_calendar_id = Column(ForeignKey('oro_calendar.id', ondelete='CASCADE'), nullable=False, index=True)
    calendar_alias = Column(String(32), nullable=False)
    calendar_id = Column(Integer, nullable=False)
    position = Column(Integer, nullable=False, server_default=text("0"))
    visible = Column(Boolean, nullable=False, server_default=text("true"))
    background_color = Column(String(7), server_default=text("NULL::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    target_calendar = relationship('OroCalendar')


