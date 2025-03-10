from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroLanguage(Base):
    __tablename__ = 'oro_language'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_language_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    code = Column(String(16), nullable=False, unique=True)
    enabled = Column(Boolean, nullable=False, server_default=text("false"))
    installed_build_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    local_files_language = Column(Boolean, nullable=False, server_default=text("false"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)

    organization = relationship('OroOrganization')


