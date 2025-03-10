from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroOrderAddres(Base):
    __tablename__ = 'oro_order_address'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_order_address_id_seq'::regclass)"))
    customer_address_id = Column(ForeignKey('oro_customer_address.id', ondelete='SET NULL'), index=True)
    customer_user_address_id = Column(ForeignKey('oro_customer_user_address.id', ondelete='SET NULL'), index=True)
    region_code = Column(ForeignKey('oro_dictionary_region.combined_code'), index=True, server_default=text("NULL::character varying"))
    country_code = Column(ForeignKey('oro_dictionary_country.iso2_code'), index=True, server_default=text("NULL::character varying"))
    label = Column(String(255), server_default=text("NULL::character varying"))
    street = Column(String(500), server_default=text("NULL::character varying"))
    street2 = Column(String(500), server_default=text("NULL::character varying"))
    city = Column(String(255), server_default=text("NULL::character varying"))
    postal_code = Column(String(255), server_default=text("NULL::character varying"))
    organization = Column(String(255), server_default=text("NULL::character varying"))
    region_text = Column(String(255), server_default=text("NULL::character varying"))
    name_prefix = Column(String(255), server_default=text("NULL::character varying"))
    first_name = Column(String(255), server_default=text("NULL::character varying"))
    middle_name = Column(String(255), server_default=text("NULL::character varying"))
    last_name = Column(String(255), server_default=text("NULL::character varying"))
    name_suffix = Column(String(255), server_default=text("NULL::character varying"))
    phone = Column(String(255), server_default=text("NULL::character varying"))
    from_external_source = Column(Boolean, nullable=False, server_default=text("false"))
    created = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    serialized_data = Column(JSONB(astext_type=Text()))

    oro_dictionary_country = relationship('OroDictionaryCountry')
    customer_address = relationship('OroCustomerAddres')
    customer_user_address = relationship('OroCustomerUserAddres')
    oro_dictionary_region = relationship('OroDictionaryRegion')


