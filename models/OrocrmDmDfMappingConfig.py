from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmDmDfMappingConfig(Base):
    __tablename__ = 'orocrm_dm_df_mapping_config'
    __table_args__ = (
        Index('orocrm_dm_df_mapping_config_unq', 'datafield_id', 'mapping_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_dm_df_mapping_config_id_seq'::regclass)"))
    mapping_id = Column(ForeignKey('orocrm_dm_df_mapping.id', ondelete='CASCADE'), index=True)
    datafield_id = Column(ForeignKey('orocrm_dm_data_field.id', ondelete='CASCADE'), index=True)
    entity_field = Column(Text, nullable=False)
    is_two_way_sync = Column(Boolean)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')

    datafield = relationship('OrocrmDmDataField')
    mapping = relationship('OrocrmDmDfMapping')


