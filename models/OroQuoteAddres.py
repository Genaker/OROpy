from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroQuoteAddres(Base):
    __tablename__ = 'oro_quote_address'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_quote_address_id_seq'::regclass)"))
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
    created = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    serialized_data = Column(JSONB(astext_type=Text()))

    oro_dictionary_country = relationship('OroDictionaryCountry')
    customer_address = relationship('OroCustomerAddres')
    customer_user_address = relationship('OroCustomerUserAddres')
    oro_dictionary_region = relationship('OroDictionaryRegion')


t_oro_rel_2653537050ef1ed9f45d78 = Table(
    'oro_rel_2653537050ef1ed9f45d78', metadata,
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('contactrequest_id', ForeignKey('orocrm_contactus_request.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_26535370f42ab603ec4b1d = Table(
    'oro_rel_26535370f42ab603ec4b1d', metadata,
    Column('email_id', ForeignKey('oro_email.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('request_id', ForeignKey('oro_rfp_request.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_46a29d19f42ab603ec4b1d = Table(
    'oro_rel_46a29d19f42ab603ec4b1d', metadata,
    Column('calendarevent_id', ForeignKey('oro_calendar_event.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('request_id', ForeignKey('oro_rfp_request.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6cbc800050ef1ed9f45d78 = Table(
    'oro_rel_6cbc800050ef1ed9f45d78', metadata,
    Column('call_id', ForeignKey('orocrm_call.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('contactrequest_id', ForeignKey('orocrm_contactus_request.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_6f8f552af42ab603ec4b1d = Table(
    'oro_rel_6f8f552af42ab603ec4b1d', metadata,
    Column('note_id', ForeignKey('oro_note.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('request_id', ForeignKey('oro_rfp_request.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba650ef1ed91c32d0 = Table(
    'oro_rel_c3990ba650ef1ed91c32d0', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('contactrequest_id', ForeignKey('orocrm_contactus_request.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c3990ba6f42ab603ed4e03 = Table(
    'oro_rel_c3990ba6f42ab603ed4e03', metadata,
    Column('activitylist_id', ForeignKey('oro_activity_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('request_id', ForeignKey('oro_rfp_request.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rel_c56bdd4f6444702dedcb9c = Table(
    'oro_rel_c56bdd4f6444702dedcb9c', metadata,
    Column('customervisitor_id', ForeignKey('oro_customer_visitor.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('shoppinglist_id', ForeignKey('oro_shopping_list.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rfp_assigned_cus_users = Table(
    'oro_rfp_assigned_cus_users', metadata,
    Column('request_id', ForeignKey('oro_rfp_request.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('customer_user_id', ForeignKey('oro_customer_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


t_oro_rfp_assigned_users = Table(
    'oro_rfp_assigned_users', metadata,
    Column('request_id', ForeignKey('oro_rfp_request.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('user_id', ForeignKey('oro_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


