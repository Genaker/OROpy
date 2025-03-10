from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroAttributeGroupRel(Base):
    __tablename__ = 'oro_attribute_group_rel'
    __table_args__ = (
        Index('oro_attribute_group_uidx', 'entity_config_field_id', 'attribute_group_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('oro_attribute_group_rel_id_seq'::regclass)"))
    attribute_group_id = Column(ForeignKey('oro_attribute_group.id'), index=True)
    entity_config_field_id = Column(Integer, nullable=False)

    attribute_group = relationship('OroAttributeGroup')


