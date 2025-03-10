from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroAttachmentFile(Base):
    __tablename__ = 'oro_attachment_file'

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_attachment_file_id_seq'::regclass)"))
    uuid = Column(UUID, index=True)
    file_size = Column(Integer)
    filename = Column(String(255), nullable=False)
    original_filename = Column(String(255), index=True, server_default=text("NULL::character varying"))
    extension = Column(String(10), server_default=text("NULL::character varying"))
    mime_type = Column(String(100), server_default=text("NULL::character varying"))
    parent_entity_class = Column(String(512), server_default=text("NULL::character varying"))
    parent_entity_id = Column(Integer)
    parent_entity_field_name = Column(String(50), server_default=text("NULL::character varying"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    external_url = Column(String(1024), server_default=text("NULL::character varying"))
    owner_user_id = Column(ForeignKey('oro_user.id', ondelete='SET NULL'), index=True)
    digitalasset_id = Column(ForeignKey('oro_digital_asset.id', ondelete='SET NULL'), index=True)
    serialized_data = Column(JSONB(astext_type=Text()))

    digitalasset = relationship('OroDigitalAsset', primaryjoin='OroAttachmentFile.digitalasset_id == OroDigitalAsset.id')
    owner_user = relationship('OroUser', primaryjoin='OroAttachmentFile.owner_user_id == OroUser.id')


