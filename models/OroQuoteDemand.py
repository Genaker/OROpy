from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroQuoteDemand(Base):
    __tablename__ = 'oro_quote_demand'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_quote_demand_id_seq'::regclass)"))
    customer_id = Column(ForeignKey('oro_customer.id', ondelete='SET NULL'), index=True)
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='SET NULL'), index=True)
    visitor_id = Column(ForeignKey('oro_customer_visitor.id', ondelete='SET NULL'), index=True)
    quote_id = Column(ForeignKey('oro_sale_quote.id', ondelete='CASCADE'), index=True)
    subtotal = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    total = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    total_currency = Column(String(3), server_default=text("NULL::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    customer = relationship('OroCustomer')
    customer_user = relationship('OroCustomerUser')
    quote = relationship('OroSaleQuote')
    visitor = relationship('OroCustomerVisitor')


t_oro_rel_2653537034e8bc9c2ddbe0 = Table(
    'oro_rel_2653537034e8bc9c2ddbe0', metadata,
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('order_id', ForeignKey('oro_order.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_26535370aab0e4f0b5ec88 = Table(
    'oro_rel_26535370aab0e4f0b5ec88', metadata,
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('quote_id', ForeignKey('oro_sale_quote.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_46a29d1934e8bc9c2ddbe0 = Table(
    'oro_rel_46a29d1934e8bc9c2ddbe0', metadata,
    Column('calendarevent_id', ForeignKey('oro_calendar_event.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('order_id', ForeignKey('oro_order.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_46a29d19aab0e4f0b5ec88 = Table(
    'oro_rel_46a29d19aab0e4f0b5ec88', metadata,
    Column('calendarevent_id', ForeignKey('oro_calendar_event.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('quote_id', ForeignKey('oro_sale_quote.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552a34e8bc9c2ddbe0 = Table(
    'oro_rel_6f8f552a34e8bc9c2ddbe0', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('order_id', ForeignKey('oro_order.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552aaab0e4f0b5ec88 = Table(
    'oro_rel_6f8f552aaab0e4f0b5ec88', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('quote_id', ForeignKey('oro_sale_quote.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba634e8bc9cac53cb = Table(
    'oro_rel_c3990ba634e8bc9cac53cb', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('order_id', ForeignKey('oro_order.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba6aab0e4f07348a4 = Table(
    'oro_rel_c3990ba6aab0e4f07348a4', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('quote_id', ForeignKey('oro_sale_quote.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


