from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmail(Base):
    __tablename__ = 'oro_email'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_id_seq'::regclass)"))
    from_email_address_id = Column(ForeignKey('oro_email_address.id'), nullable=False, index=True)
    thread_id = Column(ForeignKey('oro_email_thread.id'), index=True)
    email_body_id = Column(ForeignKey('oro_email_body.id', ondelete='SET NULL'), unique=True)
    created = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    subject = Column(String(998), nullable=False)
    from_name = Column(String(320), nullable=False)
    sent = Column(TIMESTAMP(precision=0), nullable=False, index=True, comment='(DC2Type:datetime)')
    importance = Column(Integer, nullable=False)
    internaldate = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    message_id = Column(String(512), nullable=False, index=True)
    x_message_id = Column(String(255), server_default=text("NULL::character varying"))
    x_thread_id = Column(String(255), server_default=text("NULL::character varying"))
    is_head = Column(Boolean, nullable=False, index=True, server_default=text("true"))
    refs = Column(Text)
    multi_message_id = Column(Text)
    acceptlanguageheader = Column(Text)
    body_synced = Column(Boolean, server_default=text("false"))
    serialized_data = Column(JSONB(astext_type=Text()))

    email_body = relationship('OroEmailBody')
    from_email_address = relationship('OroEmailAddres')
    thread = relationship('OroEmailThread', primaryjoin='OroEmail.thread_id == OroEmailThread.id')
    users = relationship('OroUser', secondary='oro_rel_265353702da17977bb66fd')
    tasks = relationship('OrocrmTask', secondary='oro_rel_f24c741b265353702dde5c')
    tasks1 = relationship('OrocrmTask', secondary='oro_rel_26535370f24c741be77458')
    requests = relationship('OroRfpRequest', secondary='oro_rel_26535370f42ab603ec4b1d')
    leads = relationship('OrocrmSalesLead', secondary='oro_rel_2653537088a3cef53c57d4')
    opportunitys = relationship('OrocrmSalesOpportunity', secondary='oro_rel_265353705154c0033bfb48')
    requests1 = relationship('OrocrmContactusRequest', secondary='orocrm_contactus_req_emails')
    orders = relationship('OroOrder', secondary='oro_rel_2653537034e8bc9c2ddbe0')
    quotes = relationship('OroSaleQuote', secondary='oro_rel_26535370aab0e4f0b5ec88')


