from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroRedirectSlug(Base):
    __tablename__ = 'oro_redirect_slug'
    __table_args__ = (
        UniqueConstraint('organization_id', 'url_hash', 'scopes_hash'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_redirect_slug_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    localization_id = Column(ForeignKey('oro_localization.id', ondelete='CASCADE'), index=True)
    url_hash = Column(String(32), nullable=False, index=True)
    route_name = Column(String(255), nullable=False, index=True)
    url = Column(String(1024), nullable=False)
    slug_prototype = Column(String(255), index=True, server_default=text("NULL::character varying"))
    route_parameters = Column(Text, nullable=False, comment='(DC2Type:array)(DC2Type:array)')
    parameters_hash = Column(String(32), nullable=False, index=True)
    scopes_hash = Column(String(32), nullable=False)

    localization = relationship('OroLocalization')
    organization = relationship('OroOrganization')


t_oro_rel_26535370b28b6f3865ba50 = Table(
    'oro_rel_26535370b28b6f3865ba50', metadata,
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('account_id', ForeignKey('orocrm_account.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_46a29d19b28b6f3865ba50 = Table(
    'oro_rel_46a29d19b28b6f3865ba50', metadata,
    Column('calendarevent_id', ForeignKey('oro_calendar_event.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('account_id', ForeignKey('orocrm_account.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6cbc8000b28b6f3865ba50 = Table(
    'oro_rel_6cbc8000b28b6f3865ba50', metadata,
    Column('call_id', ForeignKey('orocrm_call.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('account_id', ForeignKey('orocrm_account.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552a16cbf45882508f = Table(
    'oro_rel_6f8f552a16cbf45882508f', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('customergroup_id', ForeignKey('oro_customer_group.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552a758542cfbd3dfc = Table(
    'oro_rel_6f8f552a758542cfbd3dfc', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('webcatalog_id', ForeignKey('oro_web_catalog.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552ab28b6f3865ba50 = Table(
    'oro_rel_6f8f552ab28b6f3865ba50', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('account_id', ForeignKey('orocrm_account.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552aff3a7b97ec3308 = Table(
    'oro_rel_6f8f552aff3a7b97ec3308', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('category_id', ForeignKey('oro_catalog_category.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba616cbf45899499b = Table(
    'oro_rel_c3990ba616cbf45899499b', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('customergroup_id', ForeignKey('oro_customer_group.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba6758542cf1cec5e = Table(
    'oro_rel_c3990ba6758542cf1cec5e', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('webcatalog_id', ForeignKey('oro_web_catalog.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba6b28b6f38e2d624 = Table(
    'oro_rel_c3990ba6b28b6f38e2d624', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('account_id', ForeignKey('orocrm_account.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba6ff3a7b97760f68 = Table(
    'oro_rel_c3990ba6ff3a7b97760f68', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('category_id', ForeignKey('oro_catalog_category.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_f24c741bb28b6f3865ba50 = Table(
    'oro_rel_f24c741bb28b6f3865ba50', metadata,
    Column('task_id', ForeignKey('orocrm_task.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('account_id', ForeignKey('orocrm_account.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


