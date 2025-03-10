from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroProductKitItemProduct(Base):
    __tablename__ = 'oro_product_kit_item_product'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_product_kit_item_product_id_seq'::regclass)"))
    product_kit_item_id = Column(ForeignKey('oro_product_kit_item.id', ondelete='CASCADE'), nullable=False, index=True)
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)
    product_unit_precision_id = Column(ForeignKey('oro_product_unit_precision.id', ondelete='SET NULL'), index=True)
    sort_order = Column(Integer, nullable=False, server_default=text("0"))
    serialized_data = Column(JSONB(astext_type=Text()))

    product = relationship('OroProduct')
    product_kit_item = relationship('OroProductKitItem')
    product_unit_precision = relationship('OroProductUnitPrecision')


t_oro_rel_2653537083dfdfa436b4e2 = Table(
    'oro_rel_2653537083dfdfa436b4e2', metadata,
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('contact_id', ForeignKey('orocrm_contact.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_26535370f24c741be77458 = Table(
    'oro_rel_26535370f24c741be77458', metadata,
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('task_id', ForeignKey('orocrm_task.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_46a29d1983dfdfa436b4e2 = Table(
    'oro_rel_46a29d1983dfdfa436b4e2', metadata,
    Column('calendarevent_id', ForeignKey('oro_calendar_event.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('contact_id', ForeignKey('orocrm_contact.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6cbc80002da17977bb66fd = Table(
    'oro_rel_6cbc80002da17977bb66fd', metadata,
    Column('call_id', ForeignKey('orocrm_call.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('user_id', ForeignKey('oro_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6cbc800083dfdfa436b4e2 = Table(
    'oro_rel_6cbc800083dfdfa436b4e2', metadata,
    Column('call_id', ForeignKey('orocrm_call.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('contact_id', ForeignKey('orocrm_contact.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552a1cf73d3129e5bb = Table(
    'oro_rel_6f8f552a1cf73d3129e5bb', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('product_id', ForeignKey('oro_product.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552a2c175de41f8af0 = Table(
    'oro_rel_6f8f552a2c175de41f8af0', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('shippingmethodsconfigsrule_id', ForeignKey('oro_ship_method_configs_rule.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552a7e0cc7f027a8f9 = Table(
    'oro_rel_6f8f552a7e0cc7f027a8f9', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('pricelist_id', ForeignKey('oro_price_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552a83dfdfa436b4e2 = Table(
    'oro_rel_6f8f552a83dfdfa436b4e2', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('contact_id', ForeignKey('orocrm_contact.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552aa73c785c4e6d3f = Table(
    'oro_rel_6f8f552aa73c785c4e6d3f', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('paymentmethodsconfigsrule_id', ForeignKey('oro_payment_mtds_cfgs_rl.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552af9a91faa3967ca = Table(
    'oro_rel_6f8f552af9a91faa3967ca', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('paymentterm_id', ForeignKey('oro_payment_term.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba61cf73d31624686 = Table(
    'oro_rel_c3990ba61cf73d31624686', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('product_id', ForeignKey('oro_product.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba62653537081b7e1 = Table(
    'oro_rel_c3990ba62653537081b7e1', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba62c175de4fa9927 = Table(
    'oro_rel_c3990ba62c175de4fa9927', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('shippingmethodsconfigsrule_id', ForeignKey('oro_ship_method_configs_rule.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba62da17977270bd6 = Table(
    'oro_rel_c3990ba62da17977270bd6', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('user_id', ForeignKey('oro_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba67e0cc7f01d1498 = Table(
    'oro_rel_c3990ba67e0cc7f01d1498', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('pricelist_id', ForeignKey('oro_price_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba683dfdfa4a13cb3 = Table(
    'oro_rel_c3990ba683dfdfa4a13cb3', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('contact_id', ForeignKey('orocrm_contact.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba6a73c785ca4a8ba = Table(
    'oro_rel_c3990ba6a73c785ca4a8ba', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('paymentmethodsconfigsrule_id', ForeignKey('oro_payment_mtds_cfgs_rl.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba6f24c741b1d920a = Table(
    'oro_rel_c3990ba6f24c741b1d920a', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('task_id', ForeignKey('orocrm_task.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba6f9a91faa5f648d = Table(
    'oro_rel_c3990ba6f9a91faa5f648d', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('paymentterm_id', ForeignKey('oro_payment_term.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_f24c741b265353702dde5c = Table(
    'oro_rel_f24c741b265353702dde5c', metadata,
    Column('task_id', ForeignKey('orocrm_task.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_f24c741b83dfdfa436b4e2 = Table(
    'oro_rel_f24c741b83dfdfa436b4e2', metadata,
    Column('task_id', ForeignKey('orocrm_task.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('contact_id', ForeignKey('orocrm_contact.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


