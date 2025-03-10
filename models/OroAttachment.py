from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroAttachment(Base):
    __tablename__ = 'oro_attachment'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_attachment_id_seq'::regclass)"))
    file_id = Column(ForeignKey('oro_attachment_file.id'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    comment = Column(Text)
    owner_user_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    product_f4309915_id = Column(ForeignKey('oro_product.id', ondelete='SET NULL'), index=True)
    customer_user_539cf909_id = Column(ForeignKey('oro_customer_user.id', ondelete='SET NULL'), index=True)
    customer_e2cfcbe5_id = Column(ForeignKey('oro_customer.id', ondelete='SET NULL'), index=True)
    account_8d93c122_id = Column(ForeignKey('orocrm_account.id', ondelete='SET NULL'), index=True)
    opportunity_f89bd07c_id = Column(ForeignKey('orocrm_sales_opportunity.id', ondelete='SET NULL'), index=True)
    order_50627d4f_id = Column(ForeignKey('oro_order.id', ondelete='SET NULL'), index=True)
    quote_7de78df3_id = Column(ForeignKey('oro_sale_quote.id', ondelete='SET NULL'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    account_8d93c122 = relationship('OrocrmAccount')
    customer_e2cfcbe5 = relationship('OroCustomer')
    customer_user_539cf909 = relationship('OroCustomerUser')
    file = relationship('OroAttachmentFile')
    opportunity_f89bd07c = relationship('OrocrmSalesOpportunity')
    order_50627d4f = relationship('OroOrder')
    organization = relationship('OroOrganization')
    owner_user = relationship('OroUser')
    product_f4309915 = relationship('OroProduct')
    quote_7de78df3 = relationship('OroSaleQuote')


