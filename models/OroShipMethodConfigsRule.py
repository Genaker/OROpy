from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroShipMethodConfigsRule(Base):
    __tablename__ = 'oro_ship_method_configs_rule'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_ship_method_configs_rule_id_seq'::regclass)"))
    rule_id = Column(ForeignKey('oro_rule.id', ondelete='CASCADE'), nullable=False, index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    currency = Column(String(3), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    rule = relationship('OroRule')
    websites = relationship('OroWebsite', secondary='oro_ship_mtds_rule_website')


