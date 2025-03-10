from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroNavigationMenuUpd(Base):
    __tablename__ = 'oro_navigation_menu_upd'
    __table_args__ = (
        Index('oro_navigation_menu_upd_uidx', 'key', 'scope_id', 'menu', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_navigation_menu_upd_id_seq'::regclass)"))
    scope_id = Column(ForeignKey('oro_scope.id'), nullable=False, index=True)
    key = Column(String(100), nullable=False)
    parent_key = Column(String(100), server_default=text("NULL::character varying"))
    uri = Column(String(8190), server_default=text("NULL::character varying"))
    menu = Column(String(100), nullable=False)
    icon = Column(String(150), server_default=text("NULL::character varying"))
    is_active = Column(Boolean, nullable=False)
    is_divider = Column(Boolean, nullable=False)
    is_custom = Column(Boolean, nullable=False)
    is_synthetic = Column(Boolean, nullable=False, server_default=text("false"))
    priority = Column(Integer)
    serialized_data = Column(JSONB(astext_type=Text()))

    scope = relationship('OroScope')


