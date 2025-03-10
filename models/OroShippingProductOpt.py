from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroShippingProductOpt(Base):
    __tablename__ = 'oro_shipping_product_opts'
    __table_args__ = (
        Index('oro_shipping_product_opts_uidx', 'product_id', 'product_unit_code', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_shipping_product_opts_id_seq'::regclass)"))
    freight_class_code = Column(ForeignKey('oro_shipping_freight_class.code'), index=True, server_default=text("NULL::character varying"))
    product_id = Column(ForeignKey('oro_product.id', ondelete='CASCADE'), nullable=False, index=True)
    product_unit_code = Column(ForeignKey('oro_product_unit.code', ondelete='CASCADE'), nullable=False, index=True)
    dimensions_unit_code = Column(ForeignKey('oro_shipping_length_unit.code'), index=True, server_default=text("NULL::character varying"))
    weight_unit_code = Column(ForeignKey('oro_shipping_weight_unit.code'), index=True, server_default=text("NULL::character varying"))
    weight_value = Column(Float(53))
    dimensions_length = Column(Float(53))
    dimensions_width = Column(Float(53))
    dimensions_height = Column(Float(53))

    oro_shipping_length_unit = relationship('OroShippingLengthUnit')
    oro_shipping_freight_clas = relationship('OroShippingFreightClas')
    product = relationship('OroProduct')
    oro_product_unit = relationship('OroProductUnit')
    oro_shipping_weight_unit = relationship('OroShippingWeightUnit')


