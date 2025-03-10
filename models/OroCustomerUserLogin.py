from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCustomerUserLogin(Base):
    __tablename__ = 'oro_customer_user_login'

    id = Column(UUID, primary_key=True)
    user_id = Column(ForeignKey('oro_customer_user.id', ondelete='CASCADE'), index=True)
    attempt_at = Column(TIMESTAMP(precision=0), nullable=False, index=True, comment='(DC2Type:datetime)')
    success = Column(Boolean, nullable=False)
    source = Column(Integer, nullable=False)
    username = Column(String(255), server_default=text("NULL::character varying"))
    ip = Column(String(255), server_default=text("NULL::character varying"))
    user_agent = Column(Text, server_default=text("''::text"))
    context = Column(JSON, nullable=False, comment='(DC2Type:json)')

    user = relationship('OroCustomerUser')


t_oro_customer_user_sales_reps = Table(
    'oro_customer_user_sales_reps', metadata,
    Column('customer_user_id', ForeignKey('oro_customer_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('user_id', ForeignKey('oro_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


