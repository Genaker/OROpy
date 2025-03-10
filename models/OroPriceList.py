from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroPriceList(Base):
    __tablename__ = 'oro_price_list'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_price_list_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False)
    active = Column(Boolean, nullable=False, server_default=text("true"))
    actual = Column(Boolean, nullable=False, server_default=text("true"))
    product_assignment_rule = Column(Text)
    contain_schedule = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')


