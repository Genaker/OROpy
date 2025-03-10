from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroShippingRuleDestination(Base):
    __tablename__ = 'oro_shipping_rule_destination'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_shipping_rule_destination_id_seq'::regclass)"))
    rule_id = Column(ForeignKey('oro_ship_method_configs_rule.id', ondelete='CASCADE'), nullable=False, index=True)
    region_code = Column(ForeignKey('oro_dictionary_region.combined_code'), index=True, server_default=text("NULL::character varying"))
    country_code = Column(ForeignKey('oro_dictionary_country.iso2_code'), nullable=False, index=True)
    region_text = Column(String(255), server_default=text("NULL::character varying"))

    oro_dictionary_country = relationship('OroDictionaryCountry')
    oro_dictionary_region = relationship('OroDictionaryRegion')
    rule = relationship('OroShipMethodConfigsRule')


