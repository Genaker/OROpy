from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWebsiteSearchTermReport(Base):
    __tablename__ = 'oro_website_search_term_report'
    __table_args__ = (
        UniqueConstraint('search_date', 'normalized_search_term_hash'),
    )

    id = Column(UUID, primary_key=True)
    business_unit_owner_id = Column(ForeignKey('oro_business_unit.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    normalized_search_term_hash = Column(String(32), nullable=False)
    search_term = Column(String(255), nullable=False)
    times_searched = Column(Integer, nullable=False)
    times_returned_results = Column(Integer, nullable=False)
    times_empty = Column(Integer, nullable=False)
    search_date = Column(Date, nullable=False, index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    business_unit_owner = relationship('OroBusinessUnit')
    organization = relationship('OroOrganization')


