from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmCampaign(Base):
    __tablename__ = 'orocrm_campaign'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_campaign_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False)
    code = Column(String(255), nullable=False, unique=True)
    combined_name = Column(String(255), server_default=text("NULL::character varying"))
    start_date = Column(Date, comment='(DC2Type:date)')
    end_date = Column(Date, comment='(DC2Type:date)')
    description = Column(Text)
    budget = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    report_period = Column(String(25), nullable=False)
    report_refresh_date = Column(Date)
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    owner = relationship('OroUser')


