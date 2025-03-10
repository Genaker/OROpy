from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroDashboard(Base):
    __tablename__ = 'oro_dashboard'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_dashboard_id_seq'::regclass)"))
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    dashboard_type_id = Column(ForeignKey('oro_enum_dashboard_type.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    name = Column(String(255), server_default=text("NULL::character varying"))
    label = Column(String(255), server_default=text("NULL::character varying"))
    is_default = Column(Boolean, nullable=False, index=True, server_default=text("false"))
    createdat = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updatedat = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    serialized_data = Column(JSONB(astext_type=Text()))

    dashboard_type = relationship('OroEnumDashboardType')
    organization = relationship('OroOrganization')
    user_owner = relationship('OroUser')


