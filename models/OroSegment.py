from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroSegment(Base):
    __tablename__ = 'oro_segment'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_segment_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    type = Column(ForeignKey('oro_segment_type.name'), nullable=False, index=True)
    business_unit_owner_id = Column(ForeignKey('oro_business_unit.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False)
    name_lowercase = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    entity = Column(String(255), nullable=False)
    definition = Column(Text, nullable=False)
    createdat = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updatedat = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    last_run = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    records_limit = Column(Integer)
    serialized_data = Column(JSONB(astext_type=Text()))

    business_unit_owner = relationship('OroBusinessUnit')
    organization = relationship('OroOrganization')
    oro_segment_type = relationship('OroSegmentType')


