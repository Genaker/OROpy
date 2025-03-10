from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmContactusContactRsn(Base):
    __tablename__ = 'orocrm_contactus_contact_rsn'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_contactus_contact_rsn_id_seq'::regclass)"))
    deletedat = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    serialized_data = Column(JSONB(astext_type=Text()))

    localized_values = relationship('OroFallbackLocalizationVal', secondary='orocrm_contactus_contact_rsn_t')


