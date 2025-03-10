from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroSearchQuery(Base):
    __tablename__ = 'oro_search_query'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_search_query_id_seq'::regclass)"))
    entity = Column(String(250), nullable=False)
    query = Column(Text, nullable=False)
    result_count = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')


