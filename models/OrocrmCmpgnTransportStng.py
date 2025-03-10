from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmCmpgnTransportStng(Base):
    __tablename__ = 'orocrm_cmpgn_transport_stngs'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_cmpgn_transport_stngs_id_seq'::regclass)"))
    email_template_id = Column(ForeignKey('oro_email_template.id', ondelete='SET NULL'), index=True)
    type = Column(String(50), nullable=False)
    dotmailer_channel_id = Column(ForeignKey('oro_integration_channel.id', ondelete='SET NULL'), index=True)

    dotmailer_channel = relationship('OroIntegrationChannel')
    email_template = relationship('OroEmailTemplate')


