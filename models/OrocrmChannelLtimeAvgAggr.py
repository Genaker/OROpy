from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmChannelLtimeAvgAggr(Base):
    __tablename__ = 'orocrm_channel_ltime_avg_aggr'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_channel_ltime_avg_aggr_id_seq'::regclass)"))
    data_channel_id = Column(ForeignKey('orocrm_channel.id', ondelete='CASCADE'), index=True)
    amount = Column(Numeric(19, 4), nullable=False, comment='(DC2Type:money)(DC2Type:money)')
    aggregation_date = Column(TIMESTAMP(precision=0), nullable=False)
    month = Column(SmallInteger, nullable=False)
    quarter = Column(SmallInteger, nullable=False)
    year = Column(SmallInteger, nullable=False)

    data_channel = relationship('OrocrmChannel')


t_orocrm_contactus_contact_rsn_t = Table(
    'orocrm_contactus_contact_rsn_t', metadata,
    Column('contact_reason_id', ForeignKey('orocrm_contactus_contact_rsn.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


