# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, Date, ForeignKey, Index, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BillChargeConfirmDetail(Base):
    __tablename__ = 'bill_charge_confirm_detail'

    confirm_detail_id = Column(INTEGER, primary_key=True)
    city_id = Column(String(24))
    year_month = Column(INTEGER)
    fee_type = Column(INTEGER)
    count_type = Column(INTEGER)
    fee = Column(DECIMAL(12, 4))
    send_time = Column(TIMESTAMP)
    tw_sign_time = Column(TIMESTAMP)
    telecom_sign_time = Column(TIMESTAMP)
    create_op = Column(INTEGER)
    create_time = Column(TIMESTAMP)
    modify_op = Column(INTEGER)
    modify_time = Column(TIMESTAMP)
    delete_state = Column(CHAR(1))
    delete_time = Column(TIMESTAMP)


t_mid_bill_confirm_list = Table(
    'mid_bill_confirm_list', metadata,
    Column('conf_list_id', CHAR(24), nullable=False),
    Column('year_month', INTEGER),
    Column('contract_id', CHAR(24)),
    Column('contract_no', String(200), index=True),
    Column('req_no', String(80)),
    Column('region_id', String(24)),
    Column('site_id', String(24)),
    Column('site_name', String(200)),
    Column('site_code', String(40)),
    Column('service_begin_time', TIMESTAMP),
    Column('confirm_state', INTEGER),
    Column('pro_type', INTEGER),
    Column('tw_rent_charge', DECIMAL(12, 4)),
    Column('site_fee', DECIMAL(12, 4)),
    Column('maintain_fee', DECIMAL(12, 4)),
    Column('elect_intro_fee', DECIMAL(12, 4)),
    Column('oilgenpower_fixed_charge', DECIMAL(12, 4)),
    Column('other_price', DECIMAL(12, 4)),
    Column('product_charge', DECIMAL(12, 4)),
    Column('adj_tw_rent_fee', DECIMAL(12, 4)),
    Column('adj_site_fee', DECIMAL(12, 4)),
    Column('adj_maintain_fee', DECIMAL(12, 4)),
    Column('adj_elect_intro_fee', DECIMAL(12, 4)),
    Column('adj_oil_pw_fixed_fee', DECIMAL(12, 4)),
    Column('adj_other_price', DECIMAL(12, 4)),
    Column('adjust_price', DECIMAL(12, 4)),
    Column('adjusted_tw_rent_fee', DECIMAL(12, 4)),
    Column('adjusted_site_fee', DECIMAL(12, 4)),
    Column('adjusted_maintain_fee', DECIMAL(12, 4)),
    Column('adjusted_elect_intro_fee', DECIMAL(12, 4)),
    Column('adjusted_oil_pw_fixed_fee', DECIMAL(12, 4)),
    Column('adjusted_other_price', DECIMAL(12, 4)),
    Column('adjusted_pro_price', DECIMAL(12, 4)),
    Column('adj_reason', Text),
    Column('oilgenpower_charge_ls', DECIMAL(12, 4)),
    Column('elec_ensure_fee', DECIMAL(12, 4)),
    Column('create_op', INTEGER),
    Column('create_time', TIMESTAMP),
    Column('modify_op', INTEGER),
    Column('modify_time', TIMESTAMP),
    Column('delete_state', CHAR(1)),
    Column('delete_time', TIMESTAMP),
    Column('province_id', CHAR(24)),
    Column('city_id', CHAR(24)),
    Column('tower_rent_charge', DECIMAL(12, 4)),
    Column('room_rent_charge', DECIMAL(12, 4)),
    Column('pt_rent_charge', DECIMAL(12, 4)),
    Column('wave_fee', DECIMAL(12, 4)),
    Column('wlan_fee', DECIMAL(12, 4)),
    Column('bbutower_fee', DECIMAL(12, 4)),
    Column('adj_tower_rent_charge', DECIMAL(12, 4)),
    Column('adj_room_rent_charge', DECIMAL(12, 4)),
    Column('adj_pt_rent_charge', DECIMAL(12, 4)),
    Column('adj_wave_fee', DECIMAL(12, 4)),
    Column('adj_wlan_fee', DECIMAL(12, 4)),
    Column('adj_bbutower_fee', DECIMAL(12, 4)),
    Column('adjusted_tower_rent_charge', DECIMAL(12, 4)),
    Column('adjusted_room_rent_charge', DECIMAL(12, 4)),
    Column('adjusted_pt_rent_charge', DECIMAL(12, 4)),
    Column('adjusted_wave_fee', DECIMAL(12, 4)),
    Column('adjusted_wlan_fee', DECIMAL(12, 4)),
    Column('adjusted_bbutower_fee', DECIMAL(12, 4)),
    Column('adjusted_non_oil_pw_fixed_fee', DECIMAL(12, 4)),
    Column('adjusted_elec_ensure_fee', DECIMAL(12, 4)),
    Column('company', INTEGER),
    Column('bill_type', INTEGER),
    Column('req_type', INTEGER),
    Column('company_city', CHAR(24)),
    Column('company_county', CHAR(24)),
    Column('req_city', CHAR(24)),
    Column('site_city', CHAR(24)),
    Column('high_class_service_fee', DECIMAL(12, 4)),
    Column('battery_ext_fee', DECIMAL(12, 4)),
    Column('adj_high_class_service_fee', DECIMAL(12, 4)),
    Column('adj_battery_ext_fee', DECIMAL(12, 4)),
    Column('adjusted_high_class_serv_fee', DECIMAL(12, 4)),
    Column('adjusted_battery_ext_fee', DECIMAL(12, 4)),
    Column('adj_oil_power_none_fixed_fee', DECIMAL(12, 4)),
    Column('adj_elec_ensure_fee', DECIMAL(12, 4)),
    Column('adj_prod_price', DECIMAL(12, 4)),
    Column('adj_terminal_of_amends', DECIMAL(14, 4)),
    Column('terminal_of_amends', DECIMAL(14, 4)),
    Column('adjusted_terminal_of_amends', DECIMAL(14, 4))
)


class MidGomPs2Wo(Base):
    __tablename__ = 'mid_gom_ps_2_wo_s'

    id = Column(String(24), primary_key=True)
    ord_ps_id = Column(String(50), nullable=False, index=True)
    tache_id = Column(String(50), nullable=False)
    dyn_tab_name = Column(String(50))
    disp_obj_type = Column(String(12), nullable=False)
    disp_obj_id = Column(String(20), nullable=False)
    req_time_long = Column(INTEGER)
    rec_state = Column(String(12), nullable=False)
    create_date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    state_date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    req_time_un = Column(String(12))
    can_mod_wo_disp = Column(INTEGER, server_default=text("210000002"))
    remark = Column(Text)
    net_grid_btn_ctl = Column(String(100))
    is_all_dispatch = Column(String(12), server_default=text("210000002"))
    oper_dyn_tab_name = Column(String(50))
    asyn_service_id = Column(String(12))
    url_flag = Column(String(100))
    chd_ord_ps_id = Column(INTEGER)
    chd_ord_process_ver = Column(INTEGER)
    chd_in_date = Column(TIMESTAMP)
    up_tran_id = Column(String(30))
    down_tran_id = Column(String(30))
    sou_ord_ps_id = Column(INTEGER)
    dom_tag_wo_ps_id = Column(INTEGER)
    disp_service_id = Column(INTEGER)
    sou_wo_ps_id = Column(INTEGER)
    sou_tache_id = Column(String(50))
    sou_ord_process_ver = Column(INTEGER)
    a_wo_ps_id = Column(INTEGER)
    a_tache_id = Column(String(50))
    a_ord_process_ver = Column(INTEGER)
    a_ord_ps_id = Column(INTEGER)


class MidGomWo(Base):
    __tablename__ = 'mid_gom_wo'
    __table_args__ = (
        Index('ind_mid_gom_wo_obj_type_id', 'disp_obj_tye', 'disp_obj_id'),
    )

    wo_id = Column(String(24), primary_key=True)
    order_id = Column(String(24), nullable=False, index=True)
    wiid = Column(String(50), nullable=False, index=True)
    wo_code = Column(String(50), index=True)
    wo_title = Column(String(100))
    old_wo_id = Column(INTEGER)
    remark = Column(Text)
    disp_obj_tye = Column(String(12))
    disp_obj_id = Column(INTEGER)
    disp_id = Column(INTEGER)
    cko_user_id = Column(INTEGER)
    comp_user_id = Column(INTEGER, index=True)
    wo_state = Column(String(12), nullable=False)
    create_date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    state_date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    req_fin_date = Column(TIMESTAMP, index=True)
    inner_state = Column(String(12))
    inner_state_date = Column(TIMESTAMP)
    kw_hd_qrr_id = Column(INTEGER)
    kw_hd_qrr_name = Column(String(50))
    alarm_date = Column(TIMESTAMP)
    ps_id = Column(CHAR(24), index=True)
    form_ver = Column(INTEGER)
    wo_type = Column(String(12))
    oper_form_ver = Column(INTEGER)
    wo_chg_disp_id = Column(INTEGER)
    is_ze_fan = Column(String(12))
    priv_forward_wo_id = Column(INTEGER)
    deal_date = Column(TIMESTAMP)
    deal_user_id = Column(INTEGER, index=True)
    priv_task_info = Column(String(80))
    virtual_order_id = Column(INTEGER)
    is_auto = Column(String(12))
    is_auto_fail = Column(String(12))
    had_forward_exec = Column(String(12))
    had_back_exec = Column(String(12))
    is_calling = Column(String(12))
    send_wo_id = Column(String(12))
    send_old_wo_id = Column(String(12))
    priv_task_id = Column(String(12))
    priv_task_type = Column(INTEGER)


t_mid_req_development = Table(
    'mid_req_development', metadata,
    Column('req_no', String(30)),
    Column('req_state', String(30)),
    Column('province', String(30)),
    Column('city', String(30)),
    Column('region', String(30)),
    Column('company', INTEGER),
    Column('pro_batch', String(80)),
    Column('req_name', String(100)),
    Column('scene_divide', INTEGER),
    Column('launch_time', TIMESTAMP),
    Column('delivery_time', TIMESTAMP),
    Column('receive_state_tt', INTEGER),
    Column('req_no_tt', String(30)),
    Column('site_code', String(30)),
    Column('site_name', Text),
    Column('is_share', CHAR(1)),
    Column('tower_type', INTEGER),
    Column('room_type', INTEGER),
    Column('build_type', INTEGER),
    Column('power_introduction_mode', INTEGER),
    Column('jf_workstarttime', TIMESTAMP),
    Column('jf_workendtime', TIMESTAMP),
    Column('jf_reality_delivertime', TIMESTAMP),
    Column('jf_check_time', TIMESTAMP),
    Column('create_date', TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
    Column('state', INTEGER, server_default=text("9680104")),
    Column('year_month', INTEGER, index=True),
    Column('offset_allow', DECIMAL(12, 3)),
    Column('notes', Text),
    Column('longitude', DECIMAL(20, 10)),
    Column('latitude', DECIMAL(20, 10)),
    Column('location', String(500)),
    Column('slot_num', DECIMAL(12, 3)),
    Column('antenna_high_l', DECIMAL(12, 3)),
    Column('antenna_high_h', DECIMAL(12, 3)),
    Column('deviation_radius', DECIMAL(20, 3)),
    Column('antenna_count', DECIMAL(12, 3)),
    Column('screen_confirm_is_success', CHAR(1)),
    Column('screen_confirm_fail_reason', String(200)),
    Column('transfer_type', INTEGER),
    Column('cust_count_old', DECIMAL(20, 3)),
    Column('cust_detail_old', DECIMAL(20, 3)),
    Column('cust_count_new', DECIMAL(20, 3)),
    Column('cust_detail_new', DECIMAL(20, 3)),
    Column('tower_type_detail', INTEGER),
    Column('tower_high', DECIMAL(12, 3)),
    Column('platform_count', DECIMAL(12, 3)),
    Column('seat_count', DECIMAL(12, 3)),
    Column('system_count', DECIMAL(12, 3)),
    Column('bbu_count', DECIMAL(12, 3)),
    Column('rru_count', DECIMAL(12, 3)),
    Column('rru_power_mode', INTEGER),
    Column('a_battery_protection_time', DECIMAL(20, 3)),
    Column('a_wind_pressure', INTEGER),
    Column('a_is_oil_power', CHAR(1)),
    Column('a_customer_power', String(80)),
    Column('a_microwave_count', DECIMAL(12, 3)),
    Column('a_microwave_high', DECIMAL(12, 3)),
    Column('a_wlan_antenna_count', DECIMAL(12, 3)),
    Column('a_wlan_antenna_high', DECIMAL(12, 3)),
    Column('a_product_config', INTEGER),
    Column('product_name1', String(128)),
    Column('product_name2', String(128)),
    Column('product_name3', String(128)),
    Column('product_antenna_high_1', DECIMAL(12, 3)),
    Column('product_antenna_high_2', DECIMAL(12, 3)),
    Column('product_antenna_high_3', DECIMAL(12, 3)),
    Column('product_antenna_count1', DECIMAL(12, 3)),
    Column('product_antenna_count2', DECIMAL(12, 3)),
    Column('product_antenna_count3', DECIMAL(12, 3)),
    Column('product_rru1', CHAR(1)),
    Column('product_rru2', CHAR(1)),
    Column('product_rru3', CHAR(1)),
    Column('product_rru_in_room1', CHAR(1)),
    Column('product_rru_in_room2', CHAR(1)),
    Column('product_rru_in_room3', CHAR(1)),
    Column('bill_type', INTEGER)
)


class MidRidDeliveryTower(Base):
    __tablename__ = 'mid_rid_delivery_tower'

    delivery_id = Column(CHAR(24), primary_key=True)
    version = Column(INTEGER, nullable=False)
    notes = Column(Text)
    state = Column(CHAR(1))
    province = Column(String(24))
    city = Column(String(24))
    region = Column(String(24))
    company = Column(INTEGER)
    req_no = Column(String(80))
    req_no_tt = Column(String(80))
    order_instance_no = Column(String(80))
    business_state = Column(INTEGER)
    jf_project_name = Column(String(200))
    jf_customer_name = Column(String(100))
    jf_build_company = Column(String(100))
    jf_design_company = Column(String(500))
    jf_construction_company = Column(String(100))
    jf_supervisor_comp = Column(String(100))
    jf_workaddress = Column(Text)
    jf_workstarttime = Column(TIMESTAMP)
    jf_workendtime = Column(TIMESTAMP)
    jf_reality_delivertime = Column(TIMESTAMP)
    jf_check_time = Column(TIMESTAMP)
    sc_dyjbtj = Column(INTEGER)
    sc_site_loc_qk = Column(INTEGER)
    sc_hang_scope = Column(INTEGER)
    sc_yddcrl = Column(INTEGER)
    sc_jws = Column(INTEGER)
    sc_ktaz = Column(INTEGER)
    wtjjbf = Column(String(200))
    supervisor = Column(String(80))
    supervisor_confirm_time = Column(TIMESTAMP)
    ys_checkreuslt = Column(INTEGER)
    ys_tdgsfzr = Column(String(100))
    ys_check_people = Column(String(100))
    ys_checktime = Column(TIMESTAMP)
    ys_check_launch_man = Column(String(100))
    ys_check_launch_time = Column(TIMESTAMP)
    ys_check_real_man_tt = Column(String(100))
    ys_check_real_info = Column(String(100))
    ys_check_notification_time = Column(TIMESTAMP)
    ys_check_confirm_man = Column(String(100))
    ys_check_confirm_time = Column(String(100))
    approval_opinion = Column(CHAR(1))
    approval_opinion_desc = Column(String(200))
    approval_op = Column(INTEGER)
    approval_op_name = Column(String(200))
    approval_time = Column(TIMESTAMP)
    create_op = Column(INTEGER)
    create_time = Column(TIMESTAMP)
    modify_op = Column(INTEGER)
    modify_time = Column(TIMESTAMP)
    delete_op = Column(INTEGER)
    delete_time = Column(TIMESTAMP)


class MidRidDeliveryTowerArc(Base):
    __tablename__ = 'mid_rid_delivery_tower_arc'

    delivery_id = Column(CHAR(24), primary_key=True)
    version = Column(INTEGER, nullable=False)
    notes = Column(Text)
    state = Column(CHAR(1))
    province = Column(String(24))
    city = Column(String(24))
    region = Column(String(24))
    company = Column(INTEGER)
    req_no = Column(String(80))
    req_no_tt = Column(String(80))
    order_instance_no = Column(String(80))
    business_state = Column(INTEGER)
    jf_project_name = Column(String(200))
    jf_customer_name = Column(String(100))
    jf_build_company = Column(String(100))
    jf_design_company = Column(String(500))
    jf_construction_company = Column(String(100))
    jf_supervisor_comp = Column(String(100))
    jf_workaddress = Column(Text)
    jf_workstarttime = Column(TIMESTAMP)
    jf_workendtime = Column(TIMESTAMP)
    jf_reality_delivertime = Column(TIMESTAMP)
    jf_check_time = Column(TIMESTAMP)
    sc_dyjbtj = Column(INTEGER)
    sc_site_loc_qk = Column(INTEGER)
    sc_hang_scope = Column(INTEGER)
    sc_yddcrl = Column(INTEGER)
    sc_jws = Column(INTEGER)
    sc_ktaz = Column(INTEGER)
    wtjjbf = Column(String(200))
    supervisor = Column(String(80))
    supervisor_confirm_time = Column(TIMESTAMP)
    ys_checkreuslt = Column(INTEGER)
    ys_tdgsfzr = Column(String(100))
    ys_check_people = Column(String(100))
    ys_checktime = Column(TIMESTAMP)
    ys_check_launch_man = Column(String(100))
    ys_check_launch_time = Column(TIMESTAMP)
    ys_check_real_man_tt = Column(String(100))
    ys_check_real_info = Column(String(100))
    ys_check_notification_time = Column(TIMESTAMP)
    ys_check_confirm_man = Column(String(100))
    ys_check_confirm_time = Column(String(100))
    approval_opinion = Column(CHAR(1))
    approval_opinion_desc = Column(String(200))
    approval_op = Column(INTEGER)
    approval_op_name = Column(String(200))
    approval_time = Column(TIMESTAMP)
    create_op = Column(INTEGER)
    create_time = Column(TIMESTAMP)
    modify_op = Column(INTEGER)
    modify_time = Column(TIMESTAMP)
    delete_op = Column(INTEGER)
    delete_time = Column(TIMESTAMP)
    arc_time = Column(TIMESTAMP)
    arc_op = Column(String(200))


class MidRidOrderInstance(Base):
    __tablename__ = 'mid_rid_order_instance'

    order_instance_id = Column(CHAR(24), primary_key=True)
    version = Column(INTEGER, nullable=False)
    order_instance_no = Column(String(80))
    state = Column(CHAR(1))
    business_state = Column(INTEGER)
    province = Column(String(24))
    city = Column(String(24))
    region = Column(String(24))
    company = Column(INTEGER)
    req_no = Column(String(80))
    req_no_tt = Column(String(80))
    site_code = Column(String(80))
    site_name = Column(Text)
    is_share = Column(CHAR(1))
    scene_divide = Column(INTEGER)
    longitude = Column(DECIMAL(20, 10))
    latitude = Column(DECIMAL(20, 10))
    location = Column(String(500))
    slot_num = Column(DECIMAL(12, 3))
    antenna_high_l = Column(DECIMAL(12, 3))
    antenna_high_h = Column(DECIMAL(12, 3))
    antenna_direction = Column(DECIMAL(12, 3))
    deviation_radius = Column(DECIMAL(20, 3))
    antenna_count = Column(DECIMAL(12, 3))
    tower_type = Column(INTEGER)
    room_type = Column(INTEGER)
    build_type = Column(INTEGER)
    service_level = Column(INTEGER)
    screen_confirm_is_success = Column(CHAR(1))
    screen_confirm_fail_reason = Column(String(200))
    transfer_type = Column(INTEGER)
    power_introduction_mode = Column(INTEGER)
    cust_count_old = Column(DECIMAL(20, 3))
    cust_detail_old = Column(DECIMAL(20, 3))
    cust_count_new = Column(DECIMAL(20, 3))
    cust_detail_new = Column(DECIMAL(20, 3))
    tower_type_detail = Column(INTEGER)
    tower_high = Column(DECIMAL(12, 3))
    platform_count = Column(DECIMAL(12, 3))
    seat_count = Column(DECIMAL(12, 3))
    system_count = Column(DECIMAL(12, 3))
    bbu_count = Column(DECIMAL(12, 3))
    rru_count = Column(DECIMAL(12, 3))
    rru_power_mode = Column(INTEGER)
    a_power_introduction_mode = Column(INTEGER)
    a_battery_protection_time = Column(DECIMAL(20, 3))
    a_wind_pressure = Column(INTEGER)
    a_is_oil_power = Column(CHAR(1))
    a_customer_power = Column(String(80))
    a_microwave_count = Column(DECIMAL(12, 3))
    a_microwave_high = Column(DECIMAL(12, 3))
    a_wlan_antenna_count = Column(DECIMAL(12, 3))
    a_wlan_antenna_high = Column(DECIMAL(12, 3))
    a_product_config = Column(INTEGER)
    a_product_type = Column(String(128))
    product_name1 = Column(String(128))
    product_name2 = Column(String(128))
    product_name3 = Column(String(128))
    product_unit_count1 = Column(DECIMAL(12, 3))
    product_unit_count2 = Column(DECIMAL(12, 3))
    product_unit_count3 = Column(DECIMAL(12, 3))
    product_antenna_high_1 = Column(DECIMAL(12, 3))
    product_antenna_high_2 = Column(DECIMAL(12, 3))
    product_antenna_high_3 = Column(DECIMAL(12, 3))
    product_antenna_count1 = Column(DECIMAL(12, 3))
    product_antenna_count2 = Column(DECIMAL(12, 3))
    product_antenna_count3 = Column(DECIMAL(12, 3))
    product_system_count1 = Column(DECIMAL(12, 3))
    product_system_count2 = Column(DECIMAL(12, 3))
    product_system_count3 = Column(DECIMAL(12, 3))
    product_rru1 = Column(CHAR(1))
    product_rru2 = Column(CHAR(1))
    product_rru3 = Column(CHAR(1))
    product_rru_in_room1 = Column(CHAR(1))
    product_rru_in_room2 = Column(CHAR(1))
    product_rru_in_room3 = Column(CHAR(1))
    product_rru_servie_charge1 = Column(DECIMAL(12, 3))
    product_rru_servie_charge2 = Column(DECIMAL(12, 3))
    product_rru_servie_charge3 = Column(DECIMAL(12, 3))
    launch_man = Column(String(80))
    launch_time = Column(TIMESTAMP)
    approval_opinion = Column(CHAR(1))
    approval_opinion_desc = Column(String(200))
    approval_op = Column(INTEGER)
    approval_op_name = Column(String(200))
    approval_time = Column(TIMESTAMP)
    create_op = Column(INTEGER)
    create_time = Column(TIMESTAMP)
    modify_op = Column(INTEGER)
    modify_time = Column(TIMESTAMP)
    delete_op = Column(INTEGER)
    delete_time = Column(TIMESTAMP)
    building_type = Column(INTEGER)
    cover_area = Column(String(10))
    bbu_power = Column(String(20))
    rru_power = Column(String(20))
    tranfer_power = Column(String(20))
    tranfer_high = Column(String(20))
    system_type = Column(String(80))
    band = Column(String(80))
    poi_min_rate = Column(String(20))
    combiner_type = Column(String(20))
    combiner_port_num = Column(String(20))
    is_twinchannel = Column(String(20))
    combiner_min_rate = Column(String(200))
    extra_protection_time = Column(String(20))
    is_special = Column(String(20))
    all_power = Column(String(20))
    cabe_length = Column(String(10))
    tunnel_length = Column(String(10))
    project_name = Column(String(100))
    tunnel_longitude = Column(DECIMAL(20, 6))
    tunnel_latitude = Column(DECIMAL(20, 6))
    tunnel_bigin_point = Column(Text)
    tunnel_end_point = Column(Text)
    tunnel_rout = Column(Text)
    tunnel_built_type = Column(String(100))
    optical_longitude = Column(DECIMAL(20, 10))
    optical_latitude = Column(DECIMAL(20, 10))
    optical_bigin_point = Column(Text)
    optical_end_point = Column(Text)
    optical_built_type = Column(Text)
    optical_length = Column(String(100))
    pole_longitude = Column(DECIMAL(20, 6))
    pole_latitude = Column(DECIMAL(20, 6))
    pole_bigin_point = Column(Text)
    pole_end_point = Column(Text)
    pole_length = Column(String(100))
    remark = Column(Text)
    pt_type = Column(INTEGER)
    order_confirm_time = Column(TIMESTAMP)


class MidRidOrderInstanceArc(Base):
    __tablename__ = 'mid_rid_order_instance_arc'

    order_instance_id = Column(CHAR(24), primary_key=True)
    version = Column(INTEGER, nullable=False)
    order_instance_no = Column(String(80))
    state = Column(CHAR(1))
    business_state = Column(INTEGER)
    province = Column(String(24))
    city = Column(String(24))
    region = Column(String(24))
    company = Column(INTEGER)
    req_no = Column(String(80))
    req_no_tt = Column(String(80))
    site_code = Column(String(80))
    site_name = Column(Text)
    is_share = Column(CHAR(1))
    scene_divide = Column(INTEGER)
    longitude = Column(DECIMAL(20, 10))
    latitude = Column(DECIMAL(20, 10))
    location = Column(String(500))
    slot_num = Column(DECIMAL(12, 3))
    antenna_high_l = Column(DECIMAL(12, 3))
    antenna_high_h = Column(DECIMAL(12, 3))
    antenna_direction = Column(DECIMAL(12, 3))
    deviation_radius = Column(DECIMAL(20, 3))
    antenna_count = Column(DECIMAL(12, 3))
    tower_type = Column(INTEGER)
    room_type = Column(INTEGER)
    build_type = Column(INTEGER)
    service_level = Column(INTEGER)
    screen_confirm_is_success = Column(CHAR(1))
    screen_confirm_fail_reason = Column(String(200))
    transfer_type = Column(INTEGER)
    power_introduction_mode = Column(INTEGER)
    cust_count_old = Column(DECIMAL(20, 3))
    cust_detail_old = Column(DECIMAL(20, 3))
    cust_count_new = Column(DECIMAL(20, 3))
    cust_detail_new = Column(DECIMAL(20, 3))
    tower_type_detail = Column(INTEGER)
    tower_high = Column(DECIMAL(12, 3))
    platform_count = Column(DECIMAL(12, 3))
    seat_count = Column(DECIMAL(12, 3))
    system_count = Column(DECIMAL(12, 3))
    bbu_count = Column(DECIMAL(12, 3))
    rru_count = Column(DECIMAL(12, 3))
    rru_power_mode = Column(INTEGER)
    a_power_introduction_mode = Column(INTEGER)
    a_battery_protection_time = Column(DECIMAL(20, 3))
    a_wind_pressure = Column(INTEGER)
    a_is_oil_power = Column(CHAR(1))
    a_customer_power = Column(String(80))
    a_microwave_count = Column(DECIMAL(12, 3))
    a_microwave_high = Column(DECIMAL(12, 3))
    a_wlan_antenna_count = Column(DECIMAL(12, 3))
    a_wlan_antenna_high = Column(DECIMAL(12, 3))
    a_product_config = Column(INTEGER)
    a_product_type = Column(String(128))
    product_name1 = Column(String(128))
    product_name2 = Column(String(128))
    product_name3 = Column(String(128))
    product_unit_count1 = Column(DECIMAL(12, 3))
    product_unit_count2 = Column(DECIMAL(12, 3))
    product_unit_count3 = Column(DECIMAL(12, 3))
    product_antenna_high_1 = Column(DECIMAL(12, 3))
    product_antenna_high_2 = Column(DECIMAL(12, 3))
    product_antenna_high_3 = Column(DECIMAL(12, 3))
    product_antenna_count1 = Column(DECIMAL(12, 3))
    product_antenna_count2 = Column(DECIMAL(12, 3))
    product_antenna_count3 = Column(DECIMAL(12, 3))
    product_system_count1 = Column(DECIMAL(12, 3))
    product_system_count2 = Column(DECIMAL(12, 3))
    product_system_count3 = Column(DECIMAL(12, 3))
    product_rru1 = Column(CHAR(1))
    product_rru2 = Column(CHAR(1))
    product_rru3 = Column(CHAR(1))
    product_rru_in_room1 = Column(CHAR(1))
    product_rru_in_room2 = Column(CHAR(1))
    product_rru_in_room3 = Column(CHAR(1))
    product_rru_servie_charge1 = Column(DECIMAL(12, 3))
    product_rru_servie_charge2 = Column(DECIMAL(12, 3))
    product_rru_servie_charge3 = Column(DECIMAL(12, 3))
    launch_man = Column(String(80))
    launch_time = Column(TIMESTAMP)
    approval_opinion = Column(CHAR(1))
    approval_opinion_desc = Column(String(200))
    approval_op = Column(INTEGER)
    approval_op_name = Column(String(200))
    approval_time = Column(TIMESTAMP)
    create_op = Column(INTEGER)
    create_time = Column(TIMESTAMP)
    modify_op = Column(INTEGER)
    modify_time = Column(TIMESTAMP)
    delete_op = Column(INTEGER)
    delete_time = Column(TIMESTAMP)
    arc_time = Column(TIMESTAMP)
    arc_op = Column(String(200))
    building_type = Column(INTEGER)
    cover_area = Column(String(10))
    bbu_power = Column(String(20))
    rru_power = Column(String(20))
    tranfer_power = Column(String(20))
    tranfer_high = Column(String(20))
    system_type = Column(String(80))
    band = Column(String(80))
    poi_min_rate = Column(String(20))
    combiner_type = Column(String(20))
    combiner_port_num = Column(String(20))
    is_twinchannel = Column(String(20))
    combiner_min_rate = Column(String(200))
    extra_protection_time = Column(String(20))
    is_special = Column(String(20))
    all_power = Column(String(20))
    cabe_length = Column(String(10))
    tunnel_length = Column(String(10))
    project_name = Column(String(100))
    tunnel_longitude = Column(DECIMAL(20, 6))
    tunnel_latitude = Column(DECIMAL(20, 6))
    tunnel_bigin_point = Column(Text)
    tunnel_end_point = Column(Text)
    tunnel_rout = Column(Text)
    tunnel_built_type = Column(String(100))
    optical_longitude = Column(DECIMAL(20, 10))
    optical_latitude = Column(DECIMAL(20, 10))
    optical_bigin_point = Column(Text)
    optical_end_point = Column(Text)
    optical_built_type = Column(Text)
    optical_length = Column(String(100))
    pole_longitude = Column(DECIMAL(20, 6))
    pole_latitude = Column(DECIMAL(20, 6))
    pole_bigin_point = Column(Text)
    pole_end_point = Column(Text)
    pole_length = Column(String(100))
    remark = Column(Text)
    pt_type = Column(INTEGER)
    order_confirm_time = Column(TIMESTAMP)


class MidRidRentContract(Base):
    __tablename__ = 'mid_rid_rent_contract'
    __table_args__ = (
        Index('index_rid_rent_id_no', 'contract_id', 'contract_no'),
    )

    contract_id = Column(CHAR(24), primary_key=True, nullable=False, index=True)
    contract_no = Column(String(200), index=True)
    product_type = Column(INTEGER)
    contract_type = Column(INTEGER)
    company = Column(INTEGER)
    rent_state = Column(INTEGER, index=True)
    req_no = Column(String(80))
    region_id = Column(String(24))
    service_begin_date = Column(TIMESTAMP)
    service_end_date = Column(TIMESTAMP)
    station_id = Column(String(24))
    spare_baterry = Column(DECIMAL(8, 2))
    elec_service_mode = Column(INTEGER)
    elec_ensure_fee = Column(DECIMAL(12, 4))
    other_fee = Column(DECIMAL(12, 4))
    other_fee_notes = Column(String(400))
    mnt_discount = Column(DECIMAL(4, 2))
    mnt_fee = Column(DECIMAL(12, 4))
    field_fee = Column(DECIMAL(12, 4))
    field_discount = Column(DECIMAL(4, 2))
    product_service_fee_tax = Column(DECIMAL(12, 4))
    product_service_fee = Column(DECIMAL(12, 4))
    create_time = Column(TIMESTAMP)
    create_op = Column(INTEGER)
    modify_time = Column(TIMESTAMP)
    modify_op = Column(INTEGER)
    delete_time = Column(TIMESTAMP)
    delete_state = Column(CHAR(1), server_default=text("'0'"))
    county_id = Column(String(24))
    latitude = Column(DECIMAL(20, 10))
    prov_id = Column(String(24))
    city_id = Column(String(24))
    company_city_id = Column(String(24))
    req_city_id = Column(String(24))
    scene = Column(INTEGER)
    siteaddress_code = Column(String(255), index=True)
    siteaddress_name = Column(String(255))
    siteaddress_address = Column(String(500))
    longitude = Column(String(64))
    is_stand_bld_cost = Column(CHAR(1))
    contract_initiator = Column(INTEGER)
    contract_initia_date = Column(TIMESTAMP)
    field_fee_mode = Column(INTEGER)
    notes1 = Column(String(255))
    notes2 = Column(String(255))
    notes3 = Column(String(255))
    off_hire_date = Column(TIMESTAMP)
    delete_op = Column(INTEGER)
    year_month = Column(INTEGER, primary_key=True, nullable=False)
    basis_mode = Column(INTEGER)
    other_maintenance_fee = Column(DECIMAL(12, 4))
    site_share_info = Column(INTEGER)
    other_site_rent = Column(DECIMAL(12, 4))
    site_rent_is_share = Column(INTEGER)
    field_share_info = Column(INTEGER)
    request_source = Column(INTEGER)
    maint_is_share = Column(INTEGER)
    is_expired = Column(CHAR(1), server_default=text("'0'"))


class MidRidRentContractTw(Base):
    __tablename__ = 'mid_rid_rent_contract_tw'

    contract_id = Column(CHAR(24), primary_key=True)
    share_info = Column(INTEGER)
    tw_cur_cust_num = Column(INTEGER)
    room_cur_cust_num = Column(INTEGER)
    match_cust_num = Column(INTEGER)
    product_config = Column(String(400))
    tw_type = Column(INTEGER)
    room_config = Column(INTEGER)
    maintain_level = Column(INTEGER)
    is_have_elec = Column(INTEGER)
    is_choose_elec = Column(INTEGER)
    oilgenpower_charge_mode = Column(INTEGER)
    oilgenpower_charge_year = Column(DECIMAL(12, 4))
    high_class_service_fee = Column(DECIMAL(12, 4))
    tw_base_price = Column(DECIMAL(12, 4))
    room_base_price = Column(DECIMAL(12, 4))
    tw_discount = Column(DECIMAL(4, 2))
    room_discount = Column(DECIMAL(4, 2))
    match_discount = Column(DECIMAL(4, 2))
    battery_ext_fee = Column(DECIMAL(12, 4))
    elec_in_discount = Column(DECIMAL(4, 2))
    elec_in_fee = Column(DECIMAL(12, 4))
    create_time = Column(TIMESTAMP)
    create_op = Column(INTEGER)
    modify_time = Column(TIMESTAMP)
    modify_op = Column(INTEGER)
    delete_time = Column(TIMESTAMP)
    delete_state = Column(CHAR(1), server_default=text("'0'"))
    wind_pressure = Column(DECIMAL(12, 3))
    pro_unit_num1 = Column(DECIMAL(6, 2))
    antenna_height1 = Column(DECIMAL(12, 4))
    antenna_num1 = Column(INTEGER)
    sys_num1 = Column(INTEGER)
    bbutower_charge_year1 = Column(DECIMAL(12, 4))
    pro_unit_num2 = Column(DECIMAL(6, 2))
    antenna_height2 = Column(DECIMAL(12, 4))
    antenna_num2 = Column(INTEGER)
    sys_num2 = Column(INTEGER)
    bbutower_charge_year2 = Column(DECIMAL(12, 4))
    pro_unit_num3 = Column(DECIMAL(6, 2))
    antenna_height3 = Column(DECIMAL(12, 4))
    antenna_num3 = Column(INTEGER)
    sys_num3 = Column(INTEGER)
    is_bbu_in_room3 = Column(CHAR(1))
    is_rru_on_stand3 = Column(CHAR(1))
    bbutower_charge_year3 = Column(DECIMAL(12, 4))
    tw_share_user_bdate1 = Column(TIMESTAMP)
    tw_share_user_edate1 = Column(TIMESTAMP)
    tw_share_user_bdate2 = Column(TIMESTAMP)
    tw_share_user_edate2 = Column(TIMESTAMP)
    room_cust_bdate1 = Column(TIMESTAMP)
    room_cust_edate1 = Column(TIMESTAMP)
    room_cust_bdate2 = Column(TIMESTAMP)
    room_cust_edate2 = Column(TIMESTAMP)
    match_cust_bdate1 = Column(TIMESTAMP)
    match_cust_edate1 = Column(TIMESTAMP)
    match_cust_bdate2 = Column(TIMESTAMP)
    match_cust_edate2 = Column(TIMESTAMP)
    mnt_fee_cust_bdate1 = Column(TIMESTAMP)
    mnt_fee_cust_edate1 = Column(TIMESTAMP)
    mnt_fee_cust_bdate2 = Column(TIMESTAMP)
    mnt_fee_cust_edate2 = Column(TIMESTAMP)
    field_fee_cust_bdate1 = Column(TIMESTAMP)
    field_fee_cust_edate1 = Column(TIMESTAMP)
    field_fee_cust_bdate2 = Column(TIMESTAMP)
    field_fee_cust_edate2 = Column(TIMESTAMP)
    elec_in_disc_cust_bdate1 = Column(TIMESTAMP)
    elec_in_disc_cust_edate1 = Column(TIMESTAMP)
    elec_in_disc_cust_bdate2 = Column(TIMESTAMP)
    elec_in_disc_cust_edate2 = Column(TIMESTAMP)
    tw_build_price = Column(DECIMAL(12, 4))
    room_build_price = Column(DECIMAL(12, 4))
    match_build_price = Column(DECIMAL(12, 4))
    match_base_price = Column(DECIMAL(12, 4))
    is_rru_discount = Column(CHAR(1))
    wlan_service_fee = Column(DECIMAL(12, 4))
    wave_service_fee = Column(DECIMAL(12, 4))
    tw_service_fee = Column(DECIMAL(12, 4))
    tw_height = Column(DECIMAL(12, 4))
    elec_in_fee_mode = Column(INTEGER)
    mnt_fee_cust_num = Column(INTEGER)
    field_fee_cust_num = Column(INTEGER)
    elec_in_disc_cust_num = Column(INTEGER)
    is_bbu_in_room1 = Column(CHAR(1))
    is_rru_on_stand1 = Column(CHAR(1))
    is_bbu_in_room2 = Column(CHAR(1))
    is_rru_on_stand2 = Column(CHAR(1))
    is_06upsite = Column(INTEGER)
    room_share_info = Column(INTEGER)
    year_month = Column(INTEGER)
    other_elec_in_fee = Column(DECIMAL(12, 4))
    elec_in_fee_is_share = Column(INTEGER)
    guarantee_count = Column(INTEGER)
    guarantee_time = Column(INTEGER)
    micro_discount = Column(DECIMAL(10, 2))
    wlanap_discount = Column(DECIMAL(10, 2))
    micro_antenna_num = Column(INTEGER)
    micro_antenna_height = Column(INTEGER)
    wlanap_num = Column(INTEGER)
    wlanap_height = Column(INTEGER)
    pt_share_info = Column(INTEGER)
    pt_config = Column(INTEGER)


class MidRidReq(Base):
    __tablename__ = 'mid_rid_req'

    req_id = Column(CHAR(24), primary_key=True)
    version = Column(INTEGER, nullable=False)
    req_no = Column(String(80))
    req_no_tt = Column(String(80))
    req_type = Column(INTEGER)
    req_name = Column(String(80))
    req_desc = Column(String(200))
    province = Column(String(24))
    city = Column(String(24))
    region = Column(String(24))
    pro_batch = Column(String(80))
    delivery_time = Column(TIMESTAMP)
    company = Column(INTEGER)
    site_code = Column(String(80))
    site_name = Column(Text)
    longitude = Column(DECIMAL(20, 10))
    latitude = Column(DECIMAL(20, 10))
    location = Column(String(200))
    launch_man = Column(INTEGER)
    launch_time = Column(TIMESTAMP)
    rel_tel = Column(String(200))
    project_site = Column(String(80))
    notes = Column(Text)
    create_op = Column(INTEGER)
    create_time = Column(TIMESTAMP)
    modify_op = Column(INTEGER)
    modify_time = Column(TIMESTAMP)
    modify_desc = Column(Text)
    delete_reason = Column(INTEGER)
    delete_op = Column(INTEGER)
    delete_time = Column(TIMESTAMP)
    delete_desc = Column(Text)
    file_name = Column(Text)
    state = Column(CHAR(1))
    business_state = Column(INTEGER)
    approval_opinion = Column(CHAR(1))
    approval_opinion_desc = Column(String(200))
    approval_op = Column(INTEGER)
    approval_op_name = Column(String(200))
    approval_time = Column(TIMESTAMP)
    commit_tt_success = Column(CHAR(1))
    commit_tt_fail_reson = Column(String(200))
    receive_state_tt = Column(INTEGER)
    return_reson_tt = Column(String(200))
    receive_man = Column(String(200))
    receive_time = Column(TIMESTAMP)
    flow_order_id = Column(CHAR(24))
    deal_opinion_desc = Column(String(200))


class MidRidReqArc(Base):
    __tablename__ = 'mid_rid_req_arc'

    req_id = Column(CHAR(24), primary_key=True)
    version = Column(INTEGER, nullable=False)
    req_no = Column(String(80))
    req_no_tt = Column(String(80))
    req_type = Column(INTEGER)
    req_name = Column(String(80))
    req_desc = Column(String(200))
    province = Column(String(24))
    city = Column(String(24))
    region = Column(String(24))
    pro_batch = Column(String(80))
    delivery_time = Column(TIMESTAMP)
    company = Column(INTEGER)
    site_code = Column(String(80))
    site_name = Column(Text)
    longitude = Column(DECIMAL(20, 10))
    latitude = Column(DECIMAL(20, 10))
    location = Column(String(200))
    launch_man = Column(INTEGER)
    launch_time = Column(TIMESTAMP)
    rel_tel = Column(String(200))
    project_site = Column(String(80))
    notes = Column(Text)
    create_op = Column(INTEGER)
    create_time = Column(TIMESTAMP)
    modify_op = Column(INTEGER)
    modify_time = Column(TIMESTAMP)
    modify_desc = Column(Text)
    delete_reason = Column(INTEGER)
    delete_op = Column(INTEGER)
    delete_time = Column(TIMESTAMP)
    delete_desc = Column(Text)
    file_name = Column(Text)
    state = Column(CHAR(1))
    business_state = Column(INTEGER)
    approval_opinion = Column(CHAR(1))
    approval_opinion_desc = Column(String(200))
    approval_op = Column(INTEGER)
    approval_op_name = Column(String(200))
    approval_time = Column(TIMESTAMP)
    commit_tt_success = Column(CHAR(1))
    commit_tt_fail_reson = Column(String(200))
    receive_state_tt = Column(INTEGER)
    return_reson_tt = Column(String(200))
    receive_man = Column(String(200))
    receive_time = Column(TIMESTAMP)
    flow_order_id = Column(CHAR(24))
    deal_opinion_desc = Column(String(200))
    arc_time = Column(TIMESTAMP)
    arc_op = Column(String(200))


class MidRidReqTower(Base):
    __tablename__ = 'mid_rid_req_tower'

    req_id = Column(CHAR(24), primary_key=True)
    version = Column(INTEGER, nullable=False)
    req_no = Column(String(80))
    req_no_tt = Column(String(80))
    site_name = Column(Text)
    scene_divide = Column(INTEGER)
    longitude = Column(DECIMAL(20, 10))
    latitude = Column(DECIMAL(20, 10))
    cover_desc = Column(String(200))
    offset_allow = Column(DECIMAL(12, 3))
    slot_num = Column(DECIMAL(12, 3))
    system_count = Column(DECIMAL(12, 3))
    system_band = Column(String(50))
    antenna_high_l = Column(DECIMAL(12, 3))
    antenna_high_h = Column(DECIMAL(12, 3))
    ant_num = Column(DECIMAL(12, 3))
    is_rruremote = Column(CHAR(1))
    delivery_time = Column(TIMESTAMP)
    state = Column(CHAR(1))
    system_type = Column(String(50))


class MidRidReqTowerArc(Base):
    __tablename__ = 'mid_rid_req_tower_arc'

    req_id = Column(String(24), primary_key=True)
    version = Column(INTEGER, nullable=False)
    req_no = Column(String(80))
    req_no_tt = Column(String(80))
    site_name = Column(Text)
    scene_divide = Column(INTEGER)
    longitude = Column(DECIMAL(20, 10))
    latitude = Column(DECIMAL(20, 10))
    cover_desc = Column(String(200))
    offset_allow = Column(DECIMAL(12, 3))
    slot_num = Column(DECIMAL(12, 3))
    system_count = Column(DECIMAL(12, 3))
    system_band = Column(String(50))
    antenna_high_l = Column(DECIMAL(12, 3))
    antenna_high_h = Column(DECIMAL(12, 3))
    ant_num = Column(DECIMAL(12, 3))
    is_rruremote = Column(CHAR(1))
    delivery_time = Column(TIMESTAMP)
    state = Column(CHAR(1))
    arc_time = Column(TIMESTAMP)
    arc_op = Column(String(200))
    system_type = Column(String(50))


class PubRestriction(Base):
    __tablename__ = 'pub_restriction'

    serial_no = Column(INTEGER, primary_key=True, nullable=False)
    desc_id = Column(INTEGER, nullable=False)
    desc_china = Column(String(100), nullable=False, index=True)
    code = Column(String(10), index=True)
    keyword = Column(String(61), nullable=False, index=True)
    is_display = Column(CHAR(1), server_default=text("'1'"))
    keyword_desc = Column(String(80), index=True)
    delete_state = Column(CHAR(1), server_default=text("'0'"))
    delete_time = Column(TIMESTAMP)
    seq_id = Column(INTEGER)
    describe_field_id = Column(INTEGER)
    describe_field_name = Column(String(255), index=True)
    version = Column(INTEGER)
    env_domain_id = Column(String(10), primary_key=True, nullable=False, server_default=text("'80010001'"))
    create_op = Column(INTEGER)
    create_date = Column(TIMESTAMP)
    modify_op = Column(INTEGER)
    modify_date = Column(TIMESTAMP)


class SpcRegion(Base):
    __tablename__ = 'spc_region'
    __table_args__ = (
        Index('uq_spc_region_region_name', 'region_name', 'super_region_id', unique=True),
        Index('uq_spc_region_region_no', 'region_no', 'delete_time', unique=True)
    )

    region_id = Column(CHAR(24), primary_key=True)
    region_no = Column(String(80), nullable=False)
    region_name = Column(String(80), nullable=False)
    alias = Column(String(80))
    grade_id = Column(INTEGER)
    type_id = Column(INTEGER)
    address = Column(String(100))
    super_region_id = Column(ForeignKey('spc_region.region_id'), index=True)
    parent_id = Column(CHAR(24))
    delete_state = Column(CHAR(1), server_default=text("'0'"))
    delete_time = Column(TIMESTAMP)
    notes = Column(String(255))
    name_ab = Column(String(20))
    res_type_id = Column(INTEGER, nullable=False, index=True, server_default=text("200"))
    china_name_ab = Column(String(40))
    modify_op = Column(INTEGER)
    modiry_date = Column(TIMESTAMP)
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    sync_date = Column(TIMESTAMP)
    old_id_eqp = Column(INTEGER)
    old_sp = Column(String(8))
    lan_id = Column(INTEGER, index=True)
    ppdom_id = Column(INTEGER, index=True)
    create_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    create_op = Column(INTEGER)
    crm_region = Column(INTEGER)
    crm_lan = Column(INTEGER)
    sp_region_id = Column(String(80))
    code = Column(String(10))

    super_region = relationship('SpcRegion', remote_side=[region_id])


t_sys_import_table_01 = Table(
    'sys_import_table_01', metadata,
    Column('process_order', INTEGER),
    Column('duplicate', INTEGER),
    Column('dump_fileid', INTEGER),
    Column('dump_position', INTEGER),
    Column('dump_length', INTEGER),
    Column('dump_orig_length', INTEGER),
    Column('dump_allocation', INTEGER),
    Column('completed_rows', INTEGER),
    Column('error_count', INTEGER),
    Column('elapsed_time', INTEGER),
    Column('object_type_path', String(200)),
    Column('object_path_seqno', INTEGER, index=True),
    Column('object_type', String(30)),
    Column('in_progress', CHAR(1)),
    Column('object_name', String(500)),
    Column('object_long_name', Text),
    Column('object_schema', String(30)),
    Column('original_object_schema', String(30)),
    Column('original_object_name', Text),
    Column('partition_name', String(30)),
    Column('subpartition_name', String(30)),
    Column('dataobj_num', INTEGER),
    Column('flags', INTEGER),
    Column('property', INTEGER),
    Column('trigflag', INTEGER),
    Column('creation_level', INTEGER),
    Column('completion_time', TIMESTAMP),
    Column('object_tablespace', String(30)),
    Column('size_estimate', INTEGER),
    Column('object_row', INTEGER),
    Column('processing_state', CHAR(1)),
    Column('processing_status', CHAR(1)),
    Column('base_process_order', INTEGER, index=True),
    Column('base_object_type', String(30)),
    Column('base_object_name', String(30)),
    Column('base_object_schema', String(30)),
    Column('ancestor_process_order', INTEGER),
    Column('domain_process_order', INTEGER),
    Column('parallelization', INTEGER),
    Column('unload_method', INTEGER),
    Column('load_method', INTEGER),
    Column('granules', INTEGER),
    Column('scn', INTEGER),
    Column('grantor', String(30)),
    Column('xml_clob', Text),
    Column('parent_process_order', INTEGER),
    Column('name', String(30)),
    Column('value_t', Text),
    Column('value_n', INTEGER),
    Column('is_default', INTEGER),
    Column('file_type', INTEGER),
    Column('user_directory', Text),
    Column('user_file_name', Text),
    Column('file_name', Text),
    Column('extend_size', INTEGER),
    Column('file_max_size', INTEGER),
    Column('process_name', String(30)),
    Column('last_update', TIMESTAMP),
    Column('work_item', String(30)),
    Column('object_number', INTEGER),
    Column('completed_bytes', INTEGER),
    Column('total_bytes', INTEGER),
    Column('metadata_io', INTEGER),
    Column('data_io', INTEGER),
    Column('cumulative_time', INTEGER),
    Column('packet_number', INTEGER),
    Column('instance_id', INTEGER),
    Column('old_value', Text),
    Column('seed', INTEGER),
    Column('last_file', INTEGER),
    Column('user_name', String(30)),
    Column('operation', String(30)),
    Column('job_mode', String(30)),
    Column('queue_tabnum', INTEGER),
    Column('control_queue', String(30)),
    Column('status_queue', String(30)),
    Column('remote_link', Text),
    Column('version', INTEGER),
    Column('job_version', String(30)),
    Column('db_version', String(30)),
    Column('timezone', String(64)),
    Column('state', String(30)),
    Column('phase', INTEGER),
    Column('start_time', TIMESTAMP),
    Column('block_size', INTEGER),
    Column('metadata_buffer_size', INTEGER),
    Column('data_buffer_size', INTEGER),
    Column('degree', INTEGER),
    Column('platform', String(101)),
    Column('abort_step', INTEGER),
    Column('instance', String(60)),
    Column('cluster_ok', INTEGER),
    Column('service_name', String(100)),
    Column('object_int_oid', String(32)),
    Column('target_xml_clob', Text),
    Index('sys_mtable_000017b2c_ind_1', 'object_schema', 'object_name', 'object_type'),
    Index('sys_c0013216', 'process_order', 'duplicate', unique=True)
)


t_tmp_mid_bill_confirm_list = Table(
    'tmp_mid_bill_confirm_list', metadata,
    Column('year_month', INTEGER),
    Column('province_id', CHAR(24)),
    Column('city_id', CHAR(24)),
    Column('region_id', String(24)),
    Column('site_code', String(40)),
    Column('elec_ensure_fee', DECIMAL(12, 4)),
    Column('adjusted_tw_rent_fee', DECIMAL(12, 4)),
    Column('adjusted_tower_rent_charge', DECIMAL(12, 4)),
    Column('adjusted_room_rent_charge', DECIMAL(12, 4)),
    Column('adjusted_pt_rent_charge', DECIMAL(12, 4)),
    Column('adjusted_site_fee', DECIMAL(12, 4)),
    Column('adjusted_maintain_fee', DECIMAL(12, 4)),
    Column('adjusted_elect_intro_fee', DECIMAL(12, 4)),
    Column('adjusted_oil_pw_fixed_fee', DECIMAL(12, 4)),
    Column('adjusted_non_oil_pw_fixed_fee', DECIMAL(12, 4)),
    Column('adjusted_other_price', DECIMAL(12, 4)),
    Column('adjusted_wave_fee', DECIMAL(12, 4)),
    Column('adjusted_wlan_fee', DECIMAL(12, 4)),
    Column('adj_bbutower_fee', DECIMAL(12, 4)),
    Column('oilgenpower_charge_ls', DECIMAL(12, 4)),
    Column('adjusted_pro_price', DECIMAL(12, 4)),
    Column('data_source', CHAR(3)),
    Column('adjusted_battery_ext_fee', DECIMAL(12, 4)),
    Column('adjusted_high_class_serv_fee', DECIMAL(12, 4)),
    Column('adjusted_bbutower_fee', DECIMAL(12, 4)),
    Column('bill_type', INTEGER)
)


t_tmp_product_height_statistics = Table(
    'tmp_product_height_statistics', metadata,
    Column('year_month', INTEGER),
    Column('parent_region_id', CHAR(24)),
    Column('region_id', CHAR(24)),
    Column('tower_type', INTEGER),
    Column('antenna_height_range', INTEGER),
    Column('total_rent_num', INTEGER),
    Column('rent_fee', DECIMAL(16, 2)),
    Column('build_fee', DECIMAL(16, 2)),
    Column('field_fee', DECIMAL(16, 2)),
    Column('mnt_fee', DECIMAL(16, 2)),
    Column('elec_in_fee', DECIMAL(16, 2)),
    Column('other_fee', DECIMAL(16, 2)),
    Column('cl_rent_fee', DECIMAL(16, 2)),
    Column('cl_build_fee', DECIMAL(16, 2)),
    Column('cl_field_fee', DECIMAL(16, 2)),
    Column('cl_mnt_fee', DECIMAL(16, 2)),
    Column('cl_elec_in_fee', DECIMAL(16, 2)),
    Column('cl_clother_fee', DECIMAL(16, 2)),
    Column('xj_rent_fee', DECIMAL(16, 2)),
    Column('xj_build_fee', DECIMAL(16, 2)),
    Column('xj_field_fee', DECIMAL(16, 2)),
    Column('xj_mnt_fee', DECIMAL(16, 2)),
    Column('xj_elec_in_fee', DECIMAL(16, 2)),
    Column('xj_clother_fee', DECIMAL(16, 2)),
    Column('bqxj_rent_fee', DECIMAL(16, 2)),
    Column('bqxj_build_fee', DECIMAL(16, 2)),
    Column('bqxj_field_fee', DECIMAL(16, 2)),
    Column('bqxj_mnt_fee', DECIMAL(16, 2)),
    Column('bqxj_elec_in_fee', DECIMAL(16, 2)),
    Column('bqxj_clother_fee', DECIMAL(16, 2)),
    Column('create_date', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
    Column('state', INTEGER, nullable=False, server_default=text("9680104"))
)


t_tmp_tw_operating_detail = Table(
    'tmp_tw_operating_detail', metadata,
    Column('detail_id', INTEGER),
    Column('year_month', INTEGER),
    Column('province_name', String(30)),
    Column('province_code', String(4)),
    Column('latn_id', INTEGER),
    Column('latn_name', String(30)),
    Column('region_id', CHAR(24)),
    Column('address_id', CHAR(24)),
    Column('address_name', String(80)),
    Column('address_no', String(50)),
    Column('address_location', String(200)),
    Column('tw_type', INTEGER),
    Column('ranking', INTEGER),
    Column('prev_ranking', INTEGER),
    Column('depreciation_fee', DECIMAL(16, 2)),
    Column('power_fee', DECIMAL(16, 2)),
    Column('build_fee', DECIMAL(16, 2)),
    Column('field_fee', DECIMAL(16, 2)),
    Column('mnt_fee', DECIMAL(16, 2)),
    Column('elec_in_fee', DECIMAL(16, 2)),
    Column('other_fee', DECIMAL(16, 2)),
    Column('total_cost_fee', DECIMAL(16, 2)),
    Column('rent_fee', DECIMAL(16, 2)),
    Column('create_date', TIMESTAMP),
    Column('state', INTEGER),
    Column('oilgenpower_charge', DECIMAL(16, 2)),
    Column('room_config', INTEGER),
    Column('tw_cur_cust_num', INTEGER),
    Column('share_info', INTEGER),
    Column('data_source', CHAR(3)),
    Column('province_id', CHAR(24)),
    Column('city_id', CHAR(24)),
    Column('room_id', CHAR(24)),
    Column('tower_id', CHAR(24)),
    Column('site_cur_cust_num', INTEGER),
    Column('elec_ensure_fee', DECIMAL(12, 4)),
    Column('non_elec_ensure_fee', DECIMAL(12, 4)),
    Column('tower_rent_charge', DECIMAL(12, 4)),
    Column('room_rent_charge', DECIMAL(12, 4)),
    Column('pt_rent_charge', DECIMAL(12, 4)),
    Column('oil_pw_fixed_fee', DECIMAL(12, 4)),
    Column('non_oil_pw_fixed_fee', DECIMAL(12, 4)),
    Column('site_other_fee', DECIMAL(12, 4)),
    Column('wave_fee', DECIMAL(12, 4)),
    Column('wlan_fee', DECIMAL(12, 4)),
    Column('bbutower_fee', DECIMAL(12, 4)),
    Column('site_share_info', INTEGER),
    Column('field_share_info', INTEGER),
    Column('room_share_info', INTEGER),
    Column('earliest_service_begin_date', TIMESTAMP),
    Column('count_region_grade', INTEGER),
    Column('adjusted_high_class_serv_fee', DECIMAL(12, 4)),
    Column('adjusted_battery_ext_fee', DECIMAL(12, 4)),
    Column('non_elec_ensure_fee_have_tax', DECIMAL(12, 4)),
    Column('bill_type', INTEGER),
    Column('chamber_cur_cust_num', INTEGER),
    Column('trans_cur_cust_num', INTEGER),
    Column('chamber_rent_charge', INTEGER),
    Column('trans_rent_charge', INTEGER),
    Column('chamber_prod', INTEGER)
)


t_tmp_tw_pro_height_statistics = Table(
    'tmp_tw_pro_height_statistics', metadata,
    Column('contract_no', String(200)),
    Column('year_month', INTEGER),
    Column('province_id', String(24), index=True),
    Column('city_id', String(24), index=True),
    Column('region_id', String(24), index=True),
    Column('tw_type', INTEGER, index=True),
    Column('start_height', INTEGER, index=True),
    Column('antenna_height', DECIMAL(12, 4)),
    Column('antenna_height1', DECIMAL(12, 4)),
    Column('antenna_height2', DECIMAL(12, 4)),
    Column('antenna_height3', DECIMAL(12, 4)),
    Column('adjusted_tw_rent_fee', DECIMAL(12, 4)),
    Column('adjusted_site_fee', DECIMAL(12, 4)),
    Column('adjusted_maintain_fee', DECIMAL(12, 4)),
    Column('adjusted_elect_intro_fee', DECIMAL(12, 4)),
    Column('adjusted_other_price', DECIMAL(12, 4)),
    Column('adjusted_wave_fee', DECIMAL(12, 4)),
    Column('adjusted_wlan_fee', DECIMAL(12, 4)),
    Column('share_info', INTEGER),
    Column('service_begin_date', TIMESTAMP),
    Column('adjusted_high_class_serv_fee', DECIMAL(12, 4)),
    Column('adjusted_battery_ext_fee', DECIMAL(12, 4)),
    Column('adjusted_bbutower_fee', DECIMAL(12, 4))
)


t_tw_operating_detail = Table(
    'tw_operating_detail', metadata,
    Column('detail_id', INTEGER, nullable=False),
    Column('year_month', INTEGER),
    Column('province_name', String(30)),
    Column('province_code', String(4)),
    Column('latn_id', INTEGER),
    Column('latn_name', String(30)),
    Column('region_id', CHAR(24)),
    Column('address_id', CHAR(24)),
    Column('address_name', String(200)),
    Column('address_no', String(50)),
    Column('address_location', String(500)),
    Column('tw_type', INTEGER),
    Column('ranking', INTEGER),
    Column('prev_ranking', INTEGER),
    Column('depreciation_fee', DECIMAL(16, 2)),
    Column('power_fee', DECIMAL(16, 2)),
    Column('build_fee', DECIMAL(16, 2)),
    Column('field_fee', DECIMAL(16, 2)),
    Column('mnt_fee', DECIMAL(16, 2)),
    Column('elec_in_fee', DECIMAL(16, 2)),
    Column('other_fee', DECIMAL(16, 2)),
    Column('total_cost_fee', DECIMAL(16, 2)),
    Column('rent_fee', DECIMAL(16, 2)),
    Column('create_date', TIMESTAMP),
    Column('state', INTEGER),
    Column('oilgenpower_charge', DECIMAL(16, 2)),
    Column('room_config', INTEGER),
    Column('tw_cur_cust_num', INTEGER),
    Column('share_info', INTEGER),
    Column('data_source', CHAR(3)),
    Column('province_id', CHAR(24)),
    Column('city_id', CHAR(24)),
    Column('room_id', CHAR(24)),
    Column('tower_id', CHAR(24)),
    Column('site_cur_cust_num', INTEGER),
    Column('elec_ensure_fee', DECIMAL(12, 4)),
    Column('non_elec_ensure_fee', DECIMAL(12, 4)),
    Column('tower_rent_charge', DECIMAL(12, 4)),
    Column('room_rent_charge', DECIMAL(12, 4)),
    Column('pt_rent_charge', DECIMAL(12, 4)),
    Column('oil_pw_fixed_fee', DECIMAL(12, 4)),
    Column('non_oil_pw_fixed_fee', DECIMAL(12, 4)),
    Column('site_other_fee', DECIMAL(12, 4)),
    Column('wave_fee', DECIMAL(12, 4)),
    Column('wlan_fee', DECIMAL(12, 4)),
    Column('bbutower_fee', DECIMAL(12, 4)),
    Column('site_share_info', INTEGER),
    Column('field_share_info', INTEGER),
    Column('room_share_info', INTEGER),
    Column('earliest_service_begin_date', TIMESTAMP),
    Column('count_region_grade', INTEGER),
    Column('adjusted_high_class_serv_fee', DECIMAL(12, 4)),
    Column('adjusted_battery_ext_fee', DECIMAL(12, 4)),
    Column('non_elec_ensure_fee_have_tax', DECIMAL(12, 4)),
    Column('bill_type', INTEGER),
    Column('chamber_cur_cust_num', INTEGER),
    Column('trans_cur_cust_num', INTEGER),
    Column('chamber_rent_charge', DECIMAL(12, 4)),
    Column('trans_rent_charge', DECIMAL(12, 4)),
    Column('chamber_prod', INTEGER)
)


class TwOperatingDetailYear(Base):
    __tablename__ = 'tw_operating_detail_year'

    detail_id = Column(INTEGER, primary_key=True)
    year_month = Column(INTEGER)
    province_name = Column(String(30))
    province_code = Column(String(4))
    latn_id = Column(INTEGER)
    latn_name = Column(String(30))
    region_id = Column(CHAR(24))
    address_id = Column(CHAR(24))
    address_name = Column(String(80))
    address_no = Column(String(50))
    address_location = Column(String(200))
    tw_type = Column(INTEGER)
    ranking = Column(INTEGER)
    prev_ranking = Column(INTEGER)
    depreciation_fee = Column(DECIMAL(16, 2))
    power_fee = Column(DECIMAL(16, 2))
    build_fee = Column(DECIMAL(16, 2))
    field_fee = Column(DECIMAL(16, 2))
    mnt_fee = Column(DECIMAL(16, 2))
    elec_in_fee = Column(DECIMAL(16, 2))
    other_fee = Column(DECIMAL(16, 2))
    total_cost_fee = Column(DECIMAL(16, 2))
    rent_fee = Column(DECIMAL(16, 2))
    create_date = Column(TIMESTAMP)
    state = Column(INTEGER, server_default=text("9680104"))
    oilgenpower_charge = Column(DECIMAL(16, 2))
    room_config = Column(INTEGER)
    tw_cur_cust_num = Column(INTEGER)
    share_info = Column(INTEGER)
    data_source = Column(CHAR(3))
    province_id = Column(CHAR(24))
    city_id = Column(CHAR(24))
    room_id = Column(CHAR(24))
    tower_id = Column(CHAR(24))
    site_cur_cust_num = Column(INTEGER)
    elec_ensure_fee = Column(DECIMAL(16, 4))
    non_elec_ensure_fee = Column(DECIMAL(16, 4))
    tower_rent_charge = Column(DECIMAL(16, 4))
    room_rent_charge = Column(DECIMAL(16, 4))
    pt_rent_charge = Column(DECIMAL(16, 4))
    oil_pw_fixed_fee = Column(DECIMAL(16, 4))
    non_oil_pw_fixed_fee = Column(DECIMAL(16, 4))
    site_other_fee = Column(DECIMAL(16, 4))
    wave_fee = Column(DECIMAL(16, 4))
    wlan_fee = Column(DECIMAL(16, 4))
    bbutower_fee = Column(DECIMAL(16, 4))
    site_share_info = Column(INTEGER)
    field_share_info = Column(INTEGER)
    room_share_info = Column(INTEGER)
    earliest_service_begin_date = Column(TIMESTAMP)
    count_region_grade = Column(INTEGER)
    adjusted_high_class_serv_fee = Column(DECIMAL(16, 4))
    adjusted_battery_ext_fee = Column(DECIMAL(16, 4))
    non_elec_ensure_fee_have_tax = Column(DECIMAL(16, 4))
    bill_type = Column(INTEGER)
    chamber_cur_cust_num = Column(INTEGER)
    trans_cur_cust_num = Column(INTEGER)
    chamber_rent_charge = Column(INTEGER)
    trans_rent_charge = Column(INTEGER)
    chamber_prod = Column(INTEGER)


t_tw_operating_detail_year_1234 = Table(
    'tw_operating_detail_year_1234', metadata,
    Column('detail_id', INTEGER, nullable=False),
    Column('year_month', INTEGER),
    Column('province_name', String(30)),
    Column('province_code', String(4)),
    Column('latn_id', INTEGER),
    Column('latn_name', String(30)),
    Column('region_id', CHAR(24)),
    Column('address_id', CHAR(24)),
    Column('address_name', String(80)),
    Column('address_no', String(50)),
    Column('address_location', String(200)),
    Column('tw_type', INTEGER),
    Column('ranking', INTEGER),
    Column('prev_ranking', INTEGER),
    Column('depreciation_fee', DECIMAL(16, 2)),
    Column('power_fee', DECIMAL(16, 2)),
    Column('build_fee', DECIMAL(16, 2)),
    Column('field_fee', DECIMAL(16, 2)),
    Column('mnt_fee', DECIMAL(16, 2)),
    Column('elec_in_fee', DECIMAL(16, 2)),
    Column('other_fee', DECIMAL(16, 2)),
    Column('total_cost_fee', DECIMAL(16, 2)),
    Column('rent_fee', DECIMAL(16, 2)),
    Column('create_date', TIMESTAMP),
    Column('state', INTEGER),
    Column('oilgenpower_charge', DECIMAL(16, 2)),
    Column('room_config', INTEGER),
    Column('tw_cur_cust_num', INTEGER),
    Column('share_info', INTEGER),
    Column('data_source', CHAR(3)),
    Column('province_id', CHAR(24)),
    Column('city_id', CHAR(24)),
    Column('room_id', CHAR(24)),
    Column('tower_id', CHAR(24)),
    Column('site_cur_cust_num', INTEGER),
    Column('elec_ensure_fee', DECIMAL(16, 4)),
    Column('non_elec_ensure_fee', DECIMAL(16, 4)),
    Column('tower_rent_charge', DECIMAL(16, 4)),
    Column('room_rent_charge', DECIMAL(16, 4)),
    Column('pt_rent_charge', DECIMAL(16, 4)),
    Column('oil_pw_fixed_fee', DECIMAL(16, 4)),
    Column('non_oil_pw_fixed_fee', DECIMAL(16, 4)),
    Column('site_other_fee', DECIMAL(16, 4)),
    Column('wave_fee', DECIMAL(16, 4)),
    Column('wlan_fee', DECIMAL(16, 4)),
    Column('bbutower_fee', DECIMAL(16, 4)),
    Column('site_share_info', INTEGER),
    Column('field_share_info', INTEGER),
    Column('room_share_info', INTEGER),
    Column('earliest_service_begin_date', TIMESTAMP),
    Column('count_region_grade', INTEGER),
    Column('adjusted_high_class_serv_fee', DECIMAL(16, 4)),
    Column('adjusted_battery_ext_fee', DECIMAL(16, 4)),
    Column('non_elec_ensure_fee_have_tax', DECIMAL(16, 4)),
    Column('bill_type', INTEGER),
    Column('chamber_cur_cust_num', INTEGER),
    Column('trans_cur_cust_num', INTEGER),
    Column('chamber_rent_charge', INTEGER),
    Column('trans_rent_charge', INTEGER),
    Column('chamber_prod', INTEGER)
)


class TwProductHeightStatistic(Base):
    __tablename__ = 'tw_product_height_statistics'

    id = Column(INTEGER, primary_key=True)
    year_month = Column(INTEGER)
    parent_region_id = Column(CHAR(24))
    region_id = Column(CHAR(24))
    tower_type = Column(INTEGER)
    antenna_height_range = Column(INTEGER)
    total_rent_num = Column(INTEGER)
    rent_fee = Column(DECIMAL(16, 2))
    build_fee = Column(DECIMAL(16, 2))
    field_fee = Column(DECIMAL(16, 2))
    mnt_fee = Column(DECIMAL(16, 2))
    elec_in_fee = Column(DECIMAL(16, 2))
    other_fee = Column(DECIMAL(16, 2))
    cl_rent_fee = Column(DECIMAL(16, 2))
    cl_build_fee = Column(DECIMAL(16, 2))
    cl_field_fee = Column(DECIMAL(16, 2))
    cl_mnt_fee = Column(DECIMAL(16, 2))
    cl_elec_in_fee = Column(DECIMAL(16, 2))
    cl_clother_fee = Column(DECIMAL(16, 2))
    xj_rent_fee = Column(DECIMAL(16, 2))
    xj_build_fee = Column(DECIMAL(16, 2))
    xj_field_fee = Column(DECIMAL(16, 2))
    xj_mnt_fee = Column(DECIMAL(16, 2))
    xj_elec_in_fee = Column(DECIMAL(16, 2))
    xj_clother_fee = Column(DECIMAL(16, 2))
    bqxj_rent_fee = Column(DECIMAL(16, 2))
    bqxj_build_fee = Column(DECIMAL(16, 2))
    bqxj_field_fee = Column(DECIMAL(16, 2))
    bqxj_mnt_fee = Column(DECIMAL(16, 2))
    bqxj_elec_in_fee = Column(DECIMAL(16, 2))
    bqxj_clother_fee = Column(DECIMAL(16, 2))
    create_date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    state = Column(INTEGER, nullable=False, server_default=text("9680104"))


class TwProvinceOperating(Base):
    __tablename__ = 'tw_province_operating'

    province_oper_id = Column(INTEGER, primary_key=True)
    year_month = Column(INTEGER)
    province_name = Column(String(30))
    province_code = Column(String(50))
    latn_id = Column(String(24))
    latn_name = Column(String(30))
    region_id = Column(CHAR(24))
    ranking = Column(INTEGER)
    prev_ranking = Column(INTEGER)
    depreciation_fee = Column(DECIMAL(16, 2))
    power_fee = Column(DECIMAL(16, 2))
    build_fee = Column(DECIMAL(16, 2))
    field_fee = Column(DECIMAL(16, 2))
    mnt_fee = Column(DECIMAL(16, 2))
    elec_in_fee = Column(DECIMAL(16, 2))
    other_fee = Column(DECIMAL(16, 2))
    total_cost_fee = Column(DECIMAL(16, 2))
    rent_fee = Column(DECIMAL(16, 2))
    cdr_2g_num = Column(INTEGER)
    ps_2g_num = Column(INTEGER)
    total_2g_business_volume = Column(DECIMAL(16, 2))
    bts_2g_num = Column(INTEGER)
    cdr_3g_num = Column(INTEGER)
    ps_3g_num = Column(INTEGER)
    total_3g_business_volume = Column(DECIMAL(16, 2))
    bts_3g_num = Column(INTEGER)
    cdr_4g_num = Column(INTEGER)
    ps_4g_num = Column(INTEGER)
    total_4g_business_volume = Column(DECIMAL(16, 2))
    bts_4g_num = Column(INTEGER)
    cdr_5g_num = Column(INTEGER)
    ps_5g_num = Column(INTEGER)
    total_5g_business_volume = Column(DECIMAL(16, 2))
    bts_5g_num = Column(INTEGER)
    total_business_volume = Column(DECIMAL(16, 2))
    total_bts = Column(INTEGER)
    only_share_bts_num = Column(INTEGER)
    two_share_bts_num = Column(INTEGER)
    three_share_bts_num = Column(INTEGER)
    create_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    state = Column(INTEGER, server_default=text("9680104"))
    parent_region_id = Column(CHAR(24))
    oilgenpower_charge = Column(DECIMAL(16, 2))
    rent_contract_num = Column(INTEGER)
    ptdm_tw_num = Column(INTEGER)
    jg_tw_num = Column(INTEGER)
    jy_tw_num = Column(INTEGER)
    ptlm_tw_num = Column(INTEGER)
    lmbg_num = Column(INTEGER)
    tw_1_num = Column(INTEGER)
    tw_2_num = Column(INTEGER)
    tw_3_num = Column(INTEGER)
    zjzh_room_num = Column(INTEGER)
    zjkj_room_num = Column(INTEGER)
    zjcg_room_num = Column(INTEGER)
    yth_room_num = Column(INTEGER)
    zy_room_num = Column(INTEGER)
    yth_jg_num = Column(INTEGER)
    rru_num = Column(INTEGER)
    no_room_num = Column(INTEGER)
    room_1_num = Column(INTEGER)
    room_2_num = Column(INTEGER)
    room_3_num = Column(INTEGER)
    cljy_share_num = Column(INTEGER)
    clxz_share_num = Column(INTEGER)
    xjsj_share_num = Column(INTEGER)
    xjgx_share_num = Column(INTEGER)
    zw_share_num = Column(INTEGER)
    share_1_num = Column(INTEGER)
    share_2_num = Column(INTEGER)
    share_3_num = Column(INTEGER)
    qt_room_num = Column(INTEGER)
    elec_ensure_fee = Column(DECIMAL(16, 4))
    non_elec_ensure_fee = Column(DECIMAL(16, 4))
    tower_rent_charge = Column(DECIMAL(16, 4))
    room_rent_charge = Column(DECIMAL(16, 4))
    pt_rent_charge = Column(DECIMAL(16, 4))
    oil_pw_fixed_fee = Column(DECIMAL(16, 4))
    non_oil_pw_fixed_fee = Column(DECIMAL(16, 4))
    site_other_fee = Column(DECIMAL(16, 4))
    wave_fee = Column(DECIMAL(16, 4))
    wlan_fee = Column(DECIMAL(16, 4))
    bbutower_fee = Column(DECIMAL(16, 4))
    his_wait_refund_fee = Column(DECIMAL(16, 4))
    maintain_of_fine = Column(DECIMAL(16, 4))
    adjusted_high_class_serv_fee = Column(DECIMAL(16, 4))
    adjusted_battery_ext_fee = Column(DECIMAL(16, 4))
    non_elec_ensure_fee_have_tax = Column(DECIMAL(16, 4))
    yjyycf_share_num = Column(INTEGER)
    wjyycf_share_num = Column(INTEGER)
    bill_type = Column(INTEGER)
    chamber_rent_charge = Column(DECIMAL(12, 4))
    trans_rent_charge = Column(DECIMAL(12, 4))
    business_chamber_num = Column(INTEGER)
    venue_chamber_num = Column(INTEGER)
    other_chamber_num = Column(INTEGER)
    metro_tunnel_num = Column(INTEGER)
    railway_tunnel_num = Column(INTEGER)
    highway_tunnel_num = Column(INTEGER)
    other_tunnel_num = Column(INTEGER)
    trans_num = Column(INTEGER)


class UosTache(Base):
    __tablename__ = 'uos_tache'

    id = Column(INTEGER, primary_key=True)
    tache_catalog_id = Column(INTEGER)
    tache_name = Column(String(60))
    tache_code = Column(String(60), index=True)
    tache_param = Column(String(60))
    tache_param2 = Column(String(60))
    current_edition = Column(String(60), nullable=False)
    create_date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    state = Column(String(3), nullable=False, index=True)
    state_date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

from sqlalchemy import create_engine

engine = create_engine('mysql://test:abc123@10.45.59.163:3306/mc_test?charset=utf8')
Base.metadata.create_all(engine)