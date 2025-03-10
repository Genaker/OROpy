from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroNavigationItem(Base):
    __tablename__ = 'oro_navigation_item'
    __table_args__ = (
        Index('sorted_items_idx', 'user_id', 'position'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_navigation_item_id_seq'::regclass)"))
    user_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), nullable=False, index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    type = Column(String(10), nullable=False)
    url = Column(String(8190), nullable=False)
    title = Column(Text, nullable=False)
    position = Column(SmallInteger, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)

    organization = relationship('OroOrganization')
    user = relationship('OroUser')


