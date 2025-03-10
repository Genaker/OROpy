from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmMarketingList(Base):
    __tablename__ = 'orocrm_marketing_list'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_marketing_list_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    type = Column(ForeignKey('orocrm_marketing_list_type.name'), nullable=False, index=True)
    segment_id = Column(ForeignKey('oro_segment.id', ondelete='SET NULL'), index=True)
    owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    entity = Column(String(255), nullable=False)
    last_run = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    union_contacted_items = Column(Boolean, nullable=False, server_default=text("true"))
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    owner = relationship('OroUser')
    segment = relationship('OroSegment')
    orocrm_marketing_list_type = relationship('OrocrmMarketingListType')


