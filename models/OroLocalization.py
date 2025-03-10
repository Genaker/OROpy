from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroLocalization(Base):
    __tablename__ = 'oro_localization'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_localization_id_seq'::regclass)"))
    parent_id = Column(ForeignKey('oro_localization.id', ondelete='SET NULL'), index=True)
    language_id = Column(ForeignKey('oro_language.id', ondelete='RESTRICT'), nullable=False, index=True)
    name = Column(String(255), nullable=False, unique=True)
    formatting_code = Column(String(16), nullable=False)
    rtl_mode = Column(Boolean, nullable=False, server_default=text("false"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    language = relationship('OroLanguage')
    parent = relationship('OroLocalization', remote_side=[id])
    localized_values = relationship('OroFallbackLocalizationVal', secondary='oro_localization_title')


