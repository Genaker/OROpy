from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroAccessGroup(Base):
    __tablename__ = 'oro_access_group'
    __table_args__ = (
        Index('uq_name_org_idx', 'name', 'organization_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_access_group_id_seq'::regclass)"))
    business_unit_owner_id = Column(ForeignKey('oro_business_unit.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    name = Column(String(30), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    business_unit_owner = relationship('OroBusinessUnit')
    organization = relationship('OroOrganization')
    users = relationship('OroUser', secondary='oro_user_access_group')
    roles = relationship('OroAccessRole', secondary='oro_user_access_group_role')
    recipient_lists = relationship('OroNotificationRecipList', secondary='oro_notification_recip_group')


