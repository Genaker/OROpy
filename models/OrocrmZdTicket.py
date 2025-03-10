from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmZdTicket(Base):
    __tablename__ = 'orocrm_zd_ticket'
    __table_args__ = (
        Index('zd_ticket_oid_cid_unq', 'origin_id', 'channel_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_zd_ticket_id_seq'::regclass)"))
    problem_id = Column(ForeignKey('orocrm_zd_ticket.id', ondelete='SET NULL'), index=True)
    assignee_id = Column(ForeignKey('orocrm_zd_user.id', ondelete='SET NULL'), index=True)
    status_name = Column(ForeignKey('orocrm_zd_ticket_status.name', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    submitter_id = Column(ForeignKey('orocrm_zd_user.id', ondelete='SET NULL'), index=True)
    priority_name = Column(ForeignKey('orocrm_zd_ticket_priority.name', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    requester_id = Column(ForeignKey('orocrm_zd_user.id', ondelete='SET NULL'), index=True)
    case_id = Column(ForeignKey('orocrm_case.id', ondelete='SET NULL'), unique=True)
    channel_id = Column(ForeignKey('oro_integration_channel.id', ondelete='CASCADE'), index=True)
    type_name = Column(ForeignKey('orocrm_zd_ticket_type.name', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    origin_id = Column(BigInteger)
    url = Column(String(255), server_default=text("NULL::character varying"))
    external_id = Column(String(50), server_default=text("NULL::character varying"))
    subject = Column(String(255), server_default=text("NULL::character varying"))
    description = Column(Text)
    recipient_email = Column(String(100), server_default=text("NULL::character varying"))
    has_incidents = Column(Boolean, nullable=False, server_default=text("false"))
    due_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    origin_created_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    created_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    updated_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    origin_updated_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))

    assignee = relationship('OrocrmZdUser', primaryjoin='OrocrmZdTicket.assignee_id == OrocrmZdUser.id')
    case = relationship('OrocrmCase')
    channel = relationship('OroIntegrationChannel')
    orocrm_zd_ticket_priority = relationship('OrocrmZdTicketPriority')
    problem = relationship('OrocrmZdTicket', remote_side=[id])
    requester = relationship('OrocrmZdUser', primaryjoin='OrocrmZdTicket.requester_id == OrocrmZdUser.id')
    orocrm_zd_ticket_statu = relationship('OrocrmZdTicketStatu')
    submitter = relationship('OrocrmZdUser', primaryjoin='OrocrmZdTicket.submitter_id == OrocrmZdUser.id')
    orocrm_zd_ticket_type = relationship('OrocrmZdTicketType')
    users = relationship('OrocrmZdUser', secondary='orocrm_zd_ticket_collaborators')


t_oro_consent_name = Table(
    'oro_consent_name', metadata,
    Column('consent_id', ForeignKey('oro_consent.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


