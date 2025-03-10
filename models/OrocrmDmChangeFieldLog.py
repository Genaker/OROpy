from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmDmChangeFieldLog(Base):
    __tablename__ = 'orocrm_dm_change_field_log'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_dm_change_field_log_id_seq'::regclass)"))
    channel_id = Column(Integer, nullable=False)
    parent_entity = Column(String(255), nullable=False)
    related_field_path = Column(Text, nullable=False)
    related_id = Column(Integer)


