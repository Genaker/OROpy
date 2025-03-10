from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTaxValue(Base):
    __tablename__ = 'oro_tax_value'
    __table_args__ = (
        Index('oro_tax_value_class_id_idx', 'entity_class', 'entity_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_tax_value_id_seq'::regclass)"))
    result = Column(JSON, nullable=False, comment='(DC2Type:json_array)(DC2Type:json_array)')
    entity_class = Column(String(255), nullable=False)
    entity_id = Column(Integer)
    address = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')


