from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroFedexShipServiceRule(Base):
    __tablename__ = 'oro_fedex_ship_service_rule'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_fedex_ship_service_rule_id_seq'::regclass)"))
    limitation_expression_lbs = Column(String(250), nullable=False)
    limitation_expression_kg = Column(String(250), nullable=False)
    service_type = Column(String(250), server_default=text("NULL::character varying"))
    residential_address = Column(Boolean, nullable=False, server_default=text("false"))


