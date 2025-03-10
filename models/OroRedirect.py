from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroRedirect(Base):
    __tablename__ = 'oro_redirect'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_redirect_id_seq'::regclass)"))
    slug_id = Column(ForeignKey('oro_redirect_slug.id', ondelete='CASCADE'), index=True)
    redirect_from_prototype = Column(String(255), index=True, server_default=text("NULL::character varying"))
    redirect_from = Column(String(1024), nullable=False)
    redirect_to_prototype = Column(String(255), server_default=text("NULL::character varying"))
    redirect_to = Column(String(1024), nullable=False)
    redirect_type = Column(Integer, nullable=False)
    from_hash = Column(String(32), nullable=False, index=True)

    slug = relationship('OroRedirectSlug')
    scopes = relationship('OroScope', secondary='oro_redirect_scope')


t_oro_rel_1cf73d3121a159ae2725f3 = Table(
    'oro_rel_1cf73d3121a159ae2725f3', metadata,
    Column('product_id', ForeignKey('oro_product.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localizedfallbackvalue_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_1cf73d3121a159ae6e1a29 = Table(
    'oro_rel_1cf73d3121a159ae6e1a29', metadata,
    Column('product_id', ForeignKey('oro_product.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localizedfallbackvalue_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_1cf73d3121a159aea3971e = Table(
    'oro_rel_1cf73d3121a159aea3971e', metadata,
    Column('product_id', ForeignKey('oro_product.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localizedfallbackvalue_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_265353709e0854fe254c12 = Table(
    'oro_rel_265353709e0854fe254c12', metadata,
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('caseentity_id', ForeignKey('orocrm_case.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_46a29d199e0854fe254c12 = Table(
    'oro_rel_46a29d199e0854fe254c12', metadata,
    Column('calendarevent_id', ForeignKey('oro_calendar_event.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('caseentity_id', ForeignKey('orocrm_case.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_5b5187a321a159ae2725f3 = Table(
    'oro_rel_5b5187a321a159ae2725f3', metadata,
    Column('contentnode_id', ForeignKey('oro_web_catalog_content_node.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localizedfallbackvalue_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_5b5187a321a159ae6e1a29 = Table(
    'oro_rel_5b5187a321a159ae6e1a29', metadata,
    Column('contentnode_id', ForeignKey('oro_web_catalog_content_node.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localizedfallbackvalue_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_5b5187a321a159aea3971e = Table(
    'oro_rel_5b5187a321a159aea3971e', metadata,
    Column('contentnode_id', ForeignKey('oro_web_catalog_content_node.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localizedfallbackvalue_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6cbc80009e0854fe254c12 = Table(
    'oro_rel_6cbc80009e0854fe254c12', metadata,
    Column('call_id', ForeignKey('orocrm_call.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('caseentity_id', ForeignKey('orocrm_case.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552a43ecff72f0d342 = Table(
    'oro_rel_6f8f552a43ecff72f0d342', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('promotion_id', ForeignKey('oro_promotion.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552a5b5187a347fdf8 = Table(
    'oro_rel_6f8f552a5b5187a347fdf8', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('contentnode_id', ForeignKey('oro_web_catalog_content_node.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552a9e0854fe254c12 = Table(
    'oro_rel_6f8f552a9e0854fe254c12', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('caseentity_id', ForeignKey('orocrm_case.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_b438191e21a159ae2725f3 = Table(
    'oro_rel_b438191e21a159ae2725f3', metadata,
    Column('page_id', ForeignKey('oro_cms_page.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localizedfallbackvalue_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_b438191e21a159ae6e1a29 = Table(
    'oro_rel_b438191e21a159ae6e1a29', metadata,
    Column('page_id', ForeignKey('oro_cms_page.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localizedfallbackvalue_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_b438191e21a159aea3971e = Table(
    'oro_rel_b438191e21a159aea3971e', metadata,
    Column('page_id', ForeignKey('oro_cms_page.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localizedfallbackvalue_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba643ecff72e2f6de = Table(
    'oro_rel_c3990ba643ecff72e2f6de', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('promotion_id', ForeignKey('oro_promotion.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba65b5187a374e72c = Table(
    'oro_rel_c3990ba65b5187a374e72c', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('contentnode_id', ForeignKey('oro_web_catalog_content_node.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba69e0854fe1d2e0c = Table(
    'oro_rel_c3990ba69e0854fe1d2e0c', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('caseentity_id', ForeignKey('orocrm_case.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_dd93d65c21a159ae2725f3 = Table(
    'oro_rel_dd93d65c21a159ae2725f3', metadata,
    Column('brand_id', ForeignKey('oro_brand.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localizedfallbackvalue_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_dd93d65c21a159ae6e1a29 = Table(
    'oro_rel_dd93d65c21a159ae6e1a29', metadata,
    Column('brand_id', ForeignKey('oro_brand.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localizedfallbackvalue_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_dd93d65c21a159aea3971e = Table(
    'oro_rel_dd93d65c21a159aea3971e', metadata,
    Column('brand_id', ForeignKey('oro_brand.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localizedfallbackvalue_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_f24c741b9e0854fe254c12 = Table(
    'oro_rel_f24c741b9e0854fe254c12', metadata,
    Column('task_id', ForeignKey('orocrm_task.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('caseentity_id', ForeignKey('orocrm_case.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_ff3a7b9721a159ae2725f3 = Table(
    'oro_rel_ff3a7b9721a159ae2725f3', metadata,
    Column('category_id', ForeignKey('oro_catalog_category.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localizedfallbackvalue_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_ff3a7b9721a159ae6e1a29 = Table(
    'oro_rel_ff3a7b9721a159ae6e1a29', metadata,
    Column('category_id', ForeignKey('oro_catalog_category.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localizedfallbackvalue_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_ff3a7b9721a159aea3971e = Table(
    'oro_rel_ff3a7b9721a159aea3971e', metadata,
    Column('category_id', ForeignKey('oro_catalog_category.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localizedfallbackvalue_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_ups_transport_label = Table(
    'oro_ups_transport_label', metadata,
    Column('transport_id', ForeignKey('oro_integration_transport.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_web_catalog_node_slug_prot = Table(
    'oro_web_catalog_node_slug_prot', metadata,
    Column('node_id', ForeignKey('oro_web_catalog_content_node.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_web_catalog_node_title = Table(
    'oro_web_catalog_node_title', metadata,
    Column('node_id', ForeignKey('oro_web_catalog_content_node.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_web_catalog_node_url = Table(
    'oro_web_catalog_node_url', metadata,
    Column('node_id', ForeignKey('oro_web_catalog_content_node.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


