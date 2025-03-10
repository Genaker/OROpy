from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTrackingVisit(Base):
    __tablename__ = 'oro_tracking_visit'
    __table_args__ = (
        Index('website_first_action_time_idx', 'website_id', 'first_action_time'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tracking_visit_id_seq'::regclass)"))
    website_id = Column(ForeignKey('oro_tracking_website.id', ondelete='CASCADE'), index=True)
    visitor_uid = Column(String(255), nullable=False, index=True)
    ip = Column(String(255), server_default=text("NULL::character varying"))
    client = Column(String(255), server_default=text("NULL::character varying"))
    client_type = Column(String(255), server_default=text("NULL::character varying"))
    client_version = Column(String(255), server_default=text("NULL::character varying"))
    os = Column(String(255), server_default=text("NULL::character varying"))
    os_version = Column(String(255), server_default=text("NULL::character varying"))
    desktop = Column(Boolean)
    mobile = Column(Boolean)
    bot = Column(Boolean)
    user_identifier = Column(String(255), nullable=False, index=True)
    first_action_time = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    last_action_time = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    parsing_count = Column(Integer, nullable=False, server_default=text("0"))
    parsed_uid = Column(Integer, nullable=False, server_default=text("0"))
    identifier_detected = Column(Boolean, nullable=False, server_default=text("false"))
    code = Column(String(255), server_default=text("NULL::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    website = relationship('OroTrackingWebsite')


