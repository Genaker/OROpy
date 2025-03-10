from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroFrontendImportExportResult(Base):
    __tablename__ = 'oro_frontend_import_export_result'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_frontend_import_export_result_id_seq'::regclass)"))
    owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    customer_id = Column(ForeignKey('oro_customer.id', ondelete='SET NULL'), index=True)
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='SET NULL'), index=True)
    filename = Column(String(255), unique=True, server_default=text("NULL::character varying"))
    job_id = Column(Integer, nullable=False, unique=True)
    type = Column(String(255), nullable=False)
    entity = Column(String(255), nullable=False)
    options = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    expired = Column(Boolean, nullable=False, server_default=text("false"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False)

    customer = relationship('OroCustomer')
    customer_user = relationship('OroCustomerUser')
    organization = relationship('OroOrganization')
    owner = relationship('OroUser')


