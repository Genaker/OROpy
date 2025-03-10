from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTranslationKey(Base):
    __tablename__ = 'oro_translation_key'
    __table_args__ = (
        Index('oro_translation_key_uidx', 'domain', 'key', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_translation_key_id_seq'::regclass)"))
    key = Column(String(255), nullable=False)
    domain = Column(String(255), nullable=False, server_default=text("'messages'::character varying"))


