from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmAccount(Base):
    __tablename__ = 'orocrm_account'
    __table_args__ = (
        Index('account_name_idx', 'name', 'id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_account_id_seq'::regclass)"))
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    default_contact_id = Column(ForeignKey('orocrm_contact.id', ondelete='SET NULL'), index=True)
    referred_by_id = Column(ForeignKey('orocrm_account.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False)
    createdat = Column(TIMESTAMP(precision=0), nullable=False)
    updatedat = Column(TIMESTAMP(precision=0), nullable=False)
    extend_description = Column(Text)
    serialized_data = Column(JSONB(astext_type=Text()))
    ac_last_contact_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_in = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_out = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_contact_count = Column(Integer)
    ac_contact_count_in = Column(Integer)
    ac_contact_count_out = Column(Integer)

    default_contact = relationship('OrocrmContact')
    organization = relationship('OroOrganization')
    referred_by = relationship('OrocrmAccount', remote_side=[id])
    user_owner = relationship('OroUser')
    contacts = relationship('OrocrmContact', secondary='orocrm_account_to_contact')
    notes = relationship('OroNote', secondary='oro_rel_6f8f552ab28b6f3865ba50')
    emails = relationship('OroEmail', secondary='oro_rel_26535370b28b6f3865ba50')
    calendarevents = relationship('OroCalendarEvent', secondary='oro_rel_46a29d19b28b6f3865ba50')
    calls = relationship('OrocrmCall', secondary='oro_rel_6cbc8000b28b6f3865ba50')
    tasks = relationship('OrocrmTask', secondary='oro_rel_f24c741bb28b6f3865ba50')
    activitylists = relationship('OroActivityList', secondary='oro_rel_c3990ba6b28b6f38e2d624')


