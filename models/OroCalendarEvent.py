from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCalendarEvent(Base):
    __tablename__ = 'oro_calendar_event'
    __table_args__ = (
        Index('oro_calendar_event_uid_idx', 'calendar_id', 'uid'),
        Index('oro_calendar_event_idx', 'calendar_id', 'start_at', 'end_at'),
        Index('oro_sys_calendar_event_idx', 'system_calendar_id', 'start_at', 'end_at')
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_calendar_event_id_seq'::regclass)"))
    calendar_id = Column(ForeignKey('oro_calendar.id', ondelete='CASCADE'), index=True)
    system_calendar_id = Column(ForeignKey('oro_system_calendar.id', ondelete='CASCADE'), index=True)
    parent_id = Column(ForeignKey('oro_calendar_event.id', ondelete='CASCADE'), index=True)
    related_attendee_id = Column(ForeignKey('oro_calendar_event_attendee.id', ondelete='SET NULL'), index=True)
    recurring_event_id = Column(ForeignKey('oro_calendar_event.id', ondelete='CASCADE'), index=True)
    recurrence_id = Column(ForeignKey('oro_calendar_recurrence.id', ondelete='SET NULL'), unique=True)
    organizer_user_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    uid = Column(String(36), server_default=text("NULL::character varying"))
    title = Column(String(255), nullable=False)
    description = Column(Text)
    start_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    end_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    all_day = Column(Boolean, nullable=False, server_default=text("false"))
    background_color = Column(String(7), server_default=text("NULL::character varying"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    original_start_at = Column(TIMESTAMP(precision=0), index=True, server_default=text("NULL::timestamp without time zone"))
    is_cancelled = Column(Boolean, nullable=False, server_default=text("false"))
    is_organizer = Column(Boolean)
    organizer_email = Column(String(255), server_default=text("NULL::character varying"))
    organizer_display_name = Column(String(255), server_default=text("NULL::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    calendar = relationship('OroCalendar')
    organizer_user = relationship('OroUser')
    parent = relationship('OroCalendarEvent', remote_side=[id], primaryjoin='OroCalendarEvent.parent_id == OroCalendarEvent.id')
    recurrence = relationship('OroCalendarRecurrence')
    recurring_event = relationship('OroCalendarEvent', remote_side=[id], primaryjoin='OroCalendarEvent.recurring_event_id == OroCalendarEvent.id')
    related_attendee = relationship('OroCalendarEventAttendee', primaryjoin='OroCalendarEvent.related_attendee_id == OroCalendarEventAttendee.id')
    system_calendar = relationship('OroSystemCalendar')
    orders = relationship('OroOrder', secondary='oro_rel_46a29d1934e8bc9c2ddbe0')
    requests = relationship('OroRfpRequest', secondary='oro_rel_46a29d19f42ab603ec4b1d')
    quotes = relationship('OroSaleQuote', secondary='oro_rel_46a29d19aab0e4f0b5ec88')
    customerusers = relationship('OroCustomerUser', secondary='oro_rel_46a29d193708e583c5ba51')
    contacts = relationship('OrocrmContact', secondary='oro_rel_46a29d1983dfdfa436b4e2')
    caseentitys = relationship('OrocrmCase', secondary='oro_rel_46a29d199e0854fe254c12')
    leads = relationship('OrocrmSalesLead', secondary='oro_rel_46a29d1988a3cef53c57d4')
    opportunitys = relationship('OrocrmSalesOpportunity', secondary='oro_rel_46a29d195154c0033bfb48')


