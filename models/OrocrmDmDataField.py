from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmDmDataField(Base):
    __tablename__ = 'orocrm_dm_data_field'
    __table_args__ = (
        Index('orocrm_dm_data_field_unq', 'name', 'channel_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_dm_data_field_id_seq'::regclass)"))
    owner_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    channel_id = Column(ForeignKey('oro_integration_channel.id', ondelete='CASCADE'), index=True)
    visibility_id = Column(ForeignKey('oro_enum_dm_df_visibility.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    type_id = Column(ForeignKey('oro_enum_dm_df_type.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    name = Column(String(255), nullable=False)
    default_value = Column(String(255), server_default=text("NULL::character varying"))
    notes = Column(Text)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    serialized_data = Column(JSONB(astext_type=Text()))

    channel = relationship('OroIntegrationChannel')
    owner = relationship('OroOrganization')
    type = relationship('OroEnumDmDfType')
    visibility = relationship('OroEnumDmDfVisibility')


