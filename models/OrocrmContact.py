from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmContact(Base):
    __tablename__ = 'orocrm_contact'
    __table_args__ = (
        Index('contact_name_idx', 'last_name', 'first_name', 'id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_contact_id_seq'::regclass)"))
    assigned_to_user_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    updated_by_user_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    created_by_user_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    reports_to_contact_id = Column(ForeignKey('orocrm_contact.id', ondelete='SET NULL'), index=True)
    method_name = Column(ForeignKey('orocrm_contact_method.name'), index=True, server_default=text("NULL::character varying"))
    source_name = Column(ForeignKey('orocrm_contact_source.name'), index=True, server_default=text("NULL::character varying"))
    picture_id = Column(ForeignKey('oro_attachment_file.id', ondelete='SET NULL'), index=True)
    name_prefix = Column(String(255), server_default=text("NULL::character varying"))
    first_name = Column(String(255), index=True, server_default=text("NULL::character varying"))
    middle_name = Column(String(255), server_default=text("NULL::character varying"))
    last_name = Column(String(255), server_default=text("NULL::character varying"))
    name_suffix = Column(String(255), server_default=text("NULL::character varying"))
    gender = Column(String(8), server_default=text("NULL::character varying"))
    birthday = Column(Date)
    description = Column(Text)
    job_title = Column(String(255), server_default=text("NULL::character varying"))
    fax = Column(String(255), server_default=text("NULL::character varying"))
    skype = Column(String(255), server_default=text("NULL::character varying"))
    twitter = Column(String(255), server_default=text("NULL::character varying"))
    facebook = Column(String(255), server_default=text("NULL::character varying"))
    google_plus = Column(String(255), server_default=text("NULL::character varying"))
    linkedin = Column(String(255), server_default=text("NULL::character varying"))
    createdat = Column(TIMESTAMP(precision=0), nullable=False)
    updatedat = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    email = Column(String(255), server_default=text("NULL::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))
    ac_last_contact_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_in = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_out = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_contact_count = Column(Integer)
    ac_contact_count_in = Column(Integer)
    ac_contact_count_out = Column(Integer)

    assigned_to_user = relationship('OroUser', primaryjoin='OrocrmContact.assigned_to_user_id == OroUser.id')
    created_by_user = relationship('OroUser', primaryjoin='OrocrmContact.created_by_user_id == OroUser.id')
    orocrm_contact_method = relationship('OrocrmContactMethod')
    organization = relationship('OroOrganization')
    picture = relationship('OroAttachmentFile')
    reports_to_contact = relationship('OrocrmContact', remote_side=[id])
    orocrm_contact_source = relationship('OrocrmContactSource')
    updated_by_user = relationship('OroUser', primaryjoin='OrocrmContact.updated_by_user_id == OroUser.id')
    user_owner = relationship('OroUser', primaryjoin='OrocrmContact.user_owner_id == OroUser.id')
    emails = relationship('OroEmail', secondary='oro_rel_2653537083dfdfa436b4e2')
    notes = relationship('OroNote', secondary='oro_rel_6f8f552a83dfdfa436b4e2')
    tasks = relationship('OrocrmTask', secondary='oro_rel_f24c741b83dfdfa436b4e2')


