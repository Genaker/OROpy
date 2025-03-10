from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroSystemCalendar(Base):
    __tablename__ = 'oro_system_calendar'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_system_calendar_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False)
    background_color = Column(String(7), server_default=text("NULL::character varying"))
    is_public = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    extend_description = Column(Text)
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')


