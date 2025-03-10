from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCplActivationRule(Base):
    __tablename__ = 'oro_cpl_activation_rule'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cpl_activation_rule_id_seq'::regclass)"))
    full_combined_price_list_id = Column(ForeignKey('oro_price_list_combined.id', ondelete='CASCADE'), index=True)
    combined_price_list_id = Column(ForeignKey('oro_price_list_combined.id', ondelete='CASCADE'), index=True)
    activate_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    expire_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    is_active = Column(Boolean, nullable=False)

    combined_price_list = relationship('OroPriceListCombined', primaryjoin='OroCplActivationRule.combined_price_list_id == OroPriceListCombined.id')
    full_combined_price_list = relationship('OroPriceListCombined', primaryjoin='OroCplActivationRule.full_combined_price_list_id == OroPriceListCombined.id')


