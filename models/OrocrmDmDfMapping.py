from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmDmDfMapping(Base):
    __tablename__ = 'orocrm_dm_df_mapping'
    __table_args__ = (
        Index('orocrm_dm_data_field_mapping_unq', 'entity', 'channel_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_dm_df_mapping_id_seq'::regclass)"))
    owner_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    channel_id = Column(ForeignKey('oro_integration_channel.id', ondelete='CASCADE'), index=True)
    entity = Column(String(255), nullable=False)
    sync_priority = Column(Integer)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    serialized_data = Column(JSONB(astext_type=Text()))

    channel = relationship('OroIntegrationChannel')
    owner = relationship('OroOrganization')


