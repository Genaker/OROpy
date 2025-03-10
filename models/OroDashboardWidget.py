from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroDashboardWidget(Base):
    __tablename__ = 'oro_dashboard_widget'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_dashboard_widget_id_seq'::regclass)"))
    dashboard_id = Column(ForeignKey('oro_dashboard.id', ondelete='CASCADE'), index=True)
    name = Column(String(255), nullable=False)
    layout_position = Column(Text, nullable=False, comment='(DC2Type:simple_array)(DC2Type:simple_array)')
    options = Column(Text, comment='(DC2Type:array)(DC2Type:array)')

    dashboard = relationship('OroDashboard')


