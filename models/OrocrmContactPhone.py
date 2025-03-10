from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmContactPhone(Base):
    __tablename__ = 'orocrm_contact_phone'
    __table_args__ = (
        Index('primary_phone_idx', 'phone', 'is_primary'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_contact_phone_id_seq'::regclass)"))
    owner_id = Column(ForeignKey('orocrm_contact.id', ondelete='CASCADE'), index=True)
    phone = Column(String(255), nullable=False, index=True)
    is_primary = Column(Boolean)
    serialized_data = Column(JSONB(astext_type=Text()))

    owner = relationship('OrocrmContact')


t_orocrm_contact_to_contact_grp = Table(
    'orocrm_contact_to_contact_grp', metadata,
    Column('contact_id', ForeignKey('orocrm_contact.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('contact_group_id', ForeignKey('orocrm_contact_group.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


