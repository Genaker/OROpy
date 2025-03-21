from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroAddressTypeTranslation(Base):
    __tablename__ = 'oro_address_type_translation'
    __table_args__ = (
        Index('address_type_translation_idx', 'locale', 'object_class', 'field', 'foreign_key'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_address_type_translation_id_seq'::regclass)"))
    foreign_key = Column(String(16), nullable=False)
    content = Column(String(255), nullable=False)
    locale = Column(String(16), nullable=False)
    object_class = Column(String(191), nullable=False)
    field = Column(String(32), nullable=False)


