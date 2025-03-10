from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCustomerUserSetting(Base):
    __tablename__ = 'oro_customer_user_settings'
    __table_args__ = (
        Index('unique_cus_user_website', 'customer_user_id', 'website_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_customer_user_settings_id_seq'::regclass)"))
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='CASCADE'), nullable=False, index=True)
    website_id = Column(ForeignKey('oro_website.id', ondelete='CASCADE'), nullable=False, index=True)
    localization_id = Column(ForeignKey('oro_localization.id', ondelete='SET NULL'), index=True)
    currency = Column(String(3), server_default=text("NULL::character varying"))
    product_filters_sidebar_expanded = Column(Boolean)
    serialized_data = Column(JSONB(astext_type=Text()))

    customer_user = relationship('OroCustomerUser')
    localization = relationship('OroLocalization')
    website = relationship('OroWebsite')


