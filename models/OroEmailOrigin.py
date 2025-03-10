from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailOrigin(Base):
    __tablename__ = 'oro_email_origin'
    __table_args__ = (
        Index('isactive_name_idx', 'isactive', 'name'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_origin_id_seq'::regclass)"))
    isactive = Column(Boolean, nullable=False)
    is_sync_enabled = Column(Boolean)
    sync_code_updated = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    synchronized = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    sync_code = Column(Integer)
    name = Column(String(30), nullable=False)
    internal_name = Column(String(30), server_default=text("NULL::character varying"))
    sync_count = Column(Integer)
    mailbox_name = Column(String(64), nullable=False, index=True, server_default=text("''::character varying"))
    owner_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='CASCADE'), index=True)
    imap_host = Column(String(255), server_default=text("NULL::character varying"))
    imap_port = Column(Integer)
    imap_ssl = Column(String(3), server_default=text("NULL::character varying"))
    imap_user = Column(String(100), server_default=text("NULL::character varying"))
    imap_password = Column(Text)
    smtp_host = Column(String(255), server_default=text("NULL::character varying"))
    smtp_port = Column(Integer)
    smtp_encryption = Column(String(3), server_default=text("NULL::character varying"))
    access_token = Column(Text)
    refresh_token = Column(Text)
    access_token_expires_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    account_type = Column(String(255), server_default=text("'other'::character varying"))

    organization = relationship('OroOrganization')
    owner = relationship('OroUser')


