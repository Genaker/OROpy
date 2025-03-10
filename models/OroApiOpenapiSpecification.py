from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroApiOpenapiSpecification(Base):
    __tablename__ = 'oro_api_openapi_specification'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_api_openapi_specification_id_seq'::regclass)"))
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    status = Column(String(8), nullable=False)
    published = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    name = Column(String(255), nullable=False)
    public_slug = Column(String(100), server_default=text("NULL::character varying"))
    view = Column(String(100), nullable=False)
    format = Column(String(20), nullable=False)
    entities = Column(Text, comment='(DC2Type:simple_array)(DC2Type:simple_array)')
    server_urls = Column(Text, comment='(DC2Type:simple_array)(DC2Type:simple_array)')
    specification = Column(Text)
    specification_created_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))

    organization = relationship('OroOrganization')
    user_owner = relationship('OroUser')


