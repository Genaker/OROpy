from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroAccessRole(Base):
    __tablename__ = 'oro_access_role'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_access_role_id_seq'::regclass)"))
    role = Column(String(30), nullable=False, unique=True)
    label = Column(String(30), nullable=False)
    extend_description = Column(Text)
    serialized_data = Column(JSONB(astext_type=Text()))

    users = relationship('OroUser', secondary='oro_user_access_role')


