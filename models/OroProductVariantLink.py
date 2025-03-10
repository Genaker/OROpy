from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroProductVariantLink(Base):
    __tablename__ = 'oro_product_variant_link'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_product_variant_link_id_seq'::regclass)"))
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)
    parent_product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)
    visible = Column(Boolean, nullable=False, server_default=text("true"))

    parent_product = relationship('OroProduct', primaryjoin='OroProductVariantLink.parent_product_id == OroProduct.id')
    product = relationship('OroProduct', primaryjoin='OroProductVariantLink.product_id == OroProduct.id')


t_oro_rel_265353702da17977bb66fd = Table(
    'oro_rel_265353702da17977bb66fd', metadata,
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('user_id', ForeignKey('oro_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


