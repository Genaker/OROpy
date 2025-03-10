from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroNote(Base):
    __tablename__ = 'oro_note'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_note_id_seq'::regclass)"))
    user_owner_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    updated_by_user_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    attachment_id = Column(ForeignKey('oro_attachment_file.id', ondelete='SET NULL'), index=True)
    message = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    serialized_data = Column(JSONB(astext_type=Text()))

    attachment = relationship('OroAttachmentFile')
    organization = relationship('OroOrganization')
    updated_by_user = relationship('OroUser', primaryjoin='OroNote.updated_by_user_id == OroUser.id')
    user_owner = relationship('OroUser', primaryjoin='OroNote.user_owner_id == OroUser.id')
    websites = relationship('OroWebsite', secondary='oro_rel_6f8f552a88d2647be4fd56')
    webcatalogs = relationship('OroWebCatalog', secondary='oro_rel_6f8f552a758542cfbd3dfc')
    products = relationship('OroProduct', secondary='oro_rel_6f8f552a1cf73d3129e5bb')
    paymentmethodsconfigsrules = relationship('OroPaymentMtdsCfgsRl', secondary='oro_rel_6f8f552aa73c785c4e6d3f')
    paymentterms = relationship('OroPaymentTerm', secondary='oro_rel_6f8f552af9a91faa3967ca')
    pricelists = relationship('OroPriceList', secondary='oro_rel_6f8f552a7e0cc7f027a8f9')
    requests = relationship('OroRfpRequest', secondary='oro_rel_6f8f552af42ab603ec4b1d')
    opportunitys = relationship('OrocrmSalesOpportunity', secondary='oro_rel_6f8f552a5154c0033bfb48')
    orders = relationship('OroOrder', secondary='oro_rel_6f8f552a34e8bc9c2ddbe0')
    quotes = relationship('OroSaleQuote', secondary='oro_rel_6f8f552aaab0e4f0b5ec88')
    promotions = relationship('OroPromotion', secondary='oro_rel_6f8f552a43ecff72f0d342')
    shippingmethodsconfigsrules = relationship('OroShipMethodConfigsRule', secondary='oro_rel_6f8f552a2c175de41f8af0')


