from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPaymentMtdsCfgsRl(Base):
    __tablename__ = 'oro_payment_mtds_cfgs_rl'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_payment_mtds_cfgs_rl_id_seq'::regclass)"))
    rule_id = Column(ForeignKey('oro_rule.id', ondelete='CASCADE'), nullable=False, index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    currency = Column(String(3), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    rule = relationship('OroRule')
    websites = relationship('OroWebsite', secondary='oro_payment_mtds_rule_website')


