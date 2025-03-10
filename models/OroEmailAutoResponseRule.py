from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailAutoResponseRule(Base):
    __tablename__ = 'oro_email_auto_response_rule'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_auto_response_rule_id_seq'::regclass)"))
    template_id = Column(ForeignKey('oro_email_template.id', ondelete='CASCADE'), index=True)
    mailbox_id = Column(ForeignKey('oro_email_mailbox.id', ondelete='CASCADE'), index=True)
    name = Column(String(255), nullable=False)
    active = Column(Boolean, nullable=False)
    createdat = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    definition = Column(Text)

    mailbox = relationship('OroEmailMailbox')
    template = relationship('OroEmailTemplate')


