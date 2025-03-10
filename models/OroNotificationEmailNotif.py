from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroNotificationEmailNotif(Base):
    __tablename__ = 'oro_notification_email_notif'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_notification_email_notif_id_seq'::regclass)"))
    recipient_list_id = Column(ForeignKey('oro_notification_recip_list.id'), unique=True)
    template_id = Column(ForeignKey('oro_email_template.id', ondelete='SET NULL'), index=True)
    event_name = Column(String(255), server_default=text("NULL::character varying"))
    entity_name = Column(String(255), nullable=False)
    workflow_definition_name = Column(ForeignKey('oro_workflow_definition.name', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    workflow_transition_name = Column(String(255), index=True, server_default=text("NULL::character varying"))
    serialized_data = Column(JSONB(astext_type=Text()))

    recipient_list = relationship('OroNotificationRecipList')
    template = relationship('OroEmailTemplate')
    oro_workflow_definition = relationship('OroWorkflowDefinition')


