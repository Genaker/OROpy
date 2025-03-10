from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroTranslation(Base):
    __tablename__ = 'oro_translation'
    __table_args__ = (
        Index('language_key_uniq', 'language_id', 'translation_key_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_translation_id_seq'::regclass)"))
    translation_key_id = Column(ForeignKey('oro_translation_key.id', ondelete='CASCADE'), nullable=False, index=True)
    language_id = Column(ForeignKey('oro_language.id', ondelete='CASCADE'), nullable=False, index=True)
    value = Column(Text)
    scope = Column(SmallInteger, nullable=False)

    language = relationship('OroLanguage')
    translation_key = relationship('OroTranslationKey')


t_oro_ups_transport_ship_service = Table(
    'oro_ups_transport_ship_service', metadata,
    Column('transport_id', ForeignKey('oro_integration_transport.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('ship_service_id', ForeignKey('oro_ups_shipping_service.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_user_business_unit = Table(
    'oro_user_business_unit', metadata,
    Column('user_id', ForeignKey('oro_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('business_unit_id', ForeignKey('oro_business_unit.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


