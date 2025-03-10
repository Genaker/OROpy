from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPromotionDiscountConfig(Base):
    __tablename__ = 'oro_promotion_discount_config'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_promotion_discount_config_id_seq'::regclass)"))
    type = Column(String(50), nullable=False, index=True)
    options = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    serialized_data = Column(JSONB(astext_type=Text()))


