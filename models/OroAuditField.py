from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroAuditField(Base):
    __tablename__ = 'oro_audit_field'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_audit_field_id_seq'::regclass)"))
    audit_id = Column(ForeignKey('oro_audit.id', ondelete='CASCADE'), nullable=False, index=True)
    field = Column(String(255), nullable=False)
    data_type = Column(String(255), nullable=False)
    old_integer = Column(BigInteger)
    old_float = Column(Float(53))
    old_boolean = Column(Boolean)
    old_text = Column(Text)
    old_date = Column(Date)
    old_time = Column(TIME(precision=0), server_default=text("NULL::time without time zone"))
    old_datetime = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    new_integer = Column(BigInteger)
    new_float = Column(Float(53))
    new_boolean = Column(Boolean)
    new_text = Column(Text)
    new_date = Column(Date)
    new_time = Column(TIME(precision=0), server_default=text("NULL::time without time zone"))
    new_datetime = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    old_datetimetz = Column(TIMESTAMP(True, 0), server_default=text("NULL::timestamp with time zone"), comment='(DC2Type:datetimetz)')
    old_object = Column(Text, comment='(DC2Type:object)(DC2Type:object)')
    new_datetimetz = Column(TIMESTAMP(True, 0), server_default=text("NULL::timestamp with time zone"), comment='(DC2Type:datetimetz)')
    new_object = Column(Text, comment='(DC2Type:object)(DC2Type:object)')
    visible = Column(Boolean, nullable=False, server_default=text("true"))
    old_array = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    new_array = Column(Text, comment='(DC2Type:array)(DC2Type:array)')
    old_simplearray = Column(Text, comment='(DC2Type:simple_array)(DC2Type:simple_array)')
    new_simplearray = Column(Text, comment='(DC2Type:simple_array)(DC2Type:simple_array)')
    old_jsonarray = Column(JSON, comment='(DC2Type:json_array)(DC2Type:json_array)')
    new_jsonarray = Column(JSON, comment='(DC2Type:json_array)(DC2Type:json_array)')
    collection_diffs = Column(JSON, comment='(DC2Type:json_array)(DC2Type:json_array)')
    translation_domain = Column(String(100), server_default=text("NULL::character varying"))

    audit = relationship('OroAudit')


t_oro_commerce_menu_upd_descr = Table(
    'oro_commerce_menu_upd_descr', metadata,
    Column('menu_update_id', ForeignKey('oro_commerce_menu_upd.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_commerce_menu_upd_title = Table(
    'oro_commerce_menu_upd_title', metadata,
    Column('menu_update_id', ForeignKey('oro_commerce_menu_upd.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


