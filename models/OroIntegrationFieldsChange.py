from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroIntegrationFieldsChange(Base):
    __tablename__ = 'oro_integration_fields_changes'
    __table_args__ = (
        Index('oro_integration_fields_changes_idx', 'entity_id', 'entity_class'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_integration_fields_changes_id_seq'::regclass)"))
    entity_class = Column(String(255), nullable=False)
    entity_id = Column(Integer, nullable=False)
    changed_fields = Column(Text, nullable=False, comment='(DC2Type:array)(DC2Type:array)')


