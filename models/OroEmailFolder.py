from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailFolder(Base):
    __tablename__ = 'oro_email_folder'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_folder_id_seq'::regclass)"))
    origin_id = Column(ForeignKey('oro_email_origin.id', ondelete='CASCADE'), index=True)
    parent_folder_id = Column(ForeignKey('oro_email_folder.id', ondelete='CASCADE'), index=True)
    name = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    type = Column(String(10), nullable=False)
    synchronized = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    outdated_at = Column(TIMESTAMP(precision=0), index=True, server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    sync_enabled = Column(Boolean, nullable=False, server_default=text("false"))
    sync_start_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    failed_count = Column(Integer, nullable=False, server_default=text("0"))

    origin = relationship('OroEmailOrigin')
    parent_folder = relationship('OroEmailFolder', remote_side=[id])


