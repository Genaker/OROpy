from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailMailboxProces(Base):
    __tablename__ = 'oro_email_mailbox_process'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_mailbox_process_id_seq'::regclass)"))
    type = Column(String(30), nullable=False)
    lead_channel_id = Column(ForeignKey('orocrm_channel.id', ondelete='SET NULL'), index=True)
    lead_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    lead_source_id = Column(String(32), server_default=text("NULL::character varying"))
    case_assign_to_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    case_status_name = Column(ForeignKey('orocrm_case_status.name', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    case_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    case_priority_name = Column(ForeignKey('orocrm_case_priority.name', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    case_assign_to = relationship('OroUser', primaryjoin='OroEmailMailboxProces.case_assign_to_id == OroUser.id')
    case_owner = relationship('OroUser', primaryjoin='OroEmailMailboxProces.case_owner_id == OroUser.id')
    orocrm_case_priority = relationship('OrocrmCasePriority')
    orocrm_case_statu = relationship('OrocrmCaseStatu')
    lead_channel = relationship('OrocrmChannel')
    lead_owner = relationship('OroUser', primaryjoin='OroEmailMailboxProces.lead_owner_id == OroUser.id')


