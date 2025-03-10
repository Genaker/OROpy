from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWebCatalog(Base):
    __tablename__ = 'oro_web_catalog'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_web_catalog_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    business_unit_owner_id = Column(ForeignKey('oro_business_unit.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    serialized_data = Column(JSONB(astext_type=Text()))

    business_unit_owner = relationship('OroBusinessUnit')
    organization = relationship('OroOrganization')


