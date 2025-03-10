from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroIntegrationChannelStatu(Base):
    __tablename__ = 'oro_integration_channel_status'
    __table_args__ = (
        Index('oro_intch_con_state_idx', 'connector', 'code'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_integration_channel_status_id_seq'::regclass)"))
    channel_id = Column(ForeignKey('oro_integration_channel.id', ondelete='CASCADE'), nullable=False, index=True)
    code = Column(String(255), nullable=False)
    connector = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    date = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    data = Column(JSON, comment='(DC2Type:json_array)(DC2Type:json_array)')

    channel = relationship('OroIntegrationChannel')


t_oro_notification_recip_group = Table(
    'oro_notification_recip_group', metadata,
    Column('recipient_list_id', ForeignKey('oro_notification_recip_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('group_id', ForeignKey('oro_access_group.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


