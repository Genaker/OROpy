from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroWebsite(Base):
    __tablename__ = 'oro_website'
    __table_args__ = (
        Index('uidx_oro_website_name_organization', 'name', 'organization_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_website_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    business_unit_owner_id = Column(ForeignKey('oro_business_unit.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    is_default = Column(Boolean, nullable=False)
    guest_role_id = Column(ForeignKey('oro_customer_user_role.id', ondelete='RESTRICT'), index=True)
    default_role_id = Column(ForeignKey('oro_customer_user_role.id', ondelete='RESTRICT'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    business_unit_owner = relationship('OroBusinessUnit')
    default_role = relationship('OroCustomerUserRole', primaryjoin='OroWebsite.default_role_id == OroCustomerUserRole.id')
    guest_role = relationship('OroCustomerUserRole', primaryjoin='OroWebsite.guest_role_id == OroCustomerUserRole.id')
    organization = relationship('OroOrganization')
    websites = relationship(
        'OroWebsite',
        secondary='oro_related_website',
        primaryjoin='OroWebsite.id == oro_related_website.c.related_website_id',
        secondaryjoin='OroWebsite.id == oro_related_website.c.website_id'
    )


