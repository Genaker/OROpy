from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTagTagging(Base):
    __tablename__ = 'oro_tag_tagging'
    __table_args__ = (
        Index('tagging_idx', 'tag_id', 'entity_name', 'record_id', 'user_owner_id', unique=True),
        Index('entity_name_idx', 'entity_name', 'record_id')
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tag_tagging_id_seq'::regclass)"))
    tag_id = Column(ForeignKey('oro_tag_tag.id', ondelete='CASCADE'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    created = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    entity_name = Column(String(100), nullable=False)
    record_id = Column(Integer, nullable=False)

    tag = relationship('OroTagTag')
    user_owner = relationship('OroUser')


