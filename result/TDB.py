# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 14:28
# @Author  : Fcvane
# @Param   : 
# @File    : TDB.py

# coding: utf-8
from sqlalchemy import CHAR, Column, TIMESTAMP, Index, VARCHAR, text
from sqlalchemy.dialects.postgresql import NUMERIC
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import QueuePool

Base = declarative_base()
metadata = Base.metadata


class RmeCard(Base):
    __tablename__ = 'rme_card'
    __table_args__ = (
        Index('idx_rme_card_codename', 'shortcode', 'shortname'),
    )

    card_id = Column(CHAR(24), primary_key=True)
    card_no = Column(VARCHAR(255), nullable=False, index=True)
    position = Column(NUMERIC(4, 0, False))
    speciality_id = Column(NUMERIC(8, 0, False))
    card_type_id = Column(NUMERIC(8, 0, False))
    card_model_id = Column(NUMERIC(18, 0, False))
    card_serial_no = Column(VARCHAR(20))
    port_count = Column(NUMERIC(4, 0, False))
    card_function = Column(VARCHAR(60))
    opr_state_id = Column(NUMERIC(8, 0, False))
    mnt_state_id = Column(NUMERIC(8, 0, False))
    hdwe_ver = Column(VARCHAR(50))
    sw_ver = Column(VARCHAR(50))
    work_style = Column(NUMERIC(8, 0, False))
    alias = Column(VARCHAR(255))
    notes = Column(VARCHAR(255))
    parent_id = Column(CHAR(24))
    delete_time = Column(TIMESTAMP)
    delete_state = Column(CHAR(1), server_default=text("'0'"))
    pos_x = Column(NUMERIC(8, 4, True))
    pos_y = Column(NUMERIC(8, 4, True))
    graph_width = Column(NUMERIC(8, 4, True))
    graph_height = Column(NUMERIC(8, 4, True))
    isoffset = Column(CHAR(1), server_default=text("null"))
    graph_id = Column(NUMERIC(12, 0, False))
    res_type_id = Column(NUMERIC(8, 0, False))
    motherboard_type = Column(VARCHAR(40))
    fault_info = Column(VARCHAR(100))
    card_name = Column(VARCHAR(255), index=True)
    super_card_id = Column(CHAR(24), index=True)
    card_rate = Column(NUMERIC(8, 0, False))
    module_no = Column(VARCHAR(40))
    modify_op = Column(NUMERIC(8, 0, False))
    modiry_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    asset_code = Column(VARCHAR(20))
    card_name_alias = Column(VARCHAR(120))
    card_nmno = Column(VARCHAR(120))
    is_direct_rack = Column(CHAR(1))
    rack_id = Column(CHAR(24))
    shortcode = Column(VARCHAR(255))
    shortname = Column(VARCHAR(255))
    templatename = Column(VARCHAR(255))
    istemplate = Column(NUMERIC(2, 0, False))
    roles = Column(NUMERIC(8, 0, False))
    longorlocal = Column(NUMERIC(2, 0, False))
    lx_no = Column(VARCHAR(255), index=True)
    sw_ver2 = Column(NUMERIC(8, 0, False))
    old_id_eqp = Column(NUMERIC(10, 0, False), index=True)
    old_sp = Column(VARCHAR(8))
    resource_from = Column(NUMERIC(8, 0, False))
    singlg_bind_ne = Column(CHAR(1), server_default=text("'0'"))
    port_idleness = Column(NUMERIC(5, 0, False))
    lan_id = Column(VARCHAR(10))
    create_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    create_op = Column(NUMERIC(8, 0, False))
    res_cover_area = Column(VARCHAR(255))
    location = Column(VARCHAR(255))
    support_prod_type = Column(NUMERIC(8, 0, False), index=True)
    pon_net_type = Column(NUMERIC(8, 0, False))
    standard_name = Column(VARCHAR(255))
    standard_code = Column(VARCHAR(255))
    is_recycled = Column(NUMERIC(8, 0, False))
    room_id = Column(CHAR(24))
    ems_orig_res_id = Column(VARCHAR(255), index=True)
    wo_id = Column(VARCHAR(24))
    eqp_id = Column(CHAR(24))
    nms_orig_res_id = Column(VARCHAR(255))
    nms_orig_res_name = Column(VARCHAR(255))
    ems_orig_res_name = Column(VARCHAR(255))
    auth_unit = Column(VARCHAR(100))
    cuteover_mark = Column(NUMERIC(8, 0, False))
    is_authorization = Column(NUMERIC(8, 0, False))
    is_fault = Column(NUMERIC(8, 0, False))
    is_importportect = Column(NUMERIC(8, 0, False))
    is_lock = Column(NUMERIC(8, 0, False))
    is_subcard = Column(NUMERIC(8, 0, False))
    life_cycle = Column(NUMERIC(8, 0, False))
    mainslot = Column(VARCHAR(40))
    material_no = Column(VARCHAR(80))
    subcard_sn = Column(NUMERIC(8, 0, False))
    super_res_name = Column(VARCHAR(255))
    third_mnt_unit = Column(VARCHAR(100))
    guarantee_time = Column(TIMESTAMP)
    mnt_life = Column(TIMESTAMP)
    renewal_time = Column(TIMESTAMP)
    life_cycle_time = Column(TIMESTAMP)
    flow_state_id = Column(NUMERIC(8, 0, False))
    name_suffix = Column(VARCHAR(255))
    p_res_no = Column(VARCHAR(255))
    p_res_id = Column(VARCHAR(255))
    nm_id = Column(VARCHAR(255))

from sqlalchemy import create_engine

db_url = 'postgresql://pgtest:abc123@172.21.86.201:5432/test'
# engine = create_engine('postgresql://pgtest:abc123@172.21.86.201:5432/test')
engine = create_engine(db_url, echo=True, pool_size=100, pool_recycle=3600, poolclass=QueuePool, max_overflow=10)
Base.metadata.create_all(engine)

# conn = engine.connect()
# result = conn.execute('select 1')
# print(result.fetchone())