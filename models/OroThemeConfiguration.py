from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroThemeConfiguration(Base):
    __tablename__ = 'oro_theme_configuration'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_theme_configuration_id_seq'::regclass)"))
    business_unit_owner_id = Column(ForeignKey('oro_business_unit.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    type = Column(String(255), nullable=False, server_default=text("'Storefront'::character varying"))
    name = Column(String(255), nullable=False)
    description = Column(Text)
    theme = Column(String(255), nullable=False)
    configuration = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')

    business_unit_owner = relationship('OroBusinessUnit')
    organization = relationship('OroOrganization')


