from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmDmAbCntExport(Base):
    __tablename__ = 'orocrm_dm_ab_cnt_export'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_dm_ab_cnt_export_id_seq'::regclass)"))
    address_book_id = Column(ForeignKey('orocrm_dm_address_book.id', ondelete='SET NULL'), index=True)
    channel_id = Column(ForeignKey('oro_integration_channel.id', ondelete='SET NULL'), index=True)
    status_id = Column(ForeignKey('oro_enum_dm_import_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    import_id = Column(String(100), nullable=False, unique=True)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    faults_processed = Column(Boolean, nullable=False, index=True)
    sync_attempts = Column(SmallInteger)
    serialized_data = Column(JSONB(astext_type=Text()))

    address_book = relationship('OrocrmDmAddressBook')
    channel = relationship('OroIntegrationChannel')
    status = relationship('OroEnumDmImportStatu')


