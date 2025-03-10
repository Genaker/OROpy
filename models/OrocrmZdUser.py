from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmZdUser(Base):
    __tablename__ = 'orocrm_zd_user'
    __table_args__ = (
        Index('zd_user_oid_cid_unq', 'origin_id', 'channel_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_zd_user_id_seq'::regclass)"))
    channel_id = Column(ForeignKey('oro_integration_channel.id', ondelete='CASCADE'), index=True)
    related_contact_id = Column(ForeignKey('orocrm_contact.id', ondelete='SET NULL'), index=True)
    related_user_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    role_name = Column(ForeignKey('orocrm_zd_user_role.name', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    origin_id = Column(BigInteger)
    url = Column(String(255), server_default=text("NULL::character varying"))
    external_id = Column(String(50), server_default=text("NULL::character varying"))
    name = Column(String(255), server_default=text("NULL::character varying"))
    details = Column(Text)
    ticket_restrictions = Column(String(30), server_default=text("NULL::character varying"))
    only_private_comments = Column(Boolean, nullable=False, server_default=text("false"))
    notes = Column(Text)
    created_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    updated_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    origin_created_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    origin_updated_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    last_login_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    verified = Column(Boolean, nullable=False, server_default=text("false"))
    active = Column(Boolean, nullable=False, server_default=text("false"))
    alias = Column(String(100), server_default=text("NULL::character varying"))
    email = Column(String(255), server_default=text("NULL::character varying"))
    phone = Column(String(50), server_default=text("NULL::character varying"))
    time_zone = Column(String(30), server_default=text("NULL::character varying"))
    locale = Column(String(30), server_default=text("NULL::character varying"))

    channel = relationship('OroIntegrationChannel')
    related_contact = relationship('OrocrmContact')
    related_user = relationship('OroUser')
    orocrm_zd_user_role = relationship('OrocrmZdUserRole')


t_oro_attribute_family_label = Table(
    'oro_attribute_family_label', metadata,
    Column('attribute_family_id', ForeignKey('oro_attribute_family.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_attribute_group_label = Table(
    'oro_attribute_group_label', metadata,
    Column('attribute_group_id', ForeignKey('oro_attribute_group.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_brand_description = Table(
    'oro_brand_description', metadata,
    Column('brand_id', ForeignKey('oro_brand.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_brand_name = Table(
    'oro_brand_name', metadata,
    Column('brand_id', ForeignKey('oro_brand.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_brand_short_desc = Table(
    'oro_brand_short_desc', metadata,
    Column('brand_id', ForeignKey('oro_brand.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_brand_slug = Table(
    'oro_brand_slug', metadata,
    Column('brand_id', ForeignKey('oro_brand.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('slug_id', ForeignKey('oro_redirect_slug.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_brand_slug_prototype = Table(
    'oro_brand_slug_prototype', metadata,
    Column('brand_id', ForeignKey('oro_brand.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_catalog_cat_slug = Table(
    'oro_catalog_cat_slug', metadata,
    Column('category_id', ForeignKey('oro_catalog_category.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('slug_id', ForeignKey('oro_redirect_slug.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_catalog_cat_slug_prototype = Table(
    'oro_catalog_cat_slug_prototype', metadata,
    Column('category_id', ForeignKey('oro_catalog_category.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_cms_content_block_title = Table(
    'oro_cms_content_block_title', metadata,
    Column('content_block_id', ForeignKey('oro_cms_content_block.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_cms_content_widget_label = Table(
    'oro_cms_content_widget_label', metadata,
    Column('content_widget_id', ForeignKey('oro_cms_content_widget.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_cms_page_slug_prototype = Table(
    'oro_cms_page_slug_prototype', metadata,
    Column('page_id', ForeignKey('oro_cms_page.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_cms_page_title = Table(
    'oro_cms_page_title', metadata,
    Column('page_id', ForeignKey('oro_cms_page.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_cms_page_to_slug = Table(
    'oro_cms_page_to_slug', metadata,
    Column('page_id', ForeignKey('oro_cms_page.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('slug_id', ForeignKey('oro_redirect_slug.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


