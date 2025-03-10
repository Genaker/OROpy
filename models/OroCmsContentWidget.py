from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCmsContentWidget(Base):
    __tablename__ = 'oro_cms_content_widget'
    __table_args__ = (
        Index('uidx_oro_cms_content_widget', 'organization_id', 'name', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cms_content_widget_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    widget_type = Column(String(255), nullable=False)
    layout = Column(String(255), server_default=text("NULL::character varying"))
    settings = Column(Text, nullable=False, comment='(DC2Type:array)')

    organization = relationship('OroOrganization')
    localized_values = relationship('OroFallbackLocalizationVal', secondary='oro_cms_content_widget_label')


