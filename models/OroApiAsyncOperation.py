from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroApiAsyncOperation(Base):
    __tablename__ = 'oro_api_async_operation'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_api_async_operation_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    status = Column(String(10), nullable=False)
    progress = Column(Float(53), comment='(DC2Type:percent)(DC2Type:percent)')
    job_id = Column(Integer)
    data_file_name = Column(String(50), nullable=False)
    entity_class = Column(String(255), nullable=False)
    action_name = Column(String(20), nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    elapsed_time = Column(Integer, nullable=False)
    has_errors = Column(Boolean, nullable=False, server_default=text("false"))
    summary = Column(JSON, comment='(DC2Type:json_array)(DC2Type:json_array)')
    affected_entities = Column(JSON, comment='(DC2Type:json)')

    organization = relationship('OroOrganization')
    user_owner = relationship('OroUser')


