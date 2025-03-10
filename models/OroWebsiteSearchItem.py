from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWebsiteSearchItem(Base):
    __tablename__ = 'oro_website_search_item'
    __table_args__ = (
        Index('oro_website_search_item_uidx', 'entity', 'record_id', 'alias', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_website_search_item_id_seq'::regclass)"))
    entity = Column(String(255), nullable=False, index=True)
    alias = Column(String(255), nullable=False, index=True)
    record_id = Column(Integer)
    weight = Column(Numeric(8, 4), nullable=False, server_default=text("'1'::numeric"))
    changed = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')


