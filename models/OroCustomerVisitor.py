from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCustomerVisitor(Base):
    __tablename__ = 'oro_customer_visitor'
    __table_args__ = (
        Index('id_session_id_idx', 'id', 'session_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_customer_visitor_id_seq'::regclass)"))
    customer_user_id = Column(ForeignKey('oro_customer_user.id', ondelete='SET NULL'), unique=True)
    last_visit = Column(TIMESTAMP(precision=0), nullable=False)
    session_id = Column(String(255), nullable=False)
    cookies_accepted = Column(Boolean, nullable=False, index=True, server_default=text("false"))
    serialized_data = Column(JSONB(astext_type=Text()))

    customer_user = relationship('OroCustomerUser')
    shoppinglists = relationship('OroShoppingList', secondary='oro_rel_c56bdd4f6444702dedcb9c')


