from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailThread(Base):
    __tablename__ = 'oro_email_thread'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_thread_id_seq'::regclass)"))
    last_unseen_email_id = Column(ForeignKey('oro_email.id'), index=True)
    created = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')

    last_unseen_email = relationship('OroEmail', primaryjoin='OroEmailThread.last_unseen_email_id == OroEmail.id')


