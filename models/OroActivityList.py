from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroActivityList(Base):
    __tablename__ = 'oro_activity_list'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_activity_list_id_seq'::regclass)"))
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    user_editor_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    verb = Column(String(32), nullable=False)
    subject = Column(String(255), nullable=False)
    related_activity_class = Column(String(255), nullable=False, index=True)
    related_activity_id = Column(Integer, nullable=False, index=True)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, index=True)
    description = Column(Text)
    serialized_data = Column(JSONB(astext_type=Text()))

    organization = relationship('OroOrganization')
    user_editor = relationship('OroUser', primaryjoin='OroActivityList.user_editor_id == OroUser.id')
    user_owner = relationship('OroUser', primaryjoin='OroActivityList.user_owner_id == OroUser.id')
    customers = relationship('OroCustomer', secondary='oro_rel_c3990ba6784fec5f6e321b')
    customerusers = relationship('OroCustomerUser', secondary='oro_rel_c3990ba63708e583a2c61e')
    b2bcustomers = relationship('OrocrmSalesB2bcustomer', secondary='oro_rel_c3990ba6e65dd9d37deb67')
    orders = relationship('OroOrder', secondary='oro_rel_c3990ba634e8bc9cac53cb')
    emails = relationship('OroEmail', secondary='oro_rel_c3990ba62653537081b7e1')
    contacts = relationship('OrocrmContact', secondary='oro_rel_c3990ba683dfdfa4a13cb3')
    webcatalogs = relationship('OroWebCatalog', secondary='oro_rel_c3990ba6758542cf1cec5e')
    contentnodes = relationship('OroWebCatalogContentNode', secondary='oro_rel_c3990ba65b5187a374e72c')
    categorys = relationship('OroCatalogCategory', secondary='oro_rel_c3990ba6ff3a7b97760f68')
    customeruserroles = relationship('OroCustomerUserRole', secondary='oro_rel_c3990ba6d7fa01cd30d950')
    customergroups = relationship('OroCustomerGroup', secondary='oro_rel_c3990ba616cbf45899499b')
    tasks = relationship('OrocrmTask', secondary='oro_rel_c3990ba6f24c741b1d920a')
    pricelists = relationship('OroPriceList', secondary='oro_rel_c3990ba67e0cc7f01d1498')
    requests = relationship('OroRfpRequest', secondary='oro_rel_c3990ba6f42ab603ed4e03')
    contactrequests = relationship('OrocrmContactusRequest', secondary='oro_rel_c3990ba650ef1ed91c32d0')
    quotes = relationship('OroSaleQuote', secondary='oro_rel_c3990ba6aab0e4f07348a4')
    products = relationship('OroProduct', secondary='oro_rel_c3990ba61cf73d31624686')
    websites = relationship('OroWebsite', secondary='oro_rel_c3990ba688d2647b59a3ef')
    promotions = relationship('OroPromotion', secondary='oro_rel_c3990ba643ecff72e2f6de')
    shippingmethodsconfigsrules = relationship('OroShipMethodConfigsRule', secondary='oro_rel_c3990ba62c175de4fa9927')
    users = relationship('OroUser', secondary='oro_rel_c3990ba62da17977270bd6')
    paymentmethodsconfigsrules = relationship('OroPaymentMtdsCfgsRl', secondary='oro_rel_c3990ba6a73c785ca4a8ba')
    paymentterms = relationship('OroPaymentTerm', secondary='oro_rel_c3990ba6f9a91faa5f648d')
    opportunitys = relationship('OrocrmSalesOpportunity', secondary='oro_rel_c3990ba65154c0069aa16e')
    leads = relationship('OrocrmSalesLead', secondary='oro_rel_c3990ba688a3cef5c8efa6')
    caseentitys = relationship('OrocrmCase', secondary='oro_rel_c3990ba69e0854fe1d2e0c')


