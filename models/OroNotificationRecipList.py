from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroNotificationRecipList(Base):
    __tablename__ = 'oro_notification_recip_list'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_notification_recip_list_id_seq'::regclass)"))
    email = Column(String(255), server_default=text("NULL::character varying"))
    additional_email_associations = Column(Text, comment='(DC2Type:simple_array)(DC2Type:simple_array)')
    entity_emails = Column(Text, comment='(DC2Type:simple_array)(DC2Type:simple_array)')

    users = relationship('OroUser', secondary='oro_notification_recip_user')


