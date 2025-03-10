from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroSidebarWidget(Base):
    __tablename__ = 'oro_sidebar_widget'
    __table_args__ = (
        Index('sidebar_widgets_user_placement_idx', 'user_id', 'placement'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_sidebar_widget_id_seq'::regclass)"))
    user_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), nullable=False, index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    placement = Column(String(50), nullable=False)
    position = Column(SmallInteger, nullable=False, index=True)
    widget_name = Column(String(50), nullable=False)
    settings = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    state = Column(String(22), nullable=False)

    organization = relationship('OroOrganization')
    user = relationship('OroUser')


