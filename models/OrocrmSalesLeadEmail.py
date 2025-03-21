from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmSalesLeadEmail(Base):
    __tablename__ = 'orocrm_sales_lead_email'
    __table_args__ = (
        Index('lead_primary_email_idx', 'email', 'is_primary'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_sales_lead_email_id_seq'::regclass)"))
    owner_id = Column(ForeignKey('orocrm_sales_lead.id', ondelete='CASCADE'), index=True)
    email = Column(String(255), nullable=False)
    is_primary = Column(Boolean)
    serialized_data = Column(JSONB(astext_type=Text()))

    owner = relationship('OrocrmSalesLead')


