from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmCaseComment(Base):
    __tablename__ = 'orocrm_case_comment'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_case_comment_id_seq'::regclass)"))
    case_id = Column(ForeignKey('orocrm_case.id', ondelete='CASCADE'), index=True)
    updated_by_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    contact_id = Column(ForeignKey('orocrm_contact.id', ondelete='SET NULL'), index=True)
    attachment_id = Column(ForeignKey('oro_attachment_file.id', ondelete='SET NULL'), index=True)
    message = Column(Text, nullable=False)
    public = Column(Boolean, nullable=False, server_default=text("false"))
    createdat = Column(TIMESTAMP(precision=0), nullable=False)
    updatedat = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    attachment = relationship('OroAttachmentFile')
    case = relationship('OrocrmCase')
    contact = relationship('OrocrmContact')
    organization = relationship('OroOrganization')
    owner = relationship('OroUser', primaryjoin='OrocrmCaseComment.owner_id == OroUser.id')
    updated_by = relationship('OroUser', primaryjoin='OrocrmCaseComment.updated_by_id == OroUser.id')


