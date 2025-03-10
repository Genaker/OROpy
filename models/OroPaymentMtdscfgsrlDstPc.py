from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPaymentMtdscfgsrlDstPc(Base):
    __tablename__ = 'oro_payment_mtdscfgsrl_dst_pc'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_payment_mtdscfgsrl_dst_pc_id_seq'::regclass)"))
    destination_id = Column(ForeignKey('oro_payment_mtds_cfgs_rl_d.id', ondelete='CASCADE'), nullable=False, index=True)
    name = Column(Text, nullable=False)

    destination = relationship('OroPaymentMtdsCfgsRlD')


