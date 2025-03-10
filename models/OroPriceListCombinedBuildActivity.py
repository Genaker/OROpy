from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPriceListCombinedBuildActivity(Base):
    __tablename__ = 'oro_price_list_combined_build_activity'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('oro_price_list_combined_build_activity_id_seq'::regclass)"))
    combined_price_list_id = Column(ForeignKey('oro_price_list_combined.id', ondelete='CASCADE'), nullable=False, index=True)
    parent_job_id = Column(Integer, index=True)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')

    combined_price_list = relationship('OroPriceListCombined')


t_oro_price_list_combined_gc = Table(
    'oro_price_list_combined_gc', metadata,
    Column('combined_price_list_id', ForeignKey('oro_price_list_combined.id', ondelete='CASCADE'), nullable=False, unique=True),
    Column('requested_at', TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
)


