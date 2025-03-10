from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmDmContact(Base):
    __tablename__ = 'orocrm_dm_contact'
    __table_args__ = (
        Index('orocrm_dm_cnt_em_unq', 'email', 'channel_id', unique=True),
        Index('orocrm_dm_contact_unq', 'origin_id', 'channel_id', unique=True)
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_dm_contact_id_seq'::regclass)"))
    owner_id = Column(ForeignKey('oro_organization.id', ondelete='SET NULL'), index=True)
    channel_id = Column(ForeignKey('oro_integration_channel.id', ondelete='SET NULL'), index=True)
    opt_in_type_id = Column(ForeignKey('oro_enum_dm_cnt_opt_in_type.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    email_type_id = Column(ForeignKey('oro_enum_dm_cnt_email_type.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    status_id = Column(ForeignKey('oro_enum_dm_cnt_status.id', ondelete='SET NULL'), index=True, server_default=text("NULL::character varying"))
    origin_id = Column(BigInteger)
    email = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    updated_at = Column(TIMESTAMP(precision=0), nullable=False, comment='(DC2Type:datetime)')
    unsubscribed_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    last_subscribed_date = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    data_fields = Column(JSON, comment='(DC2Type:json_array)(DC2Type:json_array)')
    serialized_data = Column(JSONB(astext_type=Text()))

    channel = relationship('OroIntegrationChannel')
    email_type = relationship('OroEnumDmCntEmailType')
    opt_in_type = relationship('OroEnumDmCntOptInType')
    owner = relationship('OroOrganization')
    status = relationship('OroEnumDmCntStatu')


