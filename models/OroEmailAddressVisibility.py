from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailAddressVisibility(Base):
    __tablename__ = 'oro_email_address_visibility'

    email = Column(String(255), primary_key=True, nullable=False)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    is_visible = Column(Boolean, nullable=False)

    organization = relationship('OroOrganization')


