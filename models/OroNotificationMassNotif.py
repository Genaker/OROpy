from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroNotificationMassNotif(Base):
    __tablename__ = 'oro_notification_mass_notif'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_notification_mass_notif_id_seq'::regclass)"))
    email = Column(String(255), nullable=False)
    sender = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=False)
    body = Column(Text)
    scheduledat = Column(TIMESTAMP(precision=0), nullable=False)
    processedat = Column(TIMESTAMP(precision=0), nullable=False)
    status = Column(Integer, nullable=False)


