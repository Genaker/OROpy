from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroCmsLoginPage(Base):
    __tablename__ = 'oro_cms_login_page'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_cms_login_page_id_seq'::regclass)"))
    top_content = Column(Text)
    bottom_content = Column(Text)
    css = Column(Text)
    logoimage_id = Column(ForeignKey('oro_attachment_file.id', ondelete='SET NULL'), index=True)
    backgroundimage_id = Column(ForeignKey('oro_attachment_file.id', ondelete='SET NULL'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    backgroundimage = relationship('OroAttachmentFile', primaryjoin='OroCmsLoginPage.backgroundimage_id == OroAttachmentFile.id')
    logoimage = relationship('OroAttachmentFile', primaryjoin='OroCmsLoginPage.logoimage_id == OroAttachmentFile.id')


