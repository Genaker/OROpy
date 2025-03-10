from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OrocrmZdComment(Base):
    __tablename__ = 'orocrm_zd_comment'
    __table_args__ = (
        Index('zd_comment_oid_cid_unq', 'origin_id', 'channel_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('orocrm_zd_comment_id_seq'::regclass)"))
    channel_id = Column(ForeignKey('oro_integration_channel.id', ondelete='CASCADE'), index=True)
    related_comment_id = Column(ForeignKey('orocrm_case_comment.id', ondelete='SET NULL'), unique=True)
    author_id = Column(ForeignKey('orocrm_zd_user.id', ondelete='SET NULL'), index=True)
    ticket_id = Column(ForeignKey('orocrm_zd_ticket.id', ondelete='SET NULL'), index=True)
    origin_id = Column(BigInteger)
    body = Column(Text)
    html_body = Column(Text)
    public = Column(Boolean, nullable=False, server_default=text("false"))
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    origin_created_at = Column(TIMESTAMP(precision=0), server_default=text("NULL::timestamp without time zone"))
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)

    author = relationship('OrocrmZdUser')
    channel = relationship('OroIntegrationChannel')
    related_comment = relationship('OrocrmCaseComment')
    ticket = relationship('OrocrmZdTicket')


t_orocrm_zd_ticket_collaborators = Table(
    'orocrm_zd_ticket_collaborators', metadata,
    Column('ticket_id', ForeignKey('orocrm_zd_ticket.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('user_id', ForeignKey('orocrm_zd_user.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


