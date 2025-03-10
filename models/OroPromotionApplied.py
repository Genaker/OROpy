from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPromotionApplied(Base):
    __tablename__ = 'oro_promotion_applied'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_promotion_applied_id_seq'::regclass)"))
    order_id = Column(ForeignKey('oro_order.id', ondelete='CASCADE'), index=True)
    source_promotion_id = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False, server_default=text("true"))
    type = Column(String(255), nullable=False)
    promotion_name = Column(Text, nullable=False)
    config_options = Column(JSON, nullable=False, comment='(DC2Type:json_array)(DC2Type:json_array)')
    promotion_data = Column(JSON, nullable=False, comment='(DC2Type:json_array)(DC2Type:json_array)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    order = relationship('OroOrder')


t_oro_quote_assigned_cus_users = Table(
    'oro_quote_assigned_cus_users', metadata,
    Column('quote_id', ForeignKey('oro_sale_quote.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('customer_user_id', ForeignKey('oro_customer_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_quote_assigned_users = Table(
    'oro_quote_assigned_users', metadata,
    Column('quote_id', ForeignKey('oro_sale_quote.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('user_id', ForeignKey('oro_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


