from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPromotionCouponUsage(Base):
    __tablename__ = 'oro_promotion_coupon_usage'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_promotion_coupon_usage_id_seq'::regclass)"))
    promotion_id = Column(ForeignKey('oro_promotion.id', ondelete='CASCADE'), nullable=False, index=True)
    coupon_id = Column(ForeignKey('oro_promotion_coupon.id', ondelete='CASCADE'), nullable=False, index=True)
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='SET NULL'), index=True)

    coupon = relationship('OroPromotionCoupon')
    customer_user = relationship('OroCustomerUser')
    promotion = relationship('OroPromotion')


t_oro_promotion_scope = Table(
    'oro_promotion_scope', metadata,
    Column('promotion_id', ForeignKey('oro_promotion.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('scope_id', ForeignKey('oro_scope.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_redirect_scope = Table(
    'oro_redirect_scope', metadata,
    Column('redirect_id', ForeignKey('oro_redirect.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('scope_id', ForeignKey('oro_scope.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_265353703708e583c5ba51 = Table(
    'oro_rel_265353703708e583c5ba51', metadata,
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('customeruser_id', ForeignKey('oro_customer_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_265353705154c0033bfb48 = Table(
    'oro_rel_265353705154c0033bfb48', metadata,
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('opportunity_id', ForeignKey('orocrm_sales_opportunity.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_46a29d193708e583c5ba51 = Table(
    'oro_rel_46a29d193708e583c5ba51', metadata,
    Column('calendarevent_id', ForeignKey('oro_calendar_event.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('customeruser_id', ForeignKey('oro_customer_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_46a29d195154c0033bfb48 = Table(
    'oro_rel_46a29d195154c0033bfb48', metadata,
    Column('calendarevent_id', ForeignKey('oro_calendar_event.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('opportunity_id', ForeignKey('orocrm_sales_opportunity.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6cbc80005154c0033bfb48 = Table(
    'oro_rel_6cbc80005154c0033bfb48', metadata,
    Column('call_id', ForeignKey('orocrm_call.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('opportunity_id', ForeignKey('orocrm_sales_opportunity.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552a3708e583c5ba51 = Table(
    'oro_rel_6f8f552a3708e583c5ba51', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('customeruser_id', ForeignKey('oro_customer_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552a5154c0033bfb48 = Table(
    'oro_rel_6f8f552a5154c0033bfb48', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('opportunity_id', ForeignKey('orocrm_sales_opportunity.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba63708e583a2c61e = Table(
    'oro_rel_c3990ba63708e583a2c61e', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('customeruser_id', ForeignKey('oro_customer_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba65154c0069aa16e = Table(
    'oro_rel_c3990ba65154c0069aa16e', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('opportunity_id', ForeignKey('orocrm_sales_opportunity.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_f24c741b5154c0033bfb48 = Table(
    'oro_rel_f24c741b5154c0033bfb48', metadata,
    Column('task_id', ForeignKey('orocrm_task.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('opportunity_id', ForeignKey('orocrm_sales_opportunity.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


