from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEntityConfigLogDiff(Base):
    __tablename__ = 'oro_entity_config_log_diff'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_entity_config_log_diff_id_seq'::regclass)"))
    log_id = Column(ForeignKey('oro_entity_config_log.id', ondelete='CASCADE'), index=True)
    class_name = Column(String(100), nullable=False)
    field_name = Column(String(100), server_default=text("NULL::character varying"))
    scope = Column(String(100), server_default=text("NULL::character varying"))
    diff = Column(Text, nullable=False)

    log = relationship('OroEntityConfigLog')


t_oro_fedex_transp_ship_service = Table(
    'oro_fedex_transp_ship_service', metadata,
    Column('transport_id', ForeignKey('oro_integration_transport.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('ship_service_id', ForeignKey('oro_fedex_shipping_service.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


