from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCronSchedule(Base):
    __tablename__ = 'oro_cron_schedule'
    __table_args__ = (
        Index('uq_command', 'command', 'args_hash', 'definition', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cron_schedule_id_seq'::regclass)"))
    command = Column(String(255), nullable=False)
    args = Column(JSON, nullable=False, comment='(DC2Type:json_array)(DC2Type:json_array)')
    args_hash = Column(String(32), nullable=False)
    definition = Column(String(100), server_default=text("NULL::character varying"))


