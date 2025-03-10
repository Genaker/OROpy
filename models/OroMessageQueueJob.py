from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroMessageQueueJob(Base):
    __tablename__ = 'oro_message_queue_job'
    __table_args__ = (
        Index('oro_message_queue_job_inx', 'root_job_id', 'name', 'owner_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_message_queue_job_id_seq'::regclass)"))
    root_job_id = Column(ForeignKey('oro_message_queue_job.id', ondelete='CASCADE'), index=True)
    owner_id = Column(String(255), server_default=text("NULL::character varying"))
    name = Column(String(255), nullable=False)
    status = Column(String(255), nullable=False, index=True)
    interrupted = Column(Boolean, nullable=False)
    unique = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    started_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    last_active_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    stopped_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    data = Column(JSONB(astext_type=Text()), comment='(DC2Type:json_array)(DC2Type:json_array)')
    job_progress = Column(Float(53), comment='(DC2Type:percent)')

    root_job = relationship('OroMessageQueueJob', remote_side=[id])


t_oro_message_queue_job_unique = Table(
    'oro_message_queue_job_unique', metadata,
    Column('name', String(255), nullable=False, unique=True)
)


