from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroMenuUserAgentCondition(Base):
    __tablename__ = 'oro_menu_user_agent_condition'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_menu_user_agent_condition_id_seq'::regclass)"))
    menu_update_id = Column(ForeignKey('oro_commerce_menu_upd.id', ondelete='CASCADE'), index=True)
    condition_group_identifier = Column(Integer, nullable=False)
    operation = Column(String(32), nullable=False)
    value = Column(String(255), nullable=False)

    menu_update = relationship('OroCommerceMenuUpd')


t_oro_navigation_menu_upd_descr = Table(
    'oro_navigation_menu_upd_descr', metadata,
    Column('menu_update_id', ForeignKey('oro_navigation_menu_upd.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


t_oro_navigation_menu_upd_title = Table(
    'oro_navigation_menu_upd_title', metadata,
    Column('menu_update_id', ForeignKey('oro_navigation_menu_upd.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('localized_value_id', ForeignKey('oro_fallback_localization_val.id', ondelete='CASCADE'), primary_key=True, nullable=False, unique=True)
)


