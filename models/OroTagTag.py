from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTagTag(Base):
    __tablename__ = 'oro_tag_tag'
    __table_args__ = (
        Index('name_organization_idx', 'name', 'organization_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tag_tag_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    taxonomy_id = Column(ForeignKey('oro_tag_taxonomy.id', ondelete='SET NULL'), index=True)
    name = Column(String(50), nullable=False)
    created = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    taxonomy = relationship('OroTagTaxonomy')
    user_owner = relationship('OroUser')


