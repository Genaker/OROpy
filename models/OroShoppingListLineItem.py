from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroShoppingListLineItem(Base):
    __tablename__ = 'oro_shopping_list_line_item'
    __table_args__ = (
        Index('oro_shopping_list_line_item_uidx', 'product_id', 'shopping_list_id', 'unit_code', 'checksum', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_shopping_list_line_item_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='CASCADE'), index=True)
    shopping_list_id = Column(ForeignKey('oro_shopping_list.id', ondelete='CASCADE'), nullable=False, index=True)
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)
    parent_product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), index=True)
    unit_code = Column(ForeignKey('oro_product_unit.code', ondelete='CASCADE'), nullable=False, index=True)
    quantity = Column(Float(53), nullable=False)
    notes = Column(Text)
    checksum = Column(String(40), nullable=False, server_default=text("''::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    customer_user = relationship('OroCustomerUser')
    organization = relationship('OroOrganization')
    parent_product = relationship('OroProduct', primaryjoin='OroShoppingListLineItem.parent_product_id == OroProduct.id')
    product = relationship('OroProduct', primaryjoin='OroShoppingListLineItem.product_id == OroProduct.id')
    shopping_list = relationship('OroShoppingList')
    oro_product_unit = relationship('OroProductUnit')
    user_owner = relationship('OroUser')


