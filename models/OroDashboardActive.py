from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroDashboardActive(Base):
    __tablename__ = 'oro_dashboard_active'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_dashboard_active_id_seq'::regclass)"))
    user_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    dashboard_id = Column(ForeignKey('oro_dashboard.id', ondelete='CASCADE'), index=True)

    dashboard = relationship('OroDashboard')
    organization = relationship('OroOrganization')
    user = relationship('OroUser')


