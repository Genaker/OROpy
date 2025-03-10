from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPaymentMtdsCfgsRlD(Base):
    __tablename__ = 'oro_payment_mtds_cfgs_rl_d'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_payment_mtds_cfgs_rl_d_id_seq'::regclass)"))
    region_code = Column(ForeignKey('oro_dictionary_region.combined_code'), index=True, server_default=text("NULL::character varying"))
    configs_rule_id = Column(ForeignKey('oro_payment_mtds_cfgs_rl.id', ondelete='CASCADE'), nullable=False, index=True)
    country_code = Column(ForeignKey('oro_dictionary_country.iso2_code'), nullable=False, index=True)
    region_text = Column(String(255), server_default=text("NULL::character varying"))

    configs_rule = relationship('OroPaymentMtdsCfgsRl')
    oro_dictionary_country = relationship('OroDictionaryCountry')
    oro_dictionary_region = relationship('OroDictionaryRegion')


