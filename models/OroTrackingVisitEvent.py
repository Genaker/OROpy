from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTrackingVisitEvent(Base):
    __tablename__ = 'oro_tracking_visit_event'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tracking_visit_event_id_seq'::regclass)"))
    event_id = Column(ForeignKey('oro_tracking_event_dictionary.id', ondelete='CASCADE'), index=True)
    website_id = Column(ForeignKey('oro_tracking_website.id', ondelete='CASCADE'), index=True)
    visit_id = Column(ForeignKey('oro_tracking_visit.id', ondelete='CASCADE'), index=True)
    web_event_id = Column(ForeignKey('oro_tracking_event.id'), unique=True)
    parsing_count = Column(Integer, nullable=False, server_default=text("0"))
    code = Column(String(255), server_default=text("NULL::character varying"))
    campaign_a14160a8_id = Column(ForeignKey('orocrm_campaign.id', ondelete='SET NULL'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    campaign_a14160a8 = relationship('OrocrmCampaign')
    event = relationship('OroTrackingEventDictionary')
    visit = relationship('OroTrackingVisit')
    web_event = relationship('OroTrackingEvent')
    website = relationship('OroTrackingWebsite')


t_oro_user_access_group = Table(
    'oro_user_access_group', metadata,
    Column('user_id', ForeignKey('oro_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('group_id', ForeignKey('oro_access_group.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_user_access_group_role = Table(
    'oro_user_access_group_role', metadata,
    Column('group_id', ForeignKey('oro_access_group.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('role_id', ForeignKey('oro_access_role.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


