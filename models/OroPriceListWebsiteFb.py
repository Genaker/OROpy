from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPriceListWebsiteFb(Base):
    __tablename__ = 'oro_price_list_website_fb'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_price_list_website_fb_id_seq'::regclass)"))
    website_id = Column(ForeignKey('oro_website.id', ondelete='CASCADE'), nullable=False, unique=True)
    fallback = Column(Integer, nullable=False)

    website = relationship('OroWebsite')


t_oro_rel_2653537088a3cef53c57d4 = Table(
    'oro_rel_2653537088a3cef53c57d4', metadata,
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('lead_id', ForeignKey('orocrm_sales_lead.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_46a29d1988a3cef53c57d4 = Table(
    'oro_rel_46a29d1988a3cef53c57d4', metadata,
    Column('calendarevent_id', ForeignKey('oro_calendar_event.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('lead_id', ForeignKey('orocrm_sales_lead.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6cbc800088a3cef53c57d4 = Table(
    'oro_rel_6cbc800088a3cef53c57d4', metadata,
    Column('call_id', ForeignKey('orocrm_call.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('lead_id', ForeignKey('orocrm_sales_lead.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552a88a3cef53c57d4 = Table(
    'oro_rel_6f8f552a88a3cef53c57d4', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('lead_id', ForeignKey('orocrm_sales_lead.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552a88d2647be4fd56 = Table(
    'oro_rel_6f8f552a88d2647be4fd56', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('website_id', ForeignKey('oro_website.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba688a3cef5c8efa6 = Table(
    'oro_rel_c3990ba688a3cef5c8efa6', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('lead_id', ForeignKey('orocrm_sales_lead.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba688d2647b59a3ef = Table(
    'oro_rel_c3990ba688d2647b59a3ef', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('website_id', ForeignKey('oro_website.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_f24c741b88a3cef53c57d4 = Table(
    'oro_rel_f24c741b88a3cef53c57d4', metadata,
    Column('task_id', ForeignKey('orocrm_task.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('lead_id', ForeignKey('orocrm_sales_lead.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_related_website = Table(
    'oro_related_website', metadata,
    Column('website_id', ForeignKey('oro_website.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('related_website_id', ForeignKey('oro_website.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


