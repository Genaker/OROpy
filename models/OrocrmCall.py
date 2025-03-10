from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmCall(Base):
    __tablename__ = 'orocrm_call'
    __table_args__ = (
        Index('call_dt_idx', 'call_date_time', 'id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_call_id_seq'::regclass)"))
    call_direction_name = Column(ForeignKey('orocrm_call_direction.name', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    call_status_name = Column(ForeignKey('orocrm_call_status.name', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    subject = Column(String(255), nullable=False)
    phone_number = Column(String(255), server_default=text("NULL::character varying"))
    notes = Column(Text)
    call_date_time = Column(TIMESTAMP(precision=0), nullable=False)
    duration = Column(Integer, comment='(DC2Type:duration)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    orocrm_call_direction = relationship('OrocrmCallDirection')
    orocrm_call_statu = relationship('OrocrmCallStatu')
    organization = relationship('OroOrganization')
    owner = relationship('OroUser')
    users = relationship('OroUser', secondary='oro_rel_6cbc80002da17977bb66fd')
    contacts = relationship('OrocrmContact', secondary='oro_rel_6cbc800083dfdfa436b4e2')
    caseentitys = relationship('OrocrmCase', secondary='oro_rel_6cbc80009e0854fe254c12')
    contactrequests = relationship('OrocrmContactusRequest', secondary='oro_rel_6cbc800050ef1ed9f45d78')
    leads = relationship('OrocrmSalesLead', secondary='oro_rel_6cbc800088a3cef53c57d4')
    opportunitys = relationship('OrocrmSalesOpportunity', secondary='oro_rel_6cbc80005154c0033bfb48')


