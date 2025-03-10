from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroGridView(Base):
    __tablename__ = 'oro_grid_view'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_grid_view_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), index=True)
    name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    filtersdata = Column(Text, nullable=False, comment='(DC2Type:array)(DC2Type:array)')
    sortersdata = Column(Text, nullable=False, comment='(DC2Type:array)(DC2Type:array)')
    columnsdata = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    gridname = Column(String(255), nullable=False)
    appearancetype = Column(ForeignKey('oro_grid_appearance_type.name'), index=True, server_default=text("NULL::character varying"))
    appearancedata = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    discr_type = Column(String(255), nullable=False, index=True)
    customer_user_owner_id = Column(ForeignKey('oro_customer_user.id', ondelete='CASCADE'), index=True)

    oro_grid_appearance_type = relationship('OroGridAppearanceType')
    customer_user_owner = relationship('OroCustomerUser')
    organization = relationship('OroOrganization')
    user_owner = relationship('OroUser')


