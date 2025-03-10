from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroConsentAcceptance(Base):
    __tablename__ = 'oro_consent_acceptance'
    __table_args__ = (
        Index('oro_customeru_consent_uidx', 'consent_id', 'customeruser_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_consent_acceptance_id_seq'::regclass)"))
    consent_id = Column(ForeignKey('oro_consent.id', ondelete='RESTRICT'), nullable=False, index=True)
    landing_page_id = Column(ForeignKey('oro_cms_page.id', ondelete='RESTRICT'), index=True)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    customeruser_id = Column(ForeignKey('oro_customer_user.id', ondelete='CASCADE'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    consent = relationship('OroConsent')
    customeruser = relationship('OroCustomerUser')
    landing_page = relationship('OroCmsPage')


