from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroDashboardWidgetState(Base):
    __tablename__ = 'oro_dashboard_widget_state'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_dashboard_widget_state_id_seq'::regclass)"))
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), index=True)
    widget_id = Column(ForeignKey('oro_dashboard_widget.id', ondelete='CASCADE'), index=True)
    is_expanded = Column(Boolean, nullable=False)

    user_owner = relationship('OroUser')
    widget = relationship('OroDashboardWidget')


