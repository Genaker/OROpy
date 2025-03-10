from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroSidebarState(Base):
    __tablename__ = 'oro_sidebar_state'
    __table_args__ = (
        Index('sidebar_state_unique_idx', 'user_id', 'position', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_sidebar_state_id_seq'::regclass)"))
    user_id = Column(ForeignKey('oro_user.id', ondelete='CASCADE'), nullable=False, index=True)
    position = Column(String(13), nullable=False)
    state = Column(String(17), nullable=False)

    user = relationship('OroUser')


