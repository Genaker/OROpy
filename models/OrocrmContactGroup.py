from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmContactGroup(Base):
    __tablename__ = 'orocrm_contact_group'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_contact_group_id_seq'::regclass)"))
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    label = Column(String(30), nullable=False, unique=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    user_owner = relationship('OroUser')
    contacts = relationship('OrocrmContact', secondary='orocrm_contact_to_contact_grp')


