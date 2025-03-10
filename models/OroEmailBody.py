from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailBody(Base):
    __tablename__ = 'oro_email_body'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_body_id_seq'::regclass)"))
    created = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    body = Column(Text, nullable=False)
    body_is_text = Column(Boolean, nullable=False)
    has_attachments = Column(Boolean, nullable=False)
    persistent = Column(Boolean, nullable=False)
    text_body = Column(Text)


