from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPriceRuleLexeme(Base):
    __tablename__ = 'oro_price_rule_lexeme'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_price_rule_lexeme_id_seq'::regclass)"))
    price_rule_id = Column(ForeignKey('oro_price_rule.id', ondelete='CASCADE'), index=True)
    price_list_id = Column(ForeignKey('oro_price_list.id', ondelete='CASCADE'), nullable=False, index=True)
    class_name = Column(String(255), nullable=False)
    field_name = Column(String(255), nullable=False)
    relation_id = Column(Integer)

    price_list = relationship('OroPriceList')
    price_rule = relationship('OroPriceRule')


