from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmChannelCustIdentity(Base):
    __tablename__ = 'orocrm_channel_cust_identity'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_channel_cust_identity_id_seq'::regclass)"))
    contact_id = Column(ForeignKey('orocrm_contact.id', ondelete='SET NULL'), index=True)
    account_id = Column(ForeignKey('orocrm_account.id', ondelete='SET NULL'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    data_channel_id = Column(ForeignKey('orocrm_channel.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False)
    createdat = Column(TIMESTAMP(precision=0), nullable=False)
    updatedat = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    serialized_data = Column(JSONB(astext_type=Text()))

    account = relationship('OrocrmAccount')
    contact = relationship('OrocrmContact')
    data_channel = relationship('OrocrmChannel')
    user_owner = relationship('OroUser')


