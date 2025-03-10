from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroActivityOwner(Base):
    __tablename__ = 'oro_activity_owner'
    __table_args__ = (
        Index('unq_activity_owner', 'activity_id', 'user_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_activity_owner_id_seq'::regclass)"))
    activity_id = Column(ForeignKey('oro_activity_list.id', ondelete='CASCADE'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id'), index=True)
    user_id = Column(ForeignKey('oro_user.id'), index=True)

    activity = relationship('OroActivityList')
    organization = relationship('OroOrganization')
    user = relationship('OroUser')


