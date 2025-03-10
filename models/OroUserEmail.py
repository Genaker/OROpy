from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroUserEmail(Base):
    __tablename__ = 'oro_user_email'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_user_email_id_seq'::regclass)"))
    user_id = Column(ForeignKey('oro_user.id'), index=True)
    email = Column(String(255), nullable=False, index=True)

    user = relationship('OroUser')


