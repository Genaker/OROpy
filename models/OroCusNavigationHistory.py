from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCusNavigationHistory(Base):
    __tablename__ = 'oro_cus_navigation_history'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cus_navigation_history_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='CASCADE'), nullable=False, index=True)
    url = Column(String(8190), nullable=False)
    title = Column(Text, nullable=False)
    visited_at = Column(TIMESTAMP(precision=0), nullable=False)
    visit_count = Column(Integer, nullable=False)
    route = Column(String(128), nullable=False, index=True)
    route_parameters = Column(Text, nullable=False, comment='(DC2Type:array)(DC2Type:array)')
    entity_id = Column(Integer, index=True)

    customer_user = relationship('OroCustomerUser')
    organization = relationship('OroOrganization')


