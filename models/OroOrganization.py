from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroOrganization(Base):
    __tablename__ = 'oro_organization'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_organization_id_seq'::regclass)"))
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    created_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    enabled = Column(Boolean, nullable=False, server_default=text("true"))
    serialized_data = Column(JSONB(astext_type=Text()))

    users = relationship('OroUser', secondary='oro_user_organization')


