from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCusProductVisibility(Base):
    __tablename__ = 'oro_cus_product_visibility'
    __table_args__ = (
        Index('oro_cus_prod_vis_uidx', 'product_id', 'scope_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cus_product_visibility_id_seq'::regclass)"))
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), index=True)
    scope_id = Column(ForeignKey('oro_scope.id', ondelete='CASCADE'), nullable=False, index=True)
    visibility = Column(String(255), server_default=text("NULL::character varying"))

    product = relationship('OroProduct')
    scope = relationship('OroScope')


t_oro_cus_user_access_role = Table(
    'oro_cus_user_access_role', metadata,
    Column('customer_user_id', ForeignKey('oro_customer_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('customer_user_role_id', ForeignKey('oro_customer_user_role.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


