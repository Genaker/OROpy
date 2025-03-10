from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmAnalyticsRfmCategory(Base):
    __tablename__ = 'orocrm_analytics_rfm_category'

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_analytics_rfm_category_id_seq'::regclass)"))
    channel_id = Column(ForeignKey('orocrm_channel.id', ondelete='SET NULL'), index=True)
    owner_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    category_type = Column(String(16), nullable=False)
    category_index = Column(Integer, nullable=False)
    min_value = Column(Float(53))
    max_value = Column(Float(53))

    channel = relationship('OrocrmChannel')
    owner = relationship('OroOrganization')


