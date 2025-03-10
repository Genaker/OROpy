from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailUser(Base):
    __tablename__ = 'oro_email_user'
    __table_args__ = (
        Index('received_idx', 'received', 'is_seen', 'mailbox_owner_id'),
        Index('user_owner_id_mailbox_owner_id_organization_id', 'user_owner_id', 'mailbox_owner_id', 'organization_id'),
        Index('seen_idx', 'is_seen', 'mailbox_owner_id')
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_user_id_seq'::regclass)"))
    email_id = Column(ForeignKey('oro_email.id', ondelete='CASCADE'), nullable=False, index=True)
    mailbox_owner_id = Column(ForeignKey('oro_email_mailbox.id', ondelete='SET NULL'), index=True)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    received = Column(TIMESTAMP(precision=0), nullable=False)
    is_seen = Column(Boolean, nullable=False, server_default=text("true"))
    is_private = Column(Boolean)
    unsyncedflagcount = Column(Integer, nullable=False, server_default=text("0"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='CASCADE'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    origin_id = Column(ForeignKey('oro_email_origin.id', ondelete='SET NULL'), index=True)

    email = relationship('OroEmail')
    mailbox_owner = relationship('OroEmailMailbox')
    organization = relationship('OroOrganization')
    origin = relationship('OroEmailOrigin')
    user_owner = relationship('OroUser')
    folders = relationship('OroEmailFolder', secondary='oro_email_user_folders')


t_oro_rel_6f8f552ad7fa01cde46c56 = Table(
    'oro_rel_6f8f552ad7fa01cde46c56', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('customeruserrole_id', ForeignKey('oro_customer_user_role.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba6d7fa01cd30d950 = Table(
    'oro_rel_c3990ba6d7fa01cd30d950', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('customeruserrole_id', ForeignKey('oro_customer_user_role.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


