from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmCase(Base):
    __tablename__ = 'orocrm_case'
    __table_args__ = (
        Index('case_reported_at_idx', 'reportedat', 'id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_case_id_seq'::regclass)"))
    related_contact_id = Column(ForeignKey('orocrm_contact.id', ondelete='SET NULL'), index=True)
    related_account_id = Column(ForeignKey('orocrm_account.id', ondelete='SET NULL'), index=True)
    assigned_to_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    source_name = Column(ForeignKey('orocrm_case_source.name', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    status_name = Column(ForeignKey('orocrm_case_status.name', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    priority_name = Column(ForeignKey('orocrm_case_priority.name', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    subject = Column(String(255), nullable=False)
    description = Column(Text)
    resolution = Column(Text)
    createdat = Column(TIMESTAMP(precision=0), nullable=False)
    updatedat = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    reportedat = Column(TIMESTAMP(precision=0), nullable=False)
    closedat = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    serialized_data = Column(JSONB(astext_type=Text()))
    ac_last_contact_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_in = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_out = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_contact_count = Column(Integer)
    ac_contact_count_in = Column(Integer)
    ac_contact_count_out = Column(Integer)

    assigned_to = relationship('OroUser', primaryjoin='OrocrmCase.assigned_to_id == OroUser.id')
    organization = relationship('OroOrganization')
    owner = relationship('OroUser', primaryjoin='OrocrmCase.owner_id == OroUser.id')
    orocrm_case_priority = relationship('OrocrmCasePriority')
    related_account = relationship('OrocrmAccount')
    related_contact = relationship('OrocrmContact')
    orocrm_case_source = relationship('OrocrmCaseSource')
    orocrm_case_statu = relationship('OrocrmCaseStatu')
    notes = relationship('OroNote', secondary='oro_rel_6f8f552a9e0854fe254c12')
    emails = relationship('OroEmail', secondary='oro_rel_265353709e0854fe254c12')
    tasks = relationship('OrocrmTask', secondary='oro_rel_f24c741b9e0854fe254c12')


