from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCmsContentWidgetUsage(Base):
    __tablename__ = 'oro_cms_content_widget_usage'
    __table_args__ = (
        Index('uidx_oro_cms_content_widget_usage', 'entity_class', 'entity_id', 'entity_field', 'content_widget_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cms_content_widget_usage_id_seq'::regclass)"))
    content_widget_id = Column(ForeignKey('oro_cms_content_widget.id', ondelete='CASCADE'), nullable=False, index=True)
    entity_class = Column(String(255), nullable=False)
    entity_id = Column(Integer, nullable=False)
    entity_field = Column(String(50), server_default=text("NULL::character varying"))

    content_widget = relationship('OroCmsContentWidget')


