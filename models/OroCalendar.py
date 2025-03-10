from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCalendar(Base):
    __tablename__ = 'oro_calendar'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_calendar_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), server_default=text("NULL::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    user_owner = relationship('OroUser')


