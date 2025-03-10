from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmTask(Base):
    __tablename__ = 'orocrm_task'
    __table_args__ = (
        Index('task_updated_at_idx', 'updated_at', 'id'),
        Index('task_due_date_idx', 'due_date', 'id')
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_task_id_seq'::regclass)"))
    task_priority_name = Column(ForeignKey('orocrm_task_priority.name', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    created_by_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    status_id = Column(ForeignKey('oro_enum_task_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    subject = Column(String(255), server_default=text("NULL::character varying"))
    description = Column(Text)
    due_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    serialized_data = Column(JSONB(astext_type=Text()))

    created_by = relationship('OroUser', primaryjoin='OrocrmTask.created_by_id == OroUser.id')
    organization = relationship('OroOrganization')
    owner = relationship('OroUser', primaryjoin='OrocrmTask.owner_id == OroUser.id')
    status = relationship('OroEnumTaskStatu')
    orocrm_task_priority = relationship('OrocrmTaskPriority')


