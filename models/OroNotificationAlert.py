from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroNotificationAlert(Base):
    __tablename__ = 'oro_notification_alert'

    id = Column(UUID, primary_key=True)
    user_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='CASCADE'), nullable=False, index=True)
    alert_type = Column(String(20), server_default=text("NULL::character varying"))
    source_type = Column(String(50), nullable=False)
    resource_type = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    operation = Column(String(50), server_default=text("NULL::character varying"))
    step = Column(String(50), server_default=text("NULL::character varying"))
    item_id = Column(Integer)
    external_id = Column(String(255), server_default=text("NULL::character varying"))
    is_resolved = Column(Boolean, nullable=False, server_default=text("false"))
    message = Column(Text)
    additional_info = Column(JSON, comment='(DC2Type:json)')
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    user = relationship('OroUser')


t_oro_notification_recip_user = Table(
    'oro_notification_recip_user', metadata,
    Column('recipient_list_id', ForeignKey('oro_notification_recip_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('user_id', ForeignKey('oro_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


