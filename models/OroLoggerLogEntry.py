from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroLoggerLogEntry(Base):
    __tablename__ = 'oro_logger_log_entry'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_logger_log_entry_id_seq'::regclass)"))
    message = Column(Text, nullable=False)
    context = Column(JSON, nullable=False, comment='(DC2Type:json_array)(DC2Type:json_array)')
    level = Column(SmallInteger, nullable=False)
    channel = Column(String(255), nullable=False)
    datetime = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    extra = Column(JSON, nullable=False, comment='(DC2Type:json_array)(DC2Type:json_array)')


