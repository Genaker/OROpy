from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailAddres(Base):
    __tablename__ = 'oro_email_address'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_address_id_seq'::regclass)"))
    owner_mailbox_id = Column(ForeignKey('oro_email_mailbox.id'), index=True)
    created = Column(TIMESTAMP(precision=0), nullable=False)
    updated = Column(TIMESTAMP(precision=0), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    has_owner = Column(Boolean, nullable=False)
    owner_user_id = Column(ForeignKey('oro_user.id'), index=True)
    owner_contact_id = Column(ForeignKey('orocrm_contact.id'), index=True)
    owner_customeruser_id = Column(ForeignKey('oro_customer_user.id'), index=True)
    owner_request_id = Column(ForeignKey('oro_rfp_request.id'), index=True)
    owner_lead_id = Column(ForeignKey('orocrm_sales_lead.id'), index=True)

    owner_contact = relationship('OrocrmContact')
    owner_customeruser = relationship('OroCustomerUser')
    owner_lead = relationship('OrocrmSalesLead')
    owner_mailbox = relationship('OroEmailMailbox')
    owner_request = relationship('OroRfpRequest')
    owner_user = relationship('OroUser')


