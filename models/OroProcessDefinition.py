from sqlalchemy import BigInteger, Boolean, CHAR, Column, Date, Float, ForeignKey, Index, Integer, JSON, LargeBinary, Numeric, SmallInteger, String, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, configure_mappers
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, TIME, UUID
from . import Base, metadata


class OroProcessDefinition(Base):
    __tablename__ = 'oro_process_definition'

    name = Column(String(255), primary_key=True)
    label = Column(String(255), nullable=False)
    enabled = Column(Boolean, nullable=False)
    related_entity = Column(String(255), nullable=False)
    execution_order = Column(SmallInteger, nullable=False)
    exclude_definitions = Column(Text, comment='(DC2Type:simple_array)(DC2Type:simple_array)')
    actions_configuration = Column(Text, nullable=False, comment='(DC2Type:array)(DC2Type:array)')
    created_at = Column(TIMESTAMP(precision=0), nullable=False)
    updated_at = Column(TIMESTAMP(precision=0), nullable=False)
    pre_conditions_configuration = Column(Text, comment='(DC2Type:array)(DC2Type:array)')


t_oro_prod_webs_reindex_req_item = Table(
    'oro_prod_webs_reindex_req_item', metadata,
    Column('related_job_id', Integer, nullable=False, index=True),
    Column('website_id', Integer, nullable=False),
    Column('product_id', Integer, nullable=False),
    Index('prod_webs_reindex_req_uniq_idx', 'product_id', 'related_job_id', 'website_id', unique=True)
)


