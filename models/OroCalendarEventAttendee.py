from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCalendarEventAttendee(Base):
    __tablename__ = 'oro_calendar_event_attendee'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_calendar_event_attendee_id_seq'::regclass)"))
    user_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    calendar_event_id = Column(ForeignKey('oro_calendar_event.id', ondelete='CASCADE'), index=True)
    status_id = Column(ForeignKey('oro_enum_ce_attendee_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    type_id = Column(ForeignKey('oro_enum_ce_attendee_type.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    email = Column(String(255), server_default=text("NULL::character varying"))
    display_name = Column(String(255), server_default=text("NULL::character varying"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    calendar_event = relationship('OroCalendarEvent', primaryjoin='OroCalendarEventAttendee.calendar_event_id == OroCalendarEvent.id')
    status = relationship('OroEnumCeAttendeeStatu')
    type = relationship('OroEnumCeAttendeeType')
    user = relationship('OroUser')


