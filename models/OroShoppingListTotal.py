from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroShoppingListTotal(Base):
    __tablename__ = 'oro_shopping_list_total'
    __table_args__ = (
        Index('unique_shopping_list_currency_customer_user', 'shopping_list_id', 'currency', 'customer_user_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_shopping_list_total_id_seq'::regclass)"))
    shopping_list_id = Column(ForeignKey('oro_shopping_list.id', ondelete='CASCADE'), nullable=False, index=True)
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='CASCADE'), index=True)
    currency = Column(String(255), nullable=False)
    subtotal_value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    is_valid = Column(Boolean, nullable=False)

    customer_user = relationship('OroCustomerUser')
    shopping_list = relationship('OroShoppingList')


