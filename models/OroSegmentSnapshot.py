from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroSegmentSnapshot(Base):
    __tablename__ = 'oro_segment_snapshot'
    __table_args__ = (
        Index('uniq_43b8bb67db296aad81257d5d', 'segment_id', 'entity_id', unique=True),
        Index('oro_segment_snapshot_segment_id_integer_entity_id_idx', 'segment_id', 'integer_entity_id', unique=True)
    )

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('oro_segment_snapshot_id_seq'::regclass)"))
    segment_id = Column(ForeignKey('oro_segment.id', ondelete='CASCADE'), nullable=False, index=True)
    integer_entity_id = Column(Integer, index=True)
    entity_id = Column(String(255), index=True, server_default=text("NULL::character varying"))
    createdat = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')

    segment = relationship('OroSegment')


