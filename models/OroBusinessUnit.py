from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroBusinessUnit(Base):
    __tablename__ = 'oro_business_unit'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_business_unit_id_seq'::regclass)"))
    business_unit_owner_id = Column(ForeignKey('oro_business_unit.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='CASCADE'), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    phone = Column(String(100), server_default=text("NULL::character varying"))
    website = Column(String(255), server_default=text("NULL::character varying"))
    email = Column(String(255), server_default=text("NULL::character varying"))
    fax = Column(String(255), server_default=text("NULL::character varying"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    extend_description = Column(Text)
    serialized_data = Column(JSONB(astext_type=Text()))

    business_unit_owner = relationship('OroBusinessUnit', remote_side=[id])
    organization = relationship('OroOrganization')
    users = relationship('OroUser', secondary='oro_user_business_unit')


