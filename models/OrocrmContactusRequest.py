from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmContactusRequest(Base):
    __tablename__ = 'orocrm_contactus_request'
    __table_args__ = (
        Index('request_create_idx', 'created_at', 'id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_contactus_request_id_seq'::regclass)"))
    contact_reason_id = Column(ForeignKey('orocrm_contactus_contact_rsn.id'), index=True)
    lead_id = Column(ForeignKey('orocrm_sales_lead.id', ondelete='SET NULL'), index=True)
    opportunity_id = Column(ForeignKey('orocrm_sales_opportunity.id', ondelete='SET NULL'), index=True)
    owner_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    customer_name = Column(String(255), server_default=text("NULL::character varying"))
    preferred_contact_method = Column(String(100), nullable=False)
    feedback = Column(Text)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email_address = Column(String(100), server_default=text("NULL::character varying"))
    phone = Column(String(100), server_default=text("NULL::character varying"))
    comment = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='SET NULL'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))
    ac_last_contact_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_in = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_out = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_contact_count = Column(Integer)
    ac_contact_count_in = Column(Integer)
    ac_contact_count_out = Column(Integer)

    contact_reason = relationship('OrocrmContactusContactRsn')
    customer_user = relationship('OroCustomerUser')
    lead = relationship('OrocrmSalesLead')
    opportunity = relationship('OrocrmSalesOpportunity')
    owner = relationship('OroOrganization')
    emails = relationship('OroEmail', secondary='oro_rel_2653537050ef1ed9f45d78')


