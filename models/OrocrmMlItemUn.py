from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmMlItemUn(Base):
    __tablename__ = 'orocrm_ml_item_uns'
    __table_args__ = (
        Index('orocrm_ml_list_ent_uns_unq', 'entity_id', 'marketing_list_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_ml_item_uns_id_seq'::regclass)"))
    marketing_list_id = Column(ForeignKey('orocrm_marketing_list.id', ondelete='CASCADE'), nullable=False, index=True)
    entity_id = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')

    marketing_list = relationship('OrocrmMarketingList')


