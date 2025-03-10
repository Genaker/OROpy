from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWebsiteSearchSuggestion(Base):
    __tablename__ = 'oro_website_search_suggestion'
    __table_args__ = (
        Index('suggestion_unique', 'phrase', 'localization_id', 'organization_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_website_search_suggestion_id_seq'::regclass)"))
    localization_id = Column(ForeignKey('oro_localization.id', ondelete='CASCADE'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='CASCADE'), nullable=False, index=True)
    phrase = Column(String(255), nullable=False)
    words_count = Column(SmallInteger, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    serialized_data = Column(JSONB(astext_type=Text()))

    localization = relationship('OroLocalization')
    organization = relationship('OroOrganization')


t_orocrm_account_to_contact = Table(
    'orocrm_account_to_contact', metadata,
    Column('account_id', ForeignKey('orocrm_account.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('contact_id', ForeignKey('orocrm_contact.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


