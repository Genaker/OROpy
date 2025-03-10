from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmSalesLead(Base):
    __tablename__ = 'orocrm_sales_lead'
    __table_args__ = (
        Index('lead_created_idx', 'createdat', 'id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_sales_lead_id_seq'::regclass)"))
    contact_id = Column(ForeignKey('orocrm_contact.id', ondelete='SET NULL'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    customer_association_id = Column(ForeignKey('orocrm_sales_customer.id', ondelete='CASCADE'), index=True)
    source_id = Column(ForeignKey('oro_enum_lead_source.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    campaign_id = Column(ForeignKey('orocrm_campaign.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    status_id = Column(ForeignKey('oro_enum_lead_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    name = Column(String(255), nullable=False)
    name_prefix = Column(String(255), server_default=text("NULL::character varying"))
    first_name = Column(String(255), server_default=text("NULL::character varying"))
    middle_name = Column(String(255), server_default=text("NULL::character varying"))
    last_name = Column(String(255), server_default=text("NULL::character varying"))
    name_suffix = Column(String(255), server_default=text("NULL::character varying"))
    job_title = Column(String(255), server_default=text("NULL::character varying"))
    company_name = Column(String(255), server_default=text("NULL::character varying"))
    website = Column(String(255), server_default=text("NULL::character varying"))
    number_of_employees = Column(Integer)
    industry = Column(String(255), server_default=text("NULL::character varying"))
    createdat = Column(TIMESTAMP(precision=0), nullable=False)
    updatedat = Column(TIMESTAMP(precision=0), index=True, server_default=text("NULL::timestamp without time zone"))
    notes = Column(Text)
    twitter = Column(String(255), server_default=text("NULL::character varying"))
    linkedin = Column(String(255), server_default=text("NULL::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))
    ac_last_contact_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_in = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_out = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_contact_count = Column(Integer)
    ac_contact_count_in = Column(Integer)
    ac_contact_count_out = Column(Integer)

    campaign = relationship('OrocrmCampaign')
    contact = relationship('OrocrmContact')
    customer_association = relationship('OrocrmSalesCustomer')
    organization = relationship('OroOrganization')
    source = relationship('OroEnumLeadSource')
    status = relationship('OroEnumLeadStatu')
    user_owner = relationship('OroUser')
    notes1 = relationship('OroNote', secondary='oro_rel_6f8f552a88a3cef53c57d4')
    tasks = relationship('OrocrmTask', secondary='oro_rel_f24c741b88a3cef53c57d4')


