from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmSalesOpportunity(Base):
    __tablename__ = 'orocrm_sales_opportunity'
    __table_args__ = (
        Index('opportunity_created_idx', 'created_at', 'id'),
        Index('opportunities_by_status_idx', 'organization_id', 'status_id', 'close_revenue_value', 'budget_amount_value', 'created_at')
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_sales_opportunity_id_seq'::regclass)"))
    contact_id = Column(ForeignKey('orocrm_contact.id', ondelete='SET NULL'), index=True)
    close_reason_name = Column(ForeignKey('orocrm_sales_opport_close_rsn.name'), index=True, server_default=text("NULL::character varying"))
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    lead_id = Column(ForeignKey('orocrm_sales_lead.id', ondelete='SET NULL'), index=True)
    customer_association_id = Column(ForeignKey('orocrm_sales_customer.id', ondelete='CASCADE'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    status_id = Column(ForeignKey('oro_enum_opportunity_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    name = Column(String(255), nullable=False)
    close_date = Column(Date)
    probability = Column(Float(53), comment='(DC2Type:percent)(DC2Type:percent)')
    budget_amount_value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money_value)(DC2Type:money_value)')
    budget_amount_currency = Column(String(3), server_default=text("NULL::character varying"), comment='(DC2Type:currency)(DC2Type:currency)')
    base_budget_amount_value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    close_revenue_value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money_value)(DC2Type:money_value)')
    close_revenue_currency = Column(String(3), server_default=text("NULL::character varying"), comment='(DC2Type:currency)(DC2Type:currency)')
    base_close_revenue_value = Column(Numeric(19, 4), server_default=text("NULL::numeric"), comment='(DC2Type:money)(DC2Type:money)')
    customer_need = Column(Text)
    proposed_solution = Column(Text)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    notes = Column(Text)
    closed_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    serialized_data = Column(JSONB(astext_type=Text()))
    ac_last_contact_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_in = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_last_contact_date_out = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    ac_contact_count = Column(Integer)
    ac_contact_count_in = Column(Integer)
    ac_contact_count_out = Column(Integer)

    orocrm_sales_opport_close_rsn = relationship('OrocrmSalesOpportCloseRsn')
    contact = relationship('OrocrmContact')
    customer_association = relationship('OrocrmSalesCustomer')
    lead = relationship('OrocrmSalesLead')
    organization = relationship('OroOrganization')
    status = relationship('OroEnumOpportunityStatu')
    user_owner = relationship('OroUser')
    tasks = relationship('OrocrmTask', secondary='oro_rel_f24c741b5154c0033bfb48')


