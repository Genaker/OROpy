from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroEmailTemplateLocalized(Base):
    __tablename__ = 'oro_email_template_localized'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_email_template_localized_id_seq'::regclass)"))
    template_id = Column(ForeignKey('oro_email_template.id', ondelete='CASCADE'), nullable=False, index=True)
    localization_id = Column(ForeignKey('oro_localization.id', ondelete='CASCADE'), nullable=False, index=True)
    subject = Column(String(255), server_default=text("NULL::character varying"))
    subject_fallback = Column(Boolean, nullable=False, server_default=text("true"))
    content = Column(Text)
    content_fallback = Column(Boolean, nullable=False, server_default=text("true"))
    serialized_data = Column(JSONB(astext_type=Text()))

    localization = relationship('OroLocalization')
    template = relationship('OroEmailTemplate')


