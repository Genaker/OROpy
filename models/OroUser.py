from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroUser(Base):
    __tablename__ = 'oro_user'
    __table_args__ = (
        Index('user_first_name_last_name_idx', 'first_name', 'last_name'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_user_id_seq'::regclass)"))
    business_unit_owner_id = Column(ForeignKey('oro_business_unit.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    avatar_id = Column(ForeignKey('oro_attachment_file.id', ondelete='SET NULL'), index=True)
    auth_status_id = Column(ForeignKey('oro_enum_auth_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    username = Column(String(255), nullable=False, unique=True)
    username_lowercase = Column(String(255), nullable=False, index=True)
    email = Column(String(255), nullable=False, unique=True)
    email_lowercase = Column(String(255), nullable=False, index=True)
    phone = Column(String(255), index=True, server_default=text("NULL::character varying"))
    name_prefix = Column(String(255), server_default=text("NULL::character varying"))
    first_name = Column(String(255), server_default=text("NULL::character varying"))
    middle_name = Column(String(255), server_default=text("NULL::character varying"))
    last_name = Column(String(255), server_default=text("NULL::character varying"))
    name_suffix = Column(String(255), server_default=text("NULL::character varying"))
    birthday = Column(Date)
    enabled = Column(Boolean, nullable=False)
    salt = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    confirmation_token = Column(String(255), server_default=text("NULL::character varying"))
    password_requested = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    password_changed = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    last_login = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    login_count = Column(Integer, nullable=False, server_default=text("0"))
    createdat = Column(TIMESTAMP(precision=0), nullable=False)
    updatedat = Column(TIMESTAMP(precision=0), nullable=False)
    title = Column(String(255), server_default=text("NULL::character varying"))
    googleid = Column(String(255), index=True, server_default=text("NULL::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    auth_status = relationship('OroEnumAuthStatu')
    avatar = relationship('OroAttachmentFile', primaryjoin='OroUser.avatar_id == OroAttachmentFile.id')
    business_unit_owner = relationship('OroBusinessUnit')
    organization = relationship('OroOrganization')


