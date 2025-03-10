from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTrackingWebsite(Base):
    __tablename__ = 'oro_tracking_website'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tracking_website_id_seq'::regclass)"))
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False)
    identifier = Column(String(255), nullable=False, unique=True)
    url = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    extend_description = Column(Text)
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    user_owner = relationship('OroUser')


