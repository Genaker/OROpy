from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroAttributeGroup(Base):
    __tablename__ = 'oro_attribute_group'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_attribute_group_id_seq'::regclass)"))
    attribute_family_id = Column(ForeignKey('oro_attribute_family.id'), index=True)
    code = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    is_visible = Column(Boolean, nullable=False, server_default=text("true"))

    attribute_family = relationship('OroAttributeFamily')
    localized_values = relationship('OroFallbackLocalizationVal', secondary='oro_attribute_group_label')


