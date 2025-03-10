from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailTemplate(Base):
    __tablename__ = 'oro_email_template'
    __table_args__ = (
        Index('uq_name', 'name', 'entityname', 'website_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_template_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    issystem = Column(Boolean, nullable=False, index=True)
    iseditable = Column(Boolean, nullable=False)
    name = Column(String(255), nullable=False, index=True)
    parent = Column(Integer)
    subject = Column(String(255), server_default=text("NULL::character varying"))
    content = Column(Text)
    entityname = Column(String(255), index=True, server_default=text("NULL::character varying"))
    type = Column(String(20), nullable=False)
    visible = Column(Boolean, nullable=False, server_default=text("true"))
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    website_id = Column(ForeignKey('oro_website.id', ondelete='CASCADE'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    user_owner = relationship('OroUser')
    website = relationship('OroWebsite')


t_oro_email_user_folders = Table(
    'oro_email_user_folders', metadata,
    Column('email_user_id', ForeignKey('oro_email_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('folder_id', ForeignKey('oro_email_folder.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_payment_mtds_rule_website = Table(
    'oro_payment_mtds_rule_website', metadata,
    Column('oro_payment_mtds_cfgs_rl_id', ForeignKey('oro_payment_mtds_cfgs_rl.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('website_id', ForeignKey('oro_website.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


