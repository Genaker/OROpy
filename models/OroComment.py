from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroComment(Base):
    __tablename__ = 'oro_comment'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_comment_id_seq'::regclass)"))
    owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    updated_by_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    email_bb212599_id = Column(ForeignKey('oro_email.id', ondelete='SET NULL'), index=True)
    note_c0db526d_id = Column(ForeignKey('oro_note.id', ondelete='SET NULL'), index=True)
    attachment_id = Column(ForeignKey('oro_attachment_file.id', ondelete='SET NULL'), index=True)
    message = Column(Text, nullable=False)
    createdat = Column(TIMESTAMP(precision=0), nullable=False)
    updatedat = Column(TIMESTAMP(precision=0), nullable=False)
    calendar_event_78fb52b8_id = Column(ForeignKey('oro_calendar_event.id', ondelete='SET NULL'), index=True)
    call_41b3ba7d_id = Column(ForeignKey('orocrm_call.id', ondelete='SET NULL'), index=True)
    task_c50a6a28_id = Column(ForeignKey('orocrm_task.id', ondelete='SET NULL'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    attachment = relationship('OroAttachmentFile')
    calendar_event_78fb52b8 = relationship('OroCalendarEvent')
    call_41b3ba7d = relationship('OrocrmCall')
    email_bb212599 = relationship('OroEmail')
    note_c0db526d = relationship('OroNote')
    organization = relationship('OroOrganization')
    owner = relationship('OroUser', primaryjoin='OroComment.owner_id == OroUser.id')
    task_c50a6a28 = relationship('OrocrmTask')
    updated_by = relationship('OroUser', primaryjoin='OroComment.updated_by_id == OroUser.id')


