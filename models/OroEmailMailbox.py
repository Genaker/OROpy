from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailMailbox(Base):
    __tablename__ = 'oro_email_mailbox'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_mailbox_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    process_settings_id = Column(ForeignKey('oro_email_mailbox_process.id'), unique=True)
    origin_id = Column(ForeignKey('oro_email_origin.id'), unique=True)
    email = Column(String(255), nullable=False, unique=True)
    label = Column(String(255), nullable=False, unique=True)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')

    organization = relationship('OroOrganization')
    origin = relationship('OroEmailOrigin')
    process_settings = relationship('OroEmailMailboxProces')
    users = relationship('OroUser', secondary='oro_email_mailbox_users')
    roles = relationship('OroAccessRole', secondary='oro_email_mailbox_roles')


t_oro_rel_26535370e65dd9d390636c = Table(
    'oro_rel_26535370e65dd9d390636c', metadata,
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('b2bcustomer_id', ForeignKey('orocrm_sales_b2bcustomer.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_46a29d19e65dd9d390636c = Table(
    'oro_rel_46a29d19e65dd9d390636c', metadata,
    Column('calendarevent_id', ForeignKey('oro_calendar_event.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('b2bcustomer_id', ForeignKey('orocrm_sales_b2bcustomer.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6cbc8000e65dd9d390636c = Table(
    'oro_rel_6cbc8000e65dd9d390636c', metadata,
    Column('call_id', ForeignKey('orocrm_call.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('b2bcustomer_id', ForeignKey('orocrm_sales_b2bcustomer.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552a784fec5f9c970f = Table(
    'oro_rel_6f8f552a784fec5f9c970f', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('customer_id', ForeignKey('oro_customer.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba6784fec5f6e321b = Table(
    'oro_rel_c3990ba6784fec5f6e321b', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('customer_id', ForeignKey('oro_customer.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba6e65dd9d37deb67 = Table(
    'oro_rel_c3990ba6e65dd9d37deb67', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('b2bcustomer_id', ForeignKey('orocrm_sales_b2bcustomer.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_f24c741be65dd9d390636c = Table(
    'oro_rel_f24c741be65dd9d390636c', metadata,
    Column('task_id', ForeignKey('orocrm_task.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('b2bcustomer_id', ForeignKey('orocrm_sales_b2bcustomer.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_web_catalog_variant_slug = Table(
    'oro_web_catalog_variant_slug', metadata,
    Column('content_variant_id', ForeignKey('oro_web_catalog_variant.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('slug_id', ForeignKey('oro_redirect_slug.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


