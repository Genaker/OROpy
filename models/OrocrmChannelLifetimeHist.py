from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmChannelLifetimeHist(Base):
    __tablename__ = 'orocrm_channel_lifetime_hist'
    __table_args__ = (
        Index('orocrm_chl_ltv_hist_idx', 'account_id', 'data_channel_id', 'status'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_channel_lifetime_hist_id_seq'::regclass)"))
    data_channel_id = Column(ForeignKey('orocrm_channel.id', ondelete='CASCADE'), index=True)
    account_id = Column(ForeignKey('orocrm_account.id', ondelete='CASCADE'), index=True)
    status = Column(Boolean, nullable=False, index=True)
    amount = Column(Numeric(19, 4), nullable=False, comment='(DC2Type:money)(DC2Type:money)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False)

    account = relationship('OrocrmAccount')
    data_channel = relationship('OrocrmChannel')


