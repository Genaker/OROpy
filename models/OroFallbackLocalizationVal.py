from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroFallbackLocalizationVal(Base):
    __tablename__ = 'oro_fallback_localization_val'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_fallback_localization_val_id_seq'::regclass)"))
    localization_id = Column(ForeignKey('oro_localization.id', ondelete='CASCADE'), index=True)
    fallback = Column(String(64), index=True, server_default=text("NULL::character varying"))
    string = Column(String(255), index=True, server_default=text("NULL::character varying"))
    text = Column(Text)
    wysiwyg = Column(Text, comment='(DC2Type:wysiwyg)(DC2Type:wysiwyg)')
    wysiwyg_style = Column(Text, comment='(DC2Type:wysiwyg_style)')
    wysiwyg_properties = Column(JSON, comment='(DC2Type:wysiwyg_properties)')
    serialized_data = Column(JSONB(astext_type=Text()))

    localization = relationship('OroLocalization')
    menu_updates = relationship('OroNavigationMenuUpd', secondary='oro_navigation_menu_upd_title')
    menu_updates1 = relationship('OroNavigationMenuUpd', secondary='oro_navigation_menu_upd_descr')
    nodes = relationship('OroWebCatalogContentNode', secondary='oro_web_catalog_node_slug_prot')
    nodes1 = relationship('OroWebCatalogContentNode', secondary='oro_web_catalog_node_title')
    nodes2 = relationship('OroWebCatalogContentNode', secondary='oro_web_catalog_node_url')
    menu_updates2 = relationship('OroCommerceMenuUpd', secondary='oro_commerce_menu_upd_title')
    menu_updates3 = relationship('OroCommerceMenuUpd', secondary='oro_commerce_menu_upd_descr')
    products = relationship('OroProduct', secondary='oro_product_slug_prototype')
    pages = relationship('OroCmsPage', secondary='oro_cms_page_slug_prototype')
    pages1 = relationship('OroCmsPage', secondary='oro_cms_page_title')
    transports = relationship('OroIntegrationTransport', secondary='oro_money_order_trans_label')
    transports1 = relationship('OroIntegrationTransport', secondary='oro_money_order_short_label')
    transports2 = relationship('OroIntegrationTransport', secondary='oro_payment_term_short_label')
    transports3 = relationship('OroIntegrationTransport', secondary='oro_payment_term_trans_label')
    transports4 = relationship('OroIntegrationTransport', secondary='oro_paypal_credit_card_lbl')
    transports5 = relationship('OroIntegrationTransport', secondary='oro_paypal_credit_card_sh_lbl')
    transports6 = relationship('OroIntegrationTransport', secondary='oro_paypal_xprss_chkt_lbl')
    transports7 = relationship('OroIntegrationTransport', secondary='oro_paypal_xprss_chkt_shrt_lbl')
    promotions = relationship('OroPromotion', secondary='oro_promotion_description')
    promotions1 = relationship('OroPromotion', secondary='oro_promotion_label')
    products1 = relationship('OroProduct', secondary='oro_rel_1cf73d3121a159ae2725f3')
    products2 = relationship('OroProduct', secondary='oro_rel_1cf73d3121a159ae6e1a29')
    pages2 = relationship('OroCmsPage', secondary='oro_rel_b438191e21a159aea3971e')
    pages3 = relationship('OroCmsPage', secondary='oro_rel_b438191e21a159ae2725f3')
    products3 = relationship('OroProduct', secondary='oro_rel_1cf73d3121a159aea3971e')
    pages4 = relationship('OroCmsPage', secondary='oro_rel_b438191e21a159ae6e1a29')
    transports8 = relationship('OroIntegrationTransport', secondary='oro_fedex_transport_label')
    transports9 = relationship('OroIntegrationTransport', secondary='oro_fixed_product_transp_label')
    transports10 = relationship('OroIntegrationTransport', secondary='oro_flat_rate_transport_label')
    transports11 = relationship('OroIntegrationTransport', secondary='oro_ups_transport_label')


