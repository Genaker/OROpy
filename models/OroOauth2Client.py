from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroOauth2Client(Base):
    __tablename__ = 'oro_oauth2_client'
    __table_args__ = (
        Index('oro_oauth2_client_owner_idx', 'owner_entity_class', 'owner_entity_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_oauth2_client_id_seq'::regclass)"))
    organization_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    name = Column(String(255), nullable=False)
    identifier = Column(String(32), nullable=False, unique=True)
    secret = Column(String(128), server_default=text("NULL::character varying"))
    salt = Column(String(50), nullable=False)
    grants = Column(Text, nullable=False, comment='(DC2Type:simple_array)(DC2Type:simple_array)')
    scopes = Column(Text, comment='(DC2Type:simple_array)(DC2Type:simple_array)')
    redirect_uris = Column(Text, comment='(DC2Type:simple_array)(DC2Type:simple_array)')
    active = Column(Boolean, nullable=False, server_default=text("true"))
    frontend = Column(Boolean, nullable=False, server_default=text("false"))
    owner_entity_class = Column(String(255), server_default=text("NULL::character varying"))
    owner_entity_id = Column(Integer)
    last_used_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"), comment='(DC2Type:datetime)')
    confidential = Column(Boolean, nullable=False, server_default=text("true"))
    plain_text_pkce_allowed = Column(Boolean, nullable=False, server_default=text("false"))
    skip_authorize_client_allowed = Column(Boolean, nullable=False, server_default=text("false"))

    organization = relationship('OroOrganization')


