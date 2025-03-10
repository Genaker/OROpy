from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPaymentMethodConfig(Base):
    __tablename__ = 'oro_payment_method_config'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_payment_method_config_id_seq'::regclass)"))
    configs_rule_id = Column(ForeignKey('oro_payment_mtds_cfgs_rl.id', ondelete='CASCADE'), nullable=False, index=True)
    method = Column(String(255), nullable=False)
    options = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    serialized_data = Column(JSONB(astext_type=Text()))

    configs_rule = relationship('OroPaymentMtdsCfgsRl')


