# coding: utf-8
from sqlalchemy import Column, Table, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BfmEventCode(Base):
    __tablename__ = 'bfm_event_code'

    event_code = Column(VARCHAR(255), primary_key=True)
    event_type = Column(VARCHAR(255), nullable=False, index=True)
    event_src_code = Column(VARCHAR(60), nullable=False, index=True)
    is_audit = Column(VARCHAR(60))
    comments = Column(VARCHAR(255))


t_global_bo_temp = Table(
    'global_bo_temp', metadata,
    Column('res_object_id', NUMBER(6, 0, False), nullable=False),
    Column('url', VARCHAR(120), nullable=False),
    Column('domain', VARCHAR(256), nullable=False),
    Column('json_path', VARCHAR(512), nullable=False)
)


class GlobalObject(Base):
    __tablename__ = 'global_object'

    id = Column(NUMBER(9, 0, False), primary_key=True)
    domain = Column(VARCHAR(255), nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    data_source = Column(VARCHAR(255))
    field_name = Column(VARCHAR(255))
