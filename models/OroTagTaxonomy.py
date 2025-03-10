from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTagTaxonomy(Base):
    __tablename__ = 'oro_tag_taxonomy'
    __table_args__ = (
        Index('tag_taxonomy_name_organization_idx', 'name', 'organization_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tag_taxonomy_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    name = Column(String(50), nullable=False)
    background_color = Column(String(7), server_default=text("NULL::character varying"))
    created = Column(TIMESTAMP(precision=0), nullable=False)
    updated = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    user_owner = relationship('OroUser')


