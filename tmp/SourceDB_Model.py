# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, ForeignKey, Index, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER, RAW
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BillChargeConfirmDetail(Base):
    __tablename__ = 'bill_charge_confirm_detail'

    confirm_detail_id = Column(NUMBER(8, 0, False), primary_key=True)
    city_id = Column(VARCHAR(24))
    year_month = Column(NUMBER(6, 0, False))
    fee_type = Column(NUMBER(8, 0, False))
    count_type = Column(NUMBER(8, 0, False))
    fee = Column(NUMBER(12, 4, True))
    send_time = Column(DateTime)
    tw_sign_time = Column(DateTime)
    telecom_sign_time = Column(DateTime)
    create_op = Column(NUMBER(8, 0, False))
    create_time = Column(DateTime)
    modify_op = Column(NUMBER(8, 0, False))
    modify_time = Column(DateTime)
    delete_state = Column(CHAR(1))
    delete_time = Column(DateTime)


t_mid_bill_confirm_list = Table(
    'mid_bill_confirm_list', metadata,
    Column('conf_list_id', CHAR(24), nullable=False),
    Column('year_month', NUMBER(6, 0, False)),
    Column('contract_id', CHAR(24)),
    Column('contract_no', VARCHAR(200), index=True),
    Column('req_no', VARCHAR(80)),
    Column('region_id', VARCHAR(24)),
    Column('site_id', VARCHAR(24)),
    Column('site_name', VARCHAR(200)),
    Column('site_code', VARCHAR(40)),
    Column('service_begin_time', DateTime),
    Column('confirm_state', NUMBER(8, 0, False)),
    Column('pro_type', NUMBER(8, 0, False)),
    Column('tw_rent_charge', NUMBER(12, 4, True)),
    Column('site_fee', NUMBER(12, 4, True)),
    Column('maintain_fee', NUMBER(12, 4, True)),
    Column('elect_intro_fee', NUMBER(12, 4, True)),
    Column('oilgenpower_fixed_charge', NUMBER(12, 4, True)),
    Column('other_price', NUMBER(12, 4, True)),
    Column('product_charge', NUMBER(12, 4, True)),
    Column('adj_tw_rent_fee', NUMBER(12, 4, True)),
    Column('adj_site_fee', NUMBER(12, 4, True)),
    Column('adj_maintain_fee', NUMBER(12, 4, True)),
    Column('adj_elect_intro_fee', NUMBER(12, 4, True)),
    Column('adj_oil_pw_fixed_fee', NUMBER(12, 4, True)),
    Column('adj_other_price', NUMBER(12, 4, True)),
    Column('adjust_price', NUMBER(12, 4, True)),
    Column('adjusted_tw_rent_fee', NUMBER(12, 4, True)),
    Column('adjusted_site_fee', NUMBER(12, 4, True)),
    Column('adjusted_maintain_fee', NUMBER(12, 4, True)),
    Column('adjusted_elect_intro_fee', NUMBER(12, 4, True)),
    Column('adjusted_oil_pw_fixed_fee', NUMBER(12, 4, True)),
    Column('adjusted_other_price', NUMBER(12, 4, True)),
    Column('adjusted_pro_price', NUMBER(12, 4, True)),
    Column('adj_reason', VARCHAR(1000)),
    Column('oilgenpower_charge_ls', NUMBER(12, 4, True)),
    Column('elec_ensure_fee', NUMBER(12, 4, True)),
    Column('create_op', NUMBER(8, 0, False)),
    Column('create_time', DateTime),
    Column('modify_op', NUMBER(8, 0, False)),
    Column('modify_time', DateTime),
    Column('delete_state', CHAR(1)),
    Column('delete_time', DateTime),
    Column('province_id', CHAR(24)),
    Column('city_id', CHAR(24)),
    Column('tower_rent_charge', NUMBER(12, 4, True)),
    Column('room_rent_charge', NUMBER(12, 4, True)),
    Column('pt_rent_charge', NUMBER(12, 4, True)),
    Column('wave_fee', NUMBER(12, 4, True)),
    Column('wlan_fee', NUMBER(12, 4, True)),
    Column('bbutower_fee', NUMBER(12, 4, True)),
    Column('adj_tower_rent_charge', NUMBER(12, 4, True)),
    Column('adj_room_rent_charge', NUMBER(12, 4, True)),
    Column('adj_pt_rent_charge', NUMBER(12, 4, True)),
    Column('adj_wave_fee', NUMBER(12, 4, True)),
    Column('adj_wlan_fee', NUMBER(12, 4, True)),
    Column('adj_bbutower_fee', NUMBER(12, 4, True)),
    Column('adjusted_tower_rent_charge', NUMBER(12, 4, True)),
    Column('adjusted_room_rent_charge', NUMBER(12, 4, True)),
    Column('adjusted_pt_rent_charge', NUMBER(12, 4, True)),
    Column('adjusted_wave_fee', NUMBER(12, 4, True)),
    Column('adjusted_wlan_fee', NUMBER(12, 4, True)),
    Column('adjusted_bbutower_fee', NUMBER(12, 4, True)),
    Column('adjusted_non_oil_pw_fixed_fee', NUMBER(12, 4, True)),
    Column('adjusted_elec_ensure_fee', NUMBER(12, 4, True)),
    Column('company', NUMBER(8, 0, False)),
    Column('bill_type', NUMBER(8, 0, False)),
    Column('req_type', NUMBER(8, 0, False)),
    Column('company_city', CHAR(24)),
    Column('company_county', CHAR(24)),
    Column('req_city', CHAR(24)),
    Column('site_city', CHAR(24)),
    Column('high_class_service_fee', NUMBER(12, 4, True)),
    Column('battery_ext_fee', NUMBER(12, 4, True)),
    Column('adj_high_class_service_fee', NUMBER(12, 4, True)),
    Column('adj_battery_ext_fee', NUMBER(12, 4, True)),
    Column('adjusted_high_class_serv_fee', NUMBER(12, 4, True)),
    Column('adjusted_battery_ext_fee', NUMBER(12, 4, True)),
    Column('adj_oil_power_none_fixed_fee', NUMBER(12, 4, True)),
    Column('adj_elec_ensure_fee', NUMBER(12, 4, True)),
    Column('adj_prod_price', NUMBER(12, 4, True)),
    Column('adj_terminal_of_amends', NUMBER(14, 4, True)),
    Column('terminal_of_amends', NUMBER(14, 4, True)),
    Column('adjusted_terminal_of_amends', NUMBER(14, 4, True))
)


class MidGomPs2Wo(Base):
    __tablename__ = 'mid_gom_ps_2_wo_s'

    id = Column(VARCHAR(24), primary_key=True)
    ord_ps_id = Column(VARCHAR(50), nullable=False, index=True)
    tache_id = Column(VARCHAR(50), nullable=False)
    dyn_tab_name = Column(VARCHAR(50))
    disp_obj_type = Column(VARCHAR(12), nullable=False)
    disp_obj_id = Column(VARCHAR(20), nullable=False)
    req_time_long = Column(NUMBER(6, 0, False))
    rec_state = Column(VARCHAR(12), nullable=False)
    create_date = Column(DateTime, nullable=False)
    state_date = Column(DateTime, nullable=False)
    req_time_un = Column(VARCHAR(12))
    can_mod_wo_disp = Column(NUMBER(9, 0, False), server_default=text("210000002"))
    remark = Column(VARCHAR(1000))
    net_grid_btn_ctl = Column(VARCHAR(100))
    is_all_dispatch = Column(VARCHAR(12), server_default=text("210000002"))
    oper_dyn_tab_name = Column(VARCHAR(50))
    asyn_service_id = Column(VARCHAR(12))
    url_flag = Column(VARCHAR(100))
    chd_ord_ps_id = Column(NUMBER(12, 0, False))
    chd_ord_process_ver = Column(NUMBER(3, 0, False))
    chd_in_date = Column(DateTime)
    up_tran_id = Column(VARCHAR(30))
    down_tran_id = Column(VARCHAR(30))
    sou_ord_ps_id = Column(NUMBER(12, 0, False))
    dom_tag_wo_ps_id = Column(NUMBER(12, 0, False))
    disp_service_id = Column(NUMBER(12, 0, False))
    sou_wo_ps_id = Column(NUMBER(12, 0, False))
    sou_tache_id = Column(VARCHAR(50))
    sou_ord_process_ver = Column(NUMBER(3, 0, False))
    a_wo_ps_id = Column(NUMBER(12, 0, False))
    a_tache_id = Column(VARCHAR(50))
    a_ord_process_ver = Column(NUMBER(3, 0, False))
    a_ord_ps_id = Column(NUMBER(12, 0, False))


class MidGomWo(Base):
    __tablename__ = 'mid_gom_wo'
    __table_args__ = (
        Index('ind_mid_gom_wo_obj_type_id', 'disp_obj_tye', 'disp_obj_id'),
    )

    wo_id = Column(VARCHAR(24), primary_key=True)
    order_id = Column(VARCHAR(24), nullable=False, index=True)
    wiid = Column(VARCHAR(50), nullable=False, index=True)
    wo_code = Column(VARCHAR(50), index=True)
    wo_title = Column(VARCHAR(100))
    old_wo_id = Column(NUMBER(12, 0, False))
    remark = Column(VARCHAR(1000))
    disp_obj_tye = Column(VARCHAR(12))
    disp_obj_id = Column(NUMBER(20, 0, False))
    disp_id = Column(NUMBER(12, 0, False))
    cko_user_id = Column(NUMBER(12, 0, False))
    comp_user_id = Column(NUMBER(12, 0, False), index=True)
    wo_state = Column(VARCHAR(12), nullable=False)
    create_date = Column(DateTime, nullable=False)
    state_date = Column(DateTime, nullable=False)
    req_fin_date = Column(DateTime, index=True)
    inner_state = Column(VARCHAR(12))
    inner_state_date = Column(DateTime)
    kw_hd_qrr_id = Column(NUMBER(12, 0, False))
    kw_hd_qrr_name = Column(VARCHAR(50))
    alarm_date = Column(DateTime)
    ps_id = Column(CHAR(24), index=True)
    form_ver = Column(NUMBER(12, 0, False))
    wo_type = Column(VARCHAR(12))
    oper_form_ver = Column(NUMBER(12, 0, False))
    wo_chg_disp_id = Column(NUMBER(12, 0, False))
    is_ze_fan = Column(VARCHAR(12))
    priv_forward_wo_id = Column(NUMBER(12, 0, False))
    deal_date = Column(DateTime)
    deal_user_id = Column(NUMBER(12, 0, False), index=True)
    priv_task_info = Column(VARCHAR(80))
    virtual_order_id = Column(NUMBER(12, 0, False))
    is_auto = Column(VARCHAR(12))
    is_auto_fail = Column(VARCHAR(12))
    had_forward_exec = Column(VARCHAR(12))
    had_back_exec = Column(VARCHAR(12))
    is_calling = Column(VARCHAR(12))
    send_wo_id = Column(VARCHAR(12))
    send_old_wo_id = Column(VARCHAR(12))
    priv_task_id = Column(VARCHAR(12))
    priv_task_type = Column(NUMBER(12, 0, False))


t_mid_req_development = Table(
    'mid_req_development', metadata,
    Column('req_no', VARCHAR(30)),
    Column('req_state', VARCHAR(30)),
    Column('province', VARCHAR(30)),
    Column('city', VARCHAR(30)),
    Column('region', VARCHAR(30)),
    Column('company', NUMBER(12, 0, False)),
    Column('pro_batch', VARCHAR(80)),
    Column('req_name', VARCHAR(100)),
    Column('scene_divide', NUMBER(12, 0, False)),
    Column('launch_time', DateTime),
    Column('delivery_time', DateTime),
    Column('receive_state_tt', NUMBER(12, 0, False)),
    Column('req_no_tt', VARCHAR(30)),
    Column('site_code', VARCHAR(30)),
    Column('site_name', VARCHAR(1024)),
    Column('is_share', CHAR(1)),
    Column('tower_type', NUMBER(12, 0, False)),
    Column('room_type', NUMBER(12, 0, False)),
    Column('build_type', NUMBER(12, 0, False)),
    Column('power_introduction_mode', NUMBER(12, 0, False)),
    Column('jf_workstarttime', DateTime),
    Column('jf_workendtime', DateTime),
    Column('jf_reality_delivertime', DateTime),
    Column('jf_check_time', DateTime),
    Column('create_date', DateTime, server_default=text("sysdate")),
    Column('state', NUMBER(12, 0, False), server_default=text("9680104")),
    Column('year_month', NUMBER(6, 0, False), index=True),
    Column('offset_allow', NUMBER(12, 3, True)),
    Column('notes', VARCHAR(2000)),
    Column('longitude', NUMBER(20, 10, True)),
    Column('latitude', NUMBER(20, 10, True)),
    Column('location', VARCHAR(500)),
    Column('slot_num', NUMBER(12, 3, True)),
    Column('antenna_high_l', NUMBER(12, 3, True)),
    Column('antenna_high_h', NUMBER(12, 3, True)),
    Column('deviation_radius', NUMBER(20, 3, True)),
    Column('antenna_count', NUMBER(12, 3, True)),
    Column('screen_confirm_is_success', CHAR(1)),
    Column('screen_confirm_fail_reason', VARCHAR(200)),
    Column('transfer_type', NUMBER(12, 0, False)),
    Column('cust_count_old', NUMBER(20, 3, True)),
    Column('cust_detail_old', NUMBER(20, 3, True)),
    Column('cust_count_new', NUMBER(20, 3, True)),
    Column('cust_detail_new', NUMBER(20, 3, True)),
    Column('tower_type_detail', NUMBER(12, 0, False)),
    Column('tower_high', NUMBER(12, 3, True)),
    Column('platform_count', NUMBER(12, 3, True)),
    Column('seat_count', NUMBER(12, 3, True)),
    Column('system_count', NUMBER(12, 3, True)),
    Column('bbu_count', NUMBER(12, 3, True)),
    Column('rru_count', NUMBER(12, 3, True)),
    Column('rru_power_mode', NUMBER(12, 0, False)),
    Column('a_battery_protection_time', NUMBER(20, 3, True)),
    Column('a_wind_pressure', NUMBER(12, 0, False)),
    Column('a_is_oil_power', CHAR(1)),
    Column('a_customer_power', VARCHAR(80)),
    Column('a_microwave_count', NUMBER(12, 3, True)),
    Column('a_microwave_high', NUMBER(12, 3, True)),
    Column('a_wlan_antenna_count', NUMBER(12, 3, True)),
    Column('a_wlan_antenna_high', NUMBER(12, 3, True)),
    Column('a_product_config', NUMBER(12, 0, False)),
    Column('product_name1', VARCHAR(128)),
    Column('product_name2', VARCHAR(128)),
    Column('product_name3', VARCHAR(128)),
    Column('product_antenna_high_1', NUMBER(12, 3, True)),
    Column('product_antenna_high_2', NUMBER(12, 3, True)),
    Column('product_antenna_high_3', NUMBER(12, 3, True)),
    Column('product_antenna_count1', NUMBER(12, 3, True)),
    Column('product_antenna_count2', NUMBER(12, 3, True)),
    Column('product_antenna_count3', NUMBER(12, 3, True)),
    Column('product_rru1', CHAR(1)),
    Column('product_rru2', CHAR(1)),
    Column('product_rru3', CHAR(1)),
    Column('product_rru_in_room1', CHAR(1)),
    Column('product_rru_in_room2', CHAR(1)),
    Column('product_rru_in_room3', CHAR(1)),
    Column('bill_type', NUMBER(12, 0, False))
)


class MidRidDeliveryTower(Base):
    __tablename__ = 'mid_rid_delivery_tower'

    delivery_id = Column(CHAR(24), primary_key=True)
    version = Column(NUMBER(8, 0, False), nullable=False)
    notes = Column(VARCHAR(2000))
    state = Column(CHAR(1))
    province = Column(VARCHAR(24))
    city = Column(VARCHAR(24))
    region = Column(VARCHAR(24))
    company = Column(NUMBER(12, 0, False))
    req_no = Column(VARCHAR(80))
    req_no_tt = Column(VARCHAR(80))
    order_instance_no = Column(VARCHAR(80))
    business_state = Column(NUMBER(12, 0, False))
    jf_project_name = Column(VARCHAR(200))
    jf_customer_name = Column(VARCHAR(100))
    jf_build_company = Column(VARCHAR(100))
    jf_design_company = Column(VARCHAR(500))
    jf_construction_company = Column(VARCHAR(100))
    jf_supervisor_comp = Column(VARCHAR(100))
    jf_workaddress = Column(VARCHAR(1024))
    jf_workstarttime = Column(DateTime)
    jf_workendtime = Column(DateTime)
    jf_reality_delivertime = Column(DateTime)
    jf_check_time = Column(DateTime)
    sc_dyjbtj = Column(NUMBER(12, 0, False))
    sc_site_loc_qk = Column(NUMBER(12, 0, False))
    sc_hang_scope = Column(NUMBER(12, 0, False))
    sc_yddcrl = Column(NUMBER(12, 0, False))
    sc_jws = Column(NUMBER(12, 0, False))
    sc_ktaz = Column(NUMBER(12, 0, False))
    wtjjbf = Column(VARCHAR(200))
    supervisor = Column(VARCHAR(80))
    supervisor_confirm_time = Column(DateTime)
    ys_checkreuslt = Column(NUMBER(12, 0, False))
    ys_tdgsfzr = Column(VARCHAR(100))
    ys_check_people = Column(VARCHAR(100))
    ys_checktime = Column(DateTime)
    ys_check_launch_man = Column(VARCHAR(100))
    ys_check_launch_time = Column(DateTime)
    ys_check_real_man_tt = Column(VARCHAR(100))
    ys_check_real_info = Column(VARCHAR(100))
    ys_check_notification_time = Column(DateTime)
    ys_check_confirm_man = Column(VARCHAR(100))
    ys_check_confirm_time = Column(VARCHAR(100))
    approval_opinion = Column(CHAR(1))
    approval_opinion_desc = Column(VARCHAR(200))
    approval_op = Column(NUMBER(8, 0, False))
    approval_op_name = Column(VARCHAR(200))
    approval_time = Column(DateTime)
    create_op = Column(NUMBER(8, 0, False))
    create_time = Column(DateTime)
    modify_op = Column(NUMBER(8, 0, False))
    modify_time = Column(DateTime)
    delete_op = Column(NUMBER(8, 0, False))
    delete_time = Column(DateTime)


class MidRidDeliveryTowerArc(Base):
    __tablename__ = 'mid_rid_delivery_tower_arc'

    delivery_id = Column(CHAR(24), primary_key=True)
    version = Column(NUMBER(8, 0, False), nullable=False)
    notes = Column(VARCHAR(2000))
    state = Column(CHAR(1))
    province = Column(VARCHAR(24))
    city = Column(VARCHAR(24))
    region = Column(VARCHAR(24))
    company = Column(NUMBER(12, 0, False))
    req_no = Column(VARCHAR(80))
    req_no_tt = Column(VARCHAR(80))
    order_instance_no = Column(VARCHAR(80))
    business_state = Column(NUMBER(12, 0, False))
    jf_project_name = Column(VARCHAR(200))
    jf_customer_name = Column(VARCHAR(100))
    jf_build_company = Column(VARCHAR(100))
    jf_design_company = Column(VARCHAR(500))
    jf_construction_company = Column(VARCHAR(100))
    jf_supervisor_comp = Column(VARCHAR(100))
    jf_workaddress = Column(VARCHAR(1024))
    jf_workstarttime = Column(DateTime)
    jf_workendtime = Column(DateTime)
    jf_reality_delivertime = Column(DateTime)
    jf_check_time = Column(DateTime)
    sc_dyjbtj = Column(NUMBER(12, 0, False))
    sc_site_loc_qk = Column(NUMBER(12, 0, False))
    sc_hang_scope = Column(NUMBER(12, 0, False))
    sc_yddcrl = Column(NUMBER(12, 0, False))
    sc_jws = Column(NUMBER(12, 0, False))
    sc_ktaz = Column(NUMBER(12, 0, False))
    wtjjbf = Column(VARCHAR(200))
    supervisor = Column(VARCHAR(80))
    supervisor_confirm_time = Column(DateTime)
    ys_checkreuslt = Column(NUMBER(12, 0, False))
    ys_tdgsfzr = Column(VARCHAR(100))
    ys_check_people = Column(VARCHAR(100))
    ys_checktime = Column(DateTime)
    ys_check_launch_man = Column(VARCHAR(100))
    ys_check_launch_time = Column(DateTime)
    ys_check_real_man_tt = Column(VARCHAR(100))
    ys_check_real_info = Column(VARCHAR(100))
    ys_check_notification_time = Column(DateTime)
    ys_check_confirm_man = Column(VARCHAR(100))
    ys_check_confirm_time = Column(VARCHAR(100))
    approval_opinion = Column(CHAR(1))
    approval_opinion_desc = Column(VARCHAR(200))
    approval_op = Column(NUMBER(8, 0, False))
    approval_op_name = Column(VARCHAR(200))
    approval_time = Column(DateTime)
    create_op = Column(NUMBER(8, 0, False))
    create_time = Column(DateTime)
    modify_op = Column(NUMBER(8, 0, False))
    modify_time = Column(DateTime)
    delete_op = Column(NUMBER(8, 0, False))
    delete_time = Column(DateTime)
    arc_time = Column(DateTime)
    arc_op = Column(VARCHAR(200))


class MidRidOrderInstance(Base):
    __tablename__ = 'mid_rid_order_instance'

    order_instance_id = Column(CHAR(24), primary_key=True)
    version = Column(NUMBER(8, 0, False), nullable=False)
    order_instance_no = Column(VARCHAR(80))
    state = Column(CHAR(1))
    business_state = Column(NUMBER(12, 0, False))
    province = Column(VARCHAR(24))
    city = Column(VARCHAR(24))
    region = Column(VARCHAR(24))
    company = Column(NUMBER(12, 0, False))
    req_no = Column(VARCHAR(80))
    req_no_tt = Column(VARCHAR(80))
    site_code = Column(VARCHAR(80))
    site_name = Column(VARCHAR(1024))
    is_share = Column(CHAR(1))
    scene_divide = Column(NUMBER(12, 0, False))
    longitude = Column(NUMBER(20, 10, True))
    latitude = Column(NUMBER(20, 10, True))
    location = Column(VARCHAR(500))
    slot_num = Column(NUMBER(12, 3, True))
    antenna_high_l = Column(NUMBER(12, 3, True))
    antenna_high_h = Column(NUMBER(12, 3, True))
    antenna_direction = Column(NUMBER(12, 3, True))
    deviation_radius = Column(NUMBER(20, 3, True))
    antenna_count = Column(NUMBER(12, 3, True))
    tower_type = Column(NUMBER(12, 0, False))
    room_type = Column(NUMBER(12, 0, False))
    build_type = Column(NUMBER(12, 0, False))
    service_level = Column(NUMBER(12, 0, False))
    screen_confirm_is_success = Column(CHAR(1))
    screen_confirm_fail_reason = Column(VARCHAR(200))
    transfer_type = Column(NUMBER(12, 0, False))
    power_introduction_mode = Column(NUMBER(12, 0, False))
    cust_count_old = Column(NUMBER(20, 3, True))
    cust_detail_old = Column(NUMBER(20, 3, True))
    cust_count_new = Column(NUMBER(20, 3, True))
    cust_detail_new = Column(NUMBER(20, 3, True))
    tower_type_detail = Column(NUMBER(12, 0, False))
    tower_high = Column(NUMBER(12, 3, True))
    platform_count = Column(NUMBER(12, 3, True))
    seat_count = Column(NUMBER(12, 3, True))
    system_count = Column(NUMBER(12, 3, True))
    bbu_count = Column(NUMBER(12, 3, True))
    rru_count = Column(NUMBER(12, 3, True))
    rru_power_mode = Column(NUMBER(12, 0, False))
    a_power_introduction_mode = Column(NUMBER(12, 0, False))
    a_battery_protection_time = Column(NUMBER(20, 3, True))
    a_wind_pressure = Column(NUMBER(12, 0, False))
    a_is_oil_power = Column(CHAR(1))
    a_customer_power = Column(VARCHAR(80))
    a_microwave_count = Column(NUMBER(12, 3, True))
    a_microwave_high = Column(NUMBER(12, 3, True))
    a_wlan_antenna_count = Column(NUMBER(12, 3, True))
    a_wlan_antenna_high = Column(NUMBER(12, 3, True))
    a_product_config = Column(NUMBER(12, 0, False))
    a_product_type = Column(VARCHAR(128))
    product_name1 = Column(VARCHAR(128))
    product_name2 = Column(VARCHAR(128))
    product_name3 = Column(VARCHAR(128))
    product_unit_count1 = Column(NUMBER(12, 3, True))
    product_unit_count2 = Column(NUMBER(12, 3, True))
    product_unit_count3 = Column(NUMBER(12, 3, True))
    product_antenna_high_1 = Column(NUMBER(12, 3, True))
    product_antenna_high_2 = Column(NUMBER(12, 3, True))
    product_antenna_high_3 = Column(NUMBER(12, 3, True))
    product_antenna_count1 = Column(NUMBER(12, 3, True))
    product_antenna_count2 = Column(NUMBER(12, 3, True))
    product_antenna_count3 = Column(NUMBER(12, 3, True))
    product_system_count1 = Column(NUMBER(12, 3, True))
    product_system_count2 = Column(NUMBER(12, 3, True))
    product_system_count3 = Column(NUMBER(12, 3, True))
    product_rru1 = Column(CHAR(1))
    product_rru2 = Column(CHAR(1))
    product_rru3 = Column(CHAR(1))
    product_rru_in_room1 = Column(CHAR(1))
    product_rru_in_room2 = Column(CHAR(1))
    product_rru_in_room3 = Column(CHAR(1))
    product_rru_servie_charge1 = Column(NUMBER(12, 3, True))
    product_rru_servie_charge2 = Column(NUMBER(12, 3, True))
    product_rru_servie_charge3 = Column(NUMBER(12, 3, True))
    launch_man = Column(VARCHAR(80))
    launch_time = Column(DateTime)
    approval_opinion = Column(CHAR(1))
    approval_opinion_desc = Column(VARCHAR(200))
    approval_op = Column(NUMBER(8, 0, False))
    approval_op_name = Column(VARCHAR(200))
    approval_time = Column(DateTime)
    create_op = Column(NUMBER(8, 0, False))
    create_time = Column(DateTime)
    modify_op = Column(NUMBER(8, 0, False))
    modify_time = Column(DateTime)
    delete_op = Column(NUMBER(8, 0, False))
    delete_time = Column(DateTime)
    building_type = Column(NUMBER(8, 0, False))
    cover_area = Column(VARCHAR(10))
    bbu_power = Column(VARCHAR(20))
    rru_power = Column(VARCHAR(20))
    tranfer_power = Column(VARCHAR(20))
    tranfer_high = Column(VARCHAR(20))
    system_type = Column(VARCHAR(80))
    band = Column(VARCHAR(80))
    poi_min_rate = Column(VARCHAR(20))
    combiner_type = Column(VARCHAR(20))
    combiner_port_num = Column(VARCHAR(20))
    is_twinchannel = Column(VARCHAR(20))
    combiner_min_rate = Column(VARCHAR(200))
    extra_protection_time = Column(VARCHAR(20))
    is_special = Column(VARCHAR(20))
    all_power = Column(VARCHAR(20))
    cabe_length = Column(VARCHAR(10))
    tunnel_length = Column(VARCHAR(10))
    project_name = Column(VARCHAR(100))
    tunnel_longitude = Column(NUMBER(20, 6, True))
    tunnel_latitude = Column(NUMBER(20, 6, True))
    tunnel_bigin_point = Column(VARCHAR(1024))
    tunnel_end_point = Column(VARCHAR(1024))
    tunnel_rout = Column(VARCHAR(1024))
    tunnel_built_type = Column(VARCHAR(100))
    optical_longitude = Column(NUMBER(20, 10, True))
    optical_latitude = Column(NUMBER(20, 10, True))
    optical_bigin_point = Column(VARCHAR(1024))
    optical_end_point = Column(VARCHAR(1024))
    optical_built_type = Column(VARCHAR(1024))
    optical_length = Column(VARCHAR(100))
    pole_longitude = Column(NUMBER(20, 6, True))
    pole_latitude = Column(NUMBER(20, 6, True))
    pole_bigin_point = Column(VARCHAR(1024))
    pole_end_point = Column(VARCHAR(1024))
    pole_length = Column(VARCHAR(100))
    remark = Column(VARCHAR(1024))
    pt_type = Column(NUMBER(8, 0, False))
    order_confirm_time = Column(DateTime)


class MidRidOrderInstanceArc(Base):
    __tablename__ = 'mid_rid_order_instance_arc'

    order_instance_id = Column(CHAR(24), primary_key=True)
    version = Column(NUMBER(8, 0, False), nullable=False)
    order_instance_no = Column(VARCHAR(80))
    state = Column(CHAR(1))
    business_state = Column(NUMBER(12, 0, False))
    province = Column(VARCHAR(24))
    city = Column(VARCHAR(24))
    region = Column(VARCHAR(24))
    company = Column(NUMBER(12, 0, False))
    req_no = Column(VARCHAR(80))
    req_no_tt = Column(VARCHAR(80))
    site_code = Column(VARCHAR(80))
    site_name = Column(VARCHAR(1024))
    is_share = Column(CHAR(1))
    scene_divide = Column(NUMBER(12, 0, False))
    longitude = Column(NUMBER(20, 10, True))
    latitude = Column(NUMBER(20, 10, True))
    location = Column(VARCHAR(500))
    slot_num = Column(NUMBER(12, 3, True))
    antenna_high_l = Column(NUMBER(12, 3, True))
    antenna_high_h = Column(NUMBER(12, 3, True))
    antenna_direction = Column(NUMBER(12, 3, True))
    deviation_radius = Column(NUMBER(20, 3, True))
    antenna_count = Column(NUMBER(12, 3, True))
    tower_type = Column(NUMBER(12, 0, False))
    room_type = Column(NUMBER(12, 0, False))
    build_type = Column(NUMBER(12, 0, False))
    service_level = Column(NUMBER(12, 0, False))
    screen_confirm_is_success = Column(CHAR(1))
    screen_confirm_fail_reason = Column(VARCHAR(200))
    transfer_type = Column(NUMBER(12, 0, False))
    power_introduction_mode = Column(NUMBER(12, 0, False))
    cust_count_old = Column(NUMBER(20, 3, True))
    cust_detail_old = Column(NUMBER(20, 3, True))
    cust_count_new = Column(NUMBER(20, 3, True))
    cust_detail_new = Column(NUMBER(20, 3, True))
    tower_type_detail = Column(NUMBER(12, 0, False))
    tower_high = Column(NUMBER(12, 3, True))
    platform_count = Column(NUMBER(12, 3, True))
    seat_count = Column(NUMBER(12, 3, True))
    system_count = Column(NUMBER(12, 3, True))
    bbu_count = Column(NUMBER(12, 3, True))
    rru_count = Column(NUMBER(12, 3, True))
    rru_power_mode = Column(NUMBER(12, 0, False))
    a_power_introduction_mode = Column(NUMBER(12, 0, False))
    a_battery_protection_time = Column(NUMBER(20, 3, True))
    a_wind_pressure = Column(NUMBER(12, 0, False))
    a_is_oil_power = Column(CHAR(1))
    a_customer_power = Column(VARCHAR(80))
    a_microwave_count = Column(NUMBER(12, 3, True))
    a_microwave_high = Column(NUMBER(12, 3, True))
    a_wlan_antenna_count = Column(NUMBER(12, 3, True))
    a_wlan_antenna_high = Column(NUMBER(12, 3, True))
    a_product_config = Column(NUMBER(12, 0, False))
    a_product_type = Column(VARCHAR(128))
    product_name1 = Column(VARCHAR(128))
    product_name2 = Column(VARCHAR(128))
    product_name3 = Column(VARCHAR(128))
    product_unit_count1 = Column(NUMBER(12, 3, True))
    product_unit_count2 = Column(NUMBER(12, 3, True))
    product_unit_count3 = Column(NUMBER(12, 3, True))
    product_antenna_high_1 = Column(NUMBER(12, 3, True))
    product_antenna_high_2 = Column(NUMBER(12, 3, True))
    product_antenna_high_3 = Column(NUMBER(12, 3, True))
    product_antenna_count1 = Column(NUMBER(12, 3, True))
    product_antenna_count2 = Column(NUMBER(12, 3, True))
    product_antenna_count3 = Column(NUMBER(12, 3, True))
    product_system_count1 = Column(NUMBER(12, 3, True))
    product_system_count2 = Column(NUMBER(12, 3, True))
    product_system_count3 = Column(NUMBER(12, 3, True))
    product_rru1 = Column(CHAR(1))
    product_rru2 = Column(CHAR(1))
    product_rru3 = Column(CHAR(1))
    product_rru_in_room1 = Column(CHAR(1))
    product_rru_in_room2 = Column(CHAR(1))
    product_rru_in_room3 = Column(CHAR(1))
    product_rru_servie_charge1 = Column(NUMBER(12, 3, True))
    product_rru_servie_charge2 = Column(NUMBER(12, 3, True))
    product_rru_servie_charge3 = Column(NUMBER(12, 3, True))
    launch_man = Column(VARCHAR(80))
    launch_time = Column(DateTime)
    approval_opinion = Column(CHAR(1))
    approval_opinion_desc = Column(VARCHAR(200))
    approval_op = Column(NUMBER(8, 0, False))
    approval_op_name = Column(VARCHAR(200))
    approval_time = Column(DateTime)
    create_op = Column(NUMBER(8, 0, False))
    create_time = Column(DateTime)
    modify_op = Column(NUMBER(8, 0, False))
    modify_time = Column(DateTime)
    delete_op = Column(NUMBER(8, 0, False))
    delete_time = Column(DateTime)
    arc_time = Column(DateTime)
    arc_op = Column(VARCHAR(200))
    building_type = Column(NUMBER(8, 0, False))
    cover_area = Column(VARCHAR(10))
    bbu_power = Column(VARCHAR(20))
    rru_power = Column(VARCHAR(20))
    tranfer_power = Column(VARCHAR(20))
    tranfer_high = Column(VARCHAR(20))
    system_type = Column(VARCHAR(80))
    band = Column(VARCHAR(80))
    poi_min_rate = Column(VARCHAR(20))
    combiner_type = Column(VARCHAR(20))
    combiner_port_num = Column(VARCHAR(20))
    is_twinchannel = Column(VARCHAR(20))
    combiner_min_rate = Column(VARCHAR(200))
    extra_protection_time = Column(VARCHAR(20))
    is_special = Column(VARCHAR(20))
    all_power = Column(VARCHAR(20))
    cabe_length = Column(VARCHAR(10))
    tunnel_length = Column(VARCHAR(10))
    project_name = Column(VARCHAR(100))
    tunnel_longitude = Column(NUMBER(20, 6, True))
    tunnel_latitude = Column(NUMBER(20, 6, True))
    tunnel_bigin_point = Column(VARCHAR(1024))
    tunnel_end_point = Column(VARCHAR(1024))
    tunnel_rout = Column(VARCHAR(1024))
    tunnel_built_type = Column(VARCHAR(100))
    optical_longitude = Column(NUMBER(20, 10, True))
    optical_latitude = Column(NUMBER(20, 10, True))
    optical_bigin_point = Column(VARCHAR(1024))
    optical_end_point = Column(VARCHAR(1024))
    optical_built_type = Column(VARCHAR(1024))
    optical_length = Column(VARCHAR(100))
    pole_longitude = Column(NUMBER(20, 6, True))
    pole_latitude = Column(NUMBER(20, 6, True))
    pole_bigin_point = Column(VARCHAR(1024))
    pole_end_point = Column(VARCHAR(1024))
    pole_length = Column(VARCHAR(100))
    remark = Column(VARCHAR(1024))
    pt_type = Column(NUMBER(8, 0, False))
    order_confirm_time = Column(DateTime)


class MidRidRentContract(Base):
    __tablename__ = 'mid_rid_rent_contract'
    __table_args__ = (
        Index('index_rid_rent_id_no', 'contract_id', 'contract_no'),
    )

    contract_id = Column(CHAR(24), primary_key=True, nullable=False, index=True)
    contract_no = Column(VARCHAR(200), index=True)
    product_type = Column(NUMBER(8, 0, False))
    contract_type = Column(NUMBER(8, 0, False))
    company = Column(NUMBER(8, 0, False))
    rent_state = Column(NUMBER(8, 0, False), index=True)
    req_no = Column(VARCHAR(80))
    region_id = Column(VARCHAR(24))
    service_begin_date = Column(DateTime)
    service_end_date = Column(DateTime)
    station_id = Column(VARCHAR(24))
    spare_baterry = Column(NUMBER(8, 2, True))
    elec_service_mode = Column(NUMBER(8, 0, False))
    elec_ensure_fee = Column(NUMBER(12, 4, True))
    other_fee = Column(NUMBER(12, 4, True))
    other_fee_notes = Column(VARCHAR(400))
    mnt_discount = Column(NUMBER(4, 2, True))
    mnt_fee = Column(NUMBER(12, 4, True))
    field_fee = Column(NUMBER(12, 4, True))
    field_discount = Column(NUMBER(4, 2, True))
    product_service_fee_tax = Column(NUMBER(12, 4, True))
    product_service_fee = Column(NUMBER(12, 4, True))
    create_time = Column(DateTime)
    create_op = Column(NUMBER(8, 0, False))
    modify_time = Column(DateTime)
    modify_op = Column(NUMBER(8, 0, False))
    delete_time = Column(DateTime)
    delete_state = Column(CHAR(1), server_default=text("'0'"))
    county_id = Column(VARCHAR(24))
    latitude = Column(NUMBER(20, 10, True))
    prov_id = Column(VARCHAR(24))
    city_id = Column(VARCHAR(24))
    company_city_id = Column(VARCHAR(24))
    req_city_id = Column(VARCHAR(24))
    scene = Column(NUMBER(8, 0, False))
    siteaddress_code = Column(VARCHAR(255), index=True)
    siteaddress_name = Column(VARCHAR(255))
    siteaddress_address = Column(VARCHAR(500))
    longitude = Column(VARCHAR(64))
    is_stand_bld_cost = Column(CHAR(1))
    contract_initiator = Column(NUMBER(8, 0, False))
    contract_initia_date = Column(DateTime)
    field_fee_mode = Column(NUMBER(8, 0, False))
    notes1 = Column(VARCHAR(255))
    notes2 = Column(VARCHAR(255))
    notes3 = Column(VARCHAR(255))
    off_hire_date = Column(DateTime)
    delete_op = Column(NUMBER(8, 0, False))
    year_month = Column(NUMBER(6, 0, False), primary_key=True, nullable=False)
    basis_mode = Column(NUMBER(8, 0, False))
    other_maintenance_fee = Column(NUMBER(12, 4, True))
    site_share_info = Column(NUMBER(8, 0, False))
    other_site_rent = Column(NUMBER(12, 4, True))
    site_rent_is_share = Column(NUMBER(8, 0, False))
    field_share_info = Column(NUMBER(8, 0, False))
    request_source = Column(NUMBER(8, 0, False))
    maint_is_share = Column(NUMBER(8, 0, False))
    is_expired = Column(CHAR(1), server_default=text("'0'"))


class MidRidRentContractTw(Base):
    __tablename__ = 'mid_rid_rent_contract_tw'

    contract_id = Column(CHAR(24), primary_key=True)
    share_info = Column(NUMBER(8, 0, False))
    tw_cur_cust_num = Column(NUMBER(8, 0, False))
    room_cur_cust_num = Column(NUMBER(8, 0, False))
    match_cust_num = Column(NUMBER(8, 0, False))
    product_config = Column(VARCHAR(400))
    tw_type = Column(NUMBER(8, 0, False))
    room_config = Column(NUMBER(8, 0, False))
    maintain_level = Column(NUMBER(8, 0, False))
    is_have_elec = Column(NUMBER(8, 0, False))
    is_choose_elec = Column(NUMBER(8, 0, False))
    oilgenpower_charge_mode = Column(NUMBER(8, 0, False))
    oilgenpower_charge_year = Column(NUMBER(12, 4, True))
    high_class_service_fee = Column(NUMBER(12, 4, True))
    tw_base_price = Column(NUMBER(12, 4, True))
    room_base_price = Column(NUMBER(12, 4, True))
    tw_discount = Column(NUMBER(4, 2, True))
    room_discount = Column(NUMBER(4, 2, True))
    match_discount = Column(NUMBER(4, 2, True))
    battery_ext_fee = Column(NUMBER(12, 4, True))
    elec_in_discount = Column(NUMBER(4, 2, True))
    elec_in_fee = Column(NUMBER(12, 4, True))
    create_time = Column(DateTime)
    create_op = Column(NUMBER(8, 0, False))
    modify_time = Column(DateTime)
    modify_op = Column(NUMBER(8, 0, False))
    delete_time = Column(DateTime)
    delete_state = Column(CHAR(1), server_default=text("'0'"))
    wind_pressure = Column(NUMBER(12, 3, True))
    pro_unit_num1 = Column(NUMBER(6, 2, True))
    antenna_height1 = Column(NUMBER(12, 4, True))
    antenna_num1 = Column(NUMBER(8, 0, False))
    sys_num1 = Column(NUMBER(8, 0, False))
    bbutower_charge_year1 = Column(NUMBER(12, 4, True))
    pro_unit_num2 = Column(NUMBER(6, 2, True))
    antenna_height2 = Column(NUMBER(12, 4, True))
    antenna_num2 = Column(NUMBER(8, 0, False))
    sys_num2 = Column(NUMBER(8, 0, False))
    bbutower_charge_year2 = Column(NUMBER(12, 4, True))
    pro_unit_num3 = Column(NUMBER(6, 2, True))
    antenna_height3 = Column(NUMBER(12, 4, True))
    antenna_num3 = Column(NUMBER(8, 0, False))
    sys_num3 = Column(NUMBER(8, 0, False))
    is_bbu_in_room3 = Column(CHAR(1))
    is_rru_on_stand3 = Column(CHAR(1))
    bbutower_charge_year3 = Column(NUMBER(12, 4, True))
    tw_share_user_bdate1 = Column(DateTime)
    tw_share_user_edate1 = Column(DateTime)
    tw_share_user_bdate2 = Column(DateTime)
    tw_share_user_edate2 = Column(DateTime)
    room_cust_bdate1 = Column(DateTime)
    room_cust_edate1 = Column(DateTime)
    room_cust_bdate2 = Column(DateTime)
    room_cust_edate2 = Column(DateTime)
    match_cust_bdate1 = Column(DateTime)
    match_cust_edate1 = Column(DateTime)
    match_cust_bdate2 = Column(DateTime)
    match_cust_edate2 = Column(DateTime)
    mnt_fee_cust_bdate1 = Column(DateTime)
    mnt_fee_cust_edate1 = Column(DateTime)
    mnt_fee_cust_bdate2 = Column(DateTime)
    mnt_fee_cust_edate2 = Column(DateTime)
    field_fee_cust_bdate1 = Column(DateTime)
    field_fee_cust_edate1 = Column(DateTime)
    field_fee_cust_bdate2 = Column(DateTime)
    field_fee_cust_edate2 = Column(DateTime)
    elec_in_disc_cust_bdate1 = Column(DateTime)
    elec_in_disc_cust_edate1 = Column(DateTime)
    elec_in_disc_cust_bdate2 = Column(DateTime)
    elec_in_disc_cust_edate2 = Column(DateTime)
    tw_build_price = Column(NUMBER(12, 4, True))
    room_build_price = Column(NUMBER(12, 4, True))
    match_build_price = Column(NUMBER(12, 4, True))
    match_base_price = Column(NUMBER(12, 4, True))
    is_rru_discount = Column(CHAR(1))
    wlan_service_fee = Column(NUMBER(12, 4, True))
    wave_service_fee = Column(NUMBER(12, 4, True))
    tw_service_fee = Column(NUMBER(12, 4, True))
    tw_height = Column(NUMBER(12, 4, True))
    elec_in_fee_mode = Column(NUMBER(8, 0, False))
    mnt_fee_cust_num = Column(NUMBER(8, 0, False))
    field_fee_cust_num = Column(NUMBER(8, 0, False))
    elec_in_disc_cust_num = Column(NUMBER(8, 0, False))
    is_bbu_in_room1 = Column(CHAR(1))
    is_rru_on_stand1 = Column(CHAR(1))
    is_bbu_in_room2 = Column(CHAR(1))
    is_rru_on_stand2 = Column(CHAR(1))
    is_06upsite = Column(NUMBER(8, 0, False))
    room_share_info = Column(NUMBER(8, 0, False))
    year_month = Column(NUMBER(6, 0, False))
    other_elec_in_fee = Column(NUMBER(12, 4, True))
    elec_in_fee_is_share = Column(NUMBER(8, 0, False))
    guarantee_count = Column(NUMBER(10, 0, False))
    guarantee_time = Column(NUMBER(10, 0, False))
    micro_discount = Column(NUMBER(10, 2, True))
    wlanap_discount = Column(NUMBER(10, 2, True))
    micro_antenna_num = Column(NUMBER(10, 0, False))
    micro_antenna_height = Column(NUMBER(10, 0, False))
    wlanap_num = Column(NUMBER(10, 0, False))
    wlanap_height = Column(NUMBER(10, 0, False))
    pt_share_info = Column(NUMBER(8, 0, False))
    pt_config = Column(NUMBER(8, 0, False))


class MidRidReq(Base):
    __tablename__ = 'mid_rid_req'

    req_id = Column(CHAR(24), primary_key=True)
    version = Column(NUMBER(8, 0, False), nullable=False)
    req_no = Column(VARCHAR(80))
    req_no_tt = Column(VARCHAR(80))
    req_type = Column(NUMBER(12, 0, False))
    req_name = Column(VARCHAR(80))
    req_desc = Column(VARCHAR(200))
    province = Column(VARCHAR(24))
    city = Column(VARCHAR(24))
    region = Column(VARCHAR(24))
    pro_batch = Column(VARCHAR(80))
    delivery_time = Column(DateTime)
    company = Column(NUMBER(12, 0, False))
    site_code = Column(VARCHAR(80))
    site_name = Column(VARCHAR(1024))
    longitude = Column(NUMBER(20, 10, True))
    latitude = Column(NUMBER(20, 10, True))
    location = Column(VARCHAR(200))
    launch_man = Column(NUMBER(8, 0, False))
    launch_time = Column(DateTime)
    rel_tel = Column(VARCHAR(200))
    project_site = Column(VARCHAR(80))
    notes = Column(VARCHAR(2000))
    create_op = Column(NUMBER(8, 0, False))
    create_time = Column(DateTime)
    modify_op = Column(NUMBER(8, 0, False))
    modify_time = Column(DateTime)
    modify_desc = Column(VARCHAR(2000))
    delete_reason = Column(NUMBER(12, 0, False))
    delete_op = Column(NUMBER(8, 0, False))
    delete_time = Column(DateTime)
    delete_desc = Column(VARCHAR(2000))
    file_name = Column(VARCHAR(2000))
    state = Column(CHAR(1))
    business_state = Column(NUMBER(12, 0, False))
    approval_opinion = Column(CHAR(1))
    approval_opinion_desc = Column(VARCHAR(200))
    approval_op = Column(NUMBER(8, 0, False))
    approval_op_name = Column(VARCHAR(200))
    approval_time = Column(DateTime)
    commit_tt_success = Column(CHAR(1))
    commit_tt_fail_reson = Column(VARCHAR(200))
    receive_state_tt = Column(NUMBER(12, 0, False))
    return_reson_tt = Column(VARCHAR(200))
    receive_man = Column(VARCHAR(200))
    receive_time = Column(DateTime)
    flow_order_id = Column(CHAR(24))
    deal_opinion_desc = Column(VARCHAR(200))


class MidRidReqArc(Base):
    __tablename__ = 'mid_rid_req_arc'

    req_id = Column(CHAR(24), primary_key=True)
    version = Column(NUMBER(8, 0, False), nullable=False)
    req_no = Column(VARCHAR(80))
    req_no_tt = Column(VARCHAR(80))
    req_type = Column(NUMBER(12, 0, False))
    req_name = Column(VARCHAR(80))
    req_desc = Column(VARCHAR(200))
    province = Column(VARCHAR(24))
    city = Column(VARCHAR(24))
    region = Column(VARCHAR(24))
    pro_batch = Column(VARCHAR(80))
    delivery_time = Column(DateTime)
    company = Column(NUMBER(12, 0, False))
    site_code = Column(VARCHAR(80))
    site_name = Column(VARCHAR(1024))
    longitude = Column(NUMBER(20, 10, True))
    latitude = Column(NUMBER(20, 10, True))
    location = Column(VARCHAR(200))
    launch_man = Column(NUMBER(8, 0, False))
    launch_time = Column(DateTime)
    rel_tel = Column(VARCHAR(200))
    project_site = Column(VARCHAR(80))
    notes = Column(VARCHAR(2000))
    create_op = Column(NUMBER(8, 0, False))
    create_time = Column(DateTime)
    modify_op = Column(NUMBER(8, 0, False))
    modify_time = Column(DateTime)
    modify_desc = Column(VARCHAR(2000))
    delete_reason = Column(NUMBER(12, 0, False))
    delete_op = Column(NUMBER(8, 0, False))
    delete_time = Column(DateTime)
    delete_desc = Column(VARCHAR(2000))
    file_name = Column(VARCHAR(2000))
    state = Column(CHAR(1))
    business_state = Column(NUMBER(12, 0, False))
    approval_opinion = Column(CHAR(1))
    approval_opinion_desc = Column(VARCHAR(200))
    approval_op = Column(NUMBER(8, 0, False))
    approval_op_name = Column(VARCHAR(200))
    approval_time = Column(DateTime)
    commit_tt_success = Column(CHAR(1))
    commit_tt_fail_reson = Column(VARCHAR(200))
    receive_state_tt = Column(NUMBER(12, 0, False))
    return_reson_tt = Column(VARCHAR(200))
    receive_man = Column(VARCHAR(200))
    receive_time = Column(DateTime)
    flow_order_id = Column(CHAR(24))
    deal_opinion_desc = Column(VARCHAR(200))
    arc_time = Column(DateTime)
    arc_op = Column(VARCHAR(200))


class MidRidReqTower(Base):
    __tablename__ = 'mid_rid_req_tower'

    req_id = Column(CHAR(24), primary_key=True)
    version = Column(NUMBER(8, 0, False), nullable=False)
    req_no = Column(VARCHAR(80))
    req_no_tt = Column(VARCHAR(80))
    site_name = Column(VARCHAR(1024))
    scene_divide = Column(NUMBER(12, 0, False))
    longitude = Column(NUMBER(20, 10, True))
    latitude = Column(NUMBER(20, 10, True))
    cover_desc = Column(VARCHAR(200))
    offset_allow = Column(NUMBER(12, 3, True))
    slot_num = Column(NUMBER(12, 3, True))
    system_count = Column(NUMBER(12, 3, True))
    system_band = Column(VARCHAR(50))
    antenna_high_l = Column(NUMBER(12, 3, True))
    antenna_high_h = Column(NUMBER(12, 3, True))
    ant_num = Column(NUMBER(12, 3, True))
    is_rruremote = Column(CHAR(1))
    delivery_time = Column(DateTime)
    state = Column(CHAR(1))
    system_type = Column(VARCHAR(50))


class MidRidReqTowerArc(Base):
    __tablename__ = 'mid_rid_req_tower_arc'

    req_id = Column(VARCHAR(24), primary_key=True)
    version = Column(NUMBER(8, 0, False), nullable=False)
    req_no = Column(VARCHAR(80))
    req_no_tt = Column(VARCHAR(80))
    site_name = Column(VARCHAR(1024))
    scene_divide = Column(NUMBER(12, 0, False))
    longitude = Column(NUMBER(20, 10, True))
    latitude = Column(NUMBER(20, 10, True))
    cover_desc = Column(VARCHAR(200))
    offset_allow = Column(NUMBER(12, 3, True))
    slot_num = Column(NUMBER(12, 3, True))
    system_count = Column(NUMBER(12, 3, True))
    system_band = Column(VARCHAR(50))
    antenna_high_l = Column(NUMBER(12, 3, True))
    antenna_high_h = Column(NUMBER(12, 3, True))
    ant_num = Column(NUMBER(12, 3, True))
    is_rruremote = Column(CHAR(1))
    delivery_time = Column(DateTime)
    state = Column(CHAR(1))
    arc_time = Column(DateTime)
    arc_op = Column(VARCHAR(200))
    system_type = Column(VARCHAR(50))


class PubRestriction(Base):
    __tablename__ = 'pub_restriction'

    serial_no = Column(NUMBER(12, 0, False), primary_key=True, nullable=False)
    desc_id = Column(NUMBER(38, 0, False), nullable=False)
    desc_china = Column(VARCHAR(100), nullable=False, index=True)
    code = Column(VARCHAR(10), index=True)
    keyword = Column(VARCHAR(61), nullable=False, index=True)
    is_display = Column(CHAR(1), server_default=text("'1'"))
    keyword_desc = Column(VARCHAR(80), index=True)
    delete_state = Column(CHAR(1), server_default=text("'0'"))
    delete_time = Column(DateTime)
    seq_id = Column(NUMBER(5, 0, False))
    describe_field_id = Column(NUMBER(8, 0, False))
    describe_field_name = Column(VARCHAR(255), index=True)
    version = Column(NUMBER(14, 0, False))
    env_domain_id = Column(VARCHAR(10), primary_key=True, nullable=False, server_default=text("'80010001' "))
    create_op = Column(NUMBER(24, 0, False))
    create_date = Column(DateTime)
    modify_op = Column(NUMBER(24, 0, False))
    modify_date = Column(DateTime)


class SpcRegion(Base):
    __tablename__ = 'spc_region'
    __table_args__ = (
        Index('uq_spc_region_region_name', 'region_name', 'super_region_id', unique=True),
        Index('uq_spc_region_region_no', 'region_no', 'delete_time', unique=True)
    )

    region_id = Column(CHAR(24), primary_key=True)
    region_no = Column(VARCHAR(80), nullable=False)
    region_name = Column(VARCHAR(80), nullable=False)
    alias = Column(VARCHAR(80))
    grade_id = Column(NUMBER(8, 0, False))
    type_id = Column(NUMBER(8, 0, False))
    address = Column(VARCHAR(100))
    super_region_id = Column(ForeignKey('spc_region.region_id'), index=True)
    parent_id = Column(CHAR(24))
    delete_state = Column(CHAR(1), server_default=text("'0'"))
    delete_time = Column(DateTime)
    notes = Column(VARCHAR(255))
    name_ab = Column(VARCHAR(20))
    res_type_id = Column(NUMBER(8, 0, False), nullable=False, index=True, server_default=text("200 "))
    china_name_ab = Column(VARCHAR(40))
    modify_op = Column(NUMBER(8, 0, False))
    modiry_date = Column(DateTime)
    create_time = Column(DateTime, server_default=text("sysdate"))
    sync_date = Column(DateTime)
    old_id_eqp = Column(NUMBER(8, 0, False))
    old_sp = Column(VARCHAR(8))
    lan_id = Column(NUMBER(8, 0, False), index=True)
    ppdom_id = Column(NUMBER(8, 0, False), index=True)
    create_date = Column(DateTime, server_default=text("sysdate"))
    create_op = Column(NUMBER(8, 0, False))
    crm_region = Column(NUMBER(8, 0, False))
    crm_lan = Column(NUMBER(8, 0, False))
    sp_region_id = Column(VARCHAR(80))
    code = Column(VARCHAR(10))

    super_region = relationship('SpcRegion', remote_side=[region_id])


t_sys_import_table_01 = Table(
    'sys_import_table_01', metadata,
    Column('process_order', NUMBER(asdecimal=False)),
    Column('duplicate', NUMBER(asdecimal=False)),
    Column('dump_fileid', NUMBER(asdecimal=False)),
    Column('dump_position', NUMBER(asdecimal=False)),
    Column('dump_length', NUMBER(asdecimal=False)),
    Column('dump_orig_length', NUMBER(asdecimal=False)),
    Column('dump_allocation', NUMBER(asdecimal=False)),
    Column('completed_rows', NUMBER(asdecimal=False)),
    Column('error_count', NUMBER(asdecimal=False)),
    Column('elapsed_time', NUMBER(asdecimal=False)),
    Column('object_type_path', VARCHAR(200)),
    Column('object_path_seqno', NUMBER(asdecimal=False), index=True),
    Column('object_type', VARCHAR(30)),
    Column('in_progress', CHAR(1)),
    Column('object_name', VARCHAR(500)),
    Column('object_long_name', VARCHAR(4000)),
    Column('object_schema', VARCHAR(30)),
    Column('original_object_schema', VARCHAR(30)),
    Column('original_object_name', VARCHAR(4000)),
    Column('partition_name', VARCHAR(30)),
    Column('subpartition_name', VARCHAR(30)),
    Column('dataobj_num', NUMBER(asdecimal=False)),
    Column('flags', NUMBER(asdecimal=False)),
    Column('property', NUMBER(asdecimal=False)),
    Column('trigflag', NUMBER(asdecimal=False)),
    Column('creation_level', NUMBER(asdecimal=False)),
    Column('completion_time', DateTime),
    Column('object_tablespace', VARCHAR(30)),
    Column('size_estimate', NUMBER(asdecimal=False)),
    Column('object_row', NUMBER(asdecimal=False)),
    Column('processing_state', CHAR(1)),
    Column('processing_status', CHAR(1)),
    Column('base_process_order', NUMBER(asdecimal=False), index=True),
    Column('base_object_type', VARCHAR(30)),
    Column('base_object_name', VARCHAR(30)),
    Column('base_object_schema', VARCHAR(30)),
    Column('ancestor_process_order', NUMBER(asdecimal=False)),
    Column('domain_process_order', NUMBER(asdecimal=False)),
    Column('parallelization', NUMBER(asdecimal=False)),
    Column('unload_method', NUMBER(asdecimal=False)),
    Column('load_method', NUMBER(asdecimal=False)),
    Column('granules', NUMBER(asdecimal=False)),
    Column('scn', NUMBER(asdecimal=False)),
    Column('grantor', VARCHAR(30)),
    Column('xml_clob', Text),
    Column('parent_process_order', NUMBER(asdecimal=False)),
    Column('name', VARCHAR(30)),
    Column('value_t', VARCHAR(4000)),
    Column('value_n', NUMBER(asdecimal=False)),
    Column('is_default', NUMBER(asdecimal=False)),
    Column('file_type', NUMBER(asdecimal=False)),
    Column('user_directory', VARCHAR(4000)),
    Column('user_file_name', VARCHAR(4000)),
    Column('file_name', VARCHAR(4000)),
    Column('extend_size', NUMBER(asdecimal=False)),
    Column('file_max_size', NUMBER(asdecimal=False)),
    Column('process_name', VARCHAR(30)),
    Column('last_update', DateTime),
    Column('work_item', VARCHAR(30)),
    Column('object_number', NUMBER(asdecimal=False)),
    Column('completed_bytes', NUMBER(asdecimal=False)),
    Column('total_bytes', NUMBER(asdecimal=False)),
    Column('metadata_io', NUMBER(asdecimal=False)),
    Column('data_io', NUMBER(asdecimal=False)),
    Column('cumulative_time', NUMBER(asdecimal=False)),
    Column('packet_number', NUMBER(asdecimal=False)),
    Column('instance_id', NUMBER(asdecimal=False)),
    Column('old_value', VARCHAR(4000)),
    Column('seed', NUMBER(asdecimal=False)),
    Column('last_file', NUMBER(asdecimal=False)),
    Column('user_name', VARCHAR(30)),
    Column('operation', VARCHAR(30)),
    Column('job_mode', VARCHAR(30)),
    Column('queue_tabnum', NUMBER(asdecimal=False)),
    Column('control_queue', VARCHAR(30)),
    Column('status_queue', VARCHAR(30)),
    Column('remote_link', VARCHAR(4000)),
    Column('version', NUMBER(asdecimal=False)),
    Column('job_version', VARCHAR(30)),
    Column('db_version', VARCHAR(30)),
    Column('timezone', VARCHAR(64)),
    Column('state', VARCHAR(30)),
    Column('phase', NUMBER(asdecimal=False)),
    Column('guid', RAW),
    Column('start_time', DateTime),
    Column('block_size', NUMBER(asdecimal=False)),
    Column('metadata_buffer_size', NUMBER(asdecimal=False)),
    Column('data_buffer_size', NUMBER(asdecimal=False)),
    Column('degree', NUMBER(asdecimal=False)),
    Column('platform', VARCHAR(101)),
    Column('abort_step', NUMBER(asdecimal=False)),
    Column('instance', VARCHAR(60)),
    Column('cluster_ok', NUMBER(asdecimal=False)),
    Column('service_name', VARCHAR(100)),
    Column('object_int_oid', VARCHAR(32)),
    Column('target_xml_clob', Text),
    Index('sys_c0013216', 'process_order', 'duplicate', unique=True),
    Index('sys_mtable_000017b2c_ind_1', 'object_schema', 'object_name', 'object_type')
)


t_tmp_mid_bill_confirm_list = Table(
    'tmp_mid_bill_confirm_list', metadata,
    Column('year_month', NUMBER(6, 0, False)),
    Column('province_id', CHAR(24)),
    Column('city_id', CHAR(24)),
    Column('region_id', VARCHAR(24)),
    Column('site_code', VARCHAR(40)),
    Column('elec_ensure_fee', NUMBER(12, 4, True)),
    Column('adjusted_tw_rent_fee', NUMBER(12, 4, True)),
    Column('adjusted_tower_rent_charge', NUMBER(12, 4, True)),
    Column('adjusted_room_rent_charge', NUMBER(12, 4, True)),
    Column('adjusted_pt_rent_charge', NUMBER(12, 4, True)),
    Column('adjusted_site_fee', NUMBER(12, 4, True)),
    Column('adjusted_maintain_fee', NUMBER(12, 4, True)),
    Column('adjusted_elect_intro_fee', NUMBER(12, 4, True)),
    Column('adjusted_oil_pw_fixed_fee', NUMBER(12, 4, True)),
    Column('adjusted_non_oil_pw_fixed_fee', NUMBER(12, 4, True)),
    Column('adjusted_other_price', NUMBER(12, 4, True)),
    Column('adjusted_wave_fee', NUMBER(12, 4, True)),
    Column('adjusted_wlan_fee', NUMBER(12, 4, True)),
    Column('adj_bbutower_fee', NUMBER(12, 4, True)),
    Column('oilgenpower_charge_ls', NUMBER(12, 4, True)),
    Column('adjusted_pro_price', NUMBER(12, 4, True)),
    Column('data_source', CHAR(3)),
    Column('adjusted_battery_ext_fee', NUMBER(12, 4, True)),
    Column('adjusted_high_class_serv_fee', NUMBER(12, 4, True)),
    Column('adjusted_bbutower_fee', NUMBER(12, 4, True)),
    Column('bill_type', NUMBER(asdecimal=False))
)


t_tmp_product_height_statistics = Table(
    'tmp_product_height_statistics', metadata,
    Column('year_month', NUMBER(6, 0, False)),
    Column('parent_region_id', CHAR(24)),
    Column('region_id', CHAR(24)),
    Column('tower_type', NUMBER(8, 0, False)),
    Column('antenna_height_range', NUMBER(8, 0, False)),
    Column('total_rent_num', NUMBER(14, 0, False)),
    Column('rent_fee', NUMBER(16, 2, True)),
    Column('build_fee', NUMBER(16, 2, True)),
    Column('field_fee', NUMBER(16, 2, True)),
    Column('mnt_fee', NUMBER(16, 2, True)),
    Column('elec_in_fee', NUMBER(16, 2, True)),
    Column('other_fee', NUMBER(16, 2, True)),
    Column('cl_rent_fee', NUMBER(16, 2, True)),
    Column('cl_build_fee', NUMBER(16, 2, True)),
    Column('cl_field_fee', NUMBER(16, 2, True)),
    Column('cl_mnt_fee', NUMBER(16, 2, True)),
    Column('cl_elec_in_fee', NUMBER(16, 2, True)),
    Column('cl_clother_fee', NUMBER(16, 2, True)),
    Column('xj_rent_fee', NUMBER(16, 2, True)),
    Column('xj_build_fee', NUMBER(16, 2, True)),
    Column('xj_field_fee', NUMBER(16, 2, True)),
    Column('xj_mnt_fee', NUMBER(16, 2, True)),
    Column('xj_elec_in_fee', NUMBER(16, 2, True)),
    Column('xj_clother_fee', NUMBER(16, 2, True)),
    Column('bqxj_rent_fee', NUMBER(16, 2, True)),
    Column('bqxj_build_fee', NUMBER(16, 2, True)),
    Column('bqxj_field_fee', NUMBER(16, 2, True)),
    Column('bqxj_mnt_fee', NUMBER(16, 2, True)),
    Column('bqxj_elec_in_fee', NUMBER(16, 2, True)),
    Column('bqxj_clother_fee', NUMBER(16, 2, True)),
    Column('create_date', DateTime, nullable=False, server_default=text("sysdate ")),
    Column('state', NUMBER(12, 0, False), nullable=False, server_default=text("9680104 "))
)


t_tmp_tw_operating_detail = Table(
    'tmp_tw_operating_detail', metadata,
    Column('detail_id', NUMBER(12, 0, False)),
    Column('year_month', NUMBER(6, 0, False)),
    Column('province_name', VARCHAR(30)),
    Column('province_code', VARCHAR(4)),
    Column('latn_id', NUMBER(6, 0, False)),
    Column('latn_name', VARCHAR(30)),
    Column('region_id', CHAR(24)),
    Column('address_id', CHAR(24)),
    Column('address_name', VARCHAR(80)),
    Column('address_no', VARCHAR(50)),
    Column('address_location', VARCHAR(200)),
    Column('tw_type', NUMBER(8, 0, False)),
    Column('ranking', NUMBER(8, 0, False)),
    Column('prev_ranking', NUMBER(8, 0, False)),
    Column('depreciation_fee', NUMBER(16, 2, True)),
    Column('power_fee', NUMBER(16, 2, True)),
    Column('build_fee', NUMBER(16, 2, True)),
    Column('field_fee', NUMBER(16, 2, True)),
    Column('mnt_fee', NUMBER(16, 2, True)),
    Column('elec_in_fee', NUMBER(16, 2, True)),
    Column('other_fee', NUMBER(16, 2, True)),
    Column('total_cost_fee', NUMBER(16, 2, True)),
    Column('rent_fee', NUMBER(16, 2, True)),
    Column('create_date', DateTime),
    Column('state', NUMBER(12, 0, False)),
    Column('oilgenpower_charge', NUMBER(16, 2, True)),
    Column('room_config', NUMBER(8, 0, False)),
    Column('tw_cur_cust_num', NUMBER(8, 0, False)),
    Column('share_info', NUMBER(8, 0, False)),
    Column('data_source', CHAR(3)),
    Column('province_id', CHAR(24)),
    Column('city_id', CHAR(24)),
    Column('room_id', CHAR(24)),
    Column('tower_id', CHAR(24)),
    Column('site_cur_cust_num', NUMBER(8, 0, False)),
    Column('elec_ensure_fee', NUMBER(12, 4, True)),
    Column('non_elec_ensure_fee', NUMBER(12, 4, True)),
    Column('tower_rent_charge', NUMBER(12, 4, True)),
    Column('room_rent_charge', NUMBER(12, 4, True)),
    Column('pt_rent_charge', NUMBER(12, 4, True)),
    Column('oil_pw_fixed_fee', NUMBER(12, 4, True)),
    Column('non_oil_pw_fixed_fee', NUMBER(12, 4, True)),
    Column('site_other_fee', NUMBER(12, 4, True)),
    Column('wave_fee', NUMBER(12, 4, True)),
    Column('wlan_fee', NUMBER(12, 4, True)),
    Column('bbutower_fee', NUMBER(12, 4, True)),
    Column('site_share_info', NUMBER(8, 0, False)),
    Column('field_share_info', NUMBER(8, 0, False)),
    Column('room_share_info', NUMBER(8, 0, False)),
    Column('earliest_service_begin_date', DateTime),
    Column('count_region_grade', NUMBER(8, 0, False)),
    Column('adjusted_high_class_serv_fee', NUMBER(12, 4, True)),
    Column('adjusted_battery_ext_fee', NUMBER(12, 4, True)),
    Column('non_elec_ensure_fee_have_tax', NUMBER(12, 4, True)),
    Column('bill_type', NUMBER(asdecimal=False)),
    Column('chamber_cur_cust_num', NUMBER(asdecimal=False)),
    Column('trans_cur_cust_num', NUMBER(asdecimal=False)),
    Column('chamber_rent_charge', NUMBER(asdecimal=False)),
    Column('trans_rent_charge', NUMBER(asdecimal=False)),
    Column('chamber_prod', NUMBER(asdecimal=False))
)


t_tmp_tw_pro_height_statistics = Table(
    'tmp_tw_pro_height_statistics', metadata,
    Column('contract_no', VARCHAR(200)),
    Column('year_month', NUMBER(6, 0, False)),
    Column('province_id', VARCHAR(24), index=True),
    Column('city_id', VARCHAR(24), index=True),
    Column('region_id', VARCHAR(24), index=True),
    Column('tw_type', NUMBER(8, 0, False), index=True),
    Column('start_height', NUMBER(8, 0, False), index=True),
    Column('antenna_height', NUMBER(12, 4, True)),
    Column('antenna_height1', NUMBER(12, 4, True)),
    Column('antenna_height2', NUMBER(12, 4, True)),
    Column('antenna_height3', NUMBER(12, 4, True)),
    Column('adjusted_tw_rent_fee', NUMBER(12, 4, True)),
    Column('adjusted_site_fee', NUMBER(12, 4, True)),
    Column('adjusted_maintain_fee', NUMBER(12, 4, True)),
    Column('adjusted_elect_intro_fee', NUMBER(12, 4, True)),
    Column('adjusted_other_price', NUMBER(12, 4, True)),
    Column('adjusted_wave_fee', NUMBER(12, 4, True)),
    Column('adjusted_wlan_fee', NUMBER(12, 4, True)),
    Column('share_info', NUMBER(8, 0, False)),
    Column('service_begin_date', DateTime),
    Column('adjusted_high_class_serv_fee', NUMBER(12, 4, True)),
    Column('adjusted_battery_ext_fee', NUMBER(12, 4, True)),
    Column('adjusted_bbutower_fee', NUMBER(12, 4, True))
)


t_tw_operating_detail = Table(
    'tw_operating_detail', metadata,
    Column('detail_id', NUMBER(12, 0, False), nullable=False),
    Column('year_month', NUMBER(6, 0, False)),
    Column('province_name', VARCHAR(30)),
    Column('province_code', VARCHAR(4)),
    Column('latn_id', NUMBER(6, 0, False)),
    Column('latn_name', VARCHAR(30)),
    Column('region_id', CHAR(24)),
    Column('address_id', CHAR(24)),
    Column('address_name', VARCHAR(200)),
    Column('address_no', VARCHAR(50)),
    Column('address_location', VARCHAR(500)),
    Column('tw_type', NUMBER(8, 0, False)),
    Column('ranking', NUMBER(8, 0, False)),
    Column('prev_ranking', NUMBER(8, 0, False)),
    Column('depreciation_fee', NUMBER(16, 2, True)),
    Column('power_fee', NUMBER(16, 2, True)),
    Column('build_fee', NUMBER(16, 2, True)),
    Column('field_fee', NUMBER(16, 2, True)),
    Column('mnt_fee', NUMBER(16, 2, True)),
    Column('elec_in_fee', NUMBER(16, 2, True)),
    Column('other_fee', NUMBER(16, 2, True)),
    Column('total_cost_fee', NUMBER(16, 2, True)),
    Column('rent_fee', NUMBER(16, 2, True)),
    Column('create_date', DateTime),
    Column('state', NUMBER(12, 0, False)),
    Column('oilgenpower_charge', NUMBER(16, 2, True)),
    Column('room_config', NUMBER(8, 0, False)),
    Column('tw_cur_cust_num', NUMBER(8, 0, False)),
    Column('share_info', NUMBER(8, 0, False)),
    Column('data_source', CHAR(3)),
    Column('province_id', CHAR(24)),
    Column('city_id', CHAR(24)),
    Column('room_id', CHAR(24)),
    Column('tower_id', CHAR(24)),
    Column('site_cur_cust_num', NUMBER(8, 0, False)),
    Column('elec_ensure_fee', NUMBER(12, 4, True)),
    Column('non_elec_ensure_fee', NUMBER(12, 4, True)),
    Column('tower_rent_charge', NUMBER(12, 4, True)),
    Column('room_rent_charge', NUMBER(12, 4, True)),
    Column('pt_rent_charge', NUMBER(12, 4, True)),
    Column('oil_pw_fixed_fee', NUMBER(12, 4, True)),
    Column('non_oil_pw_fixed_fee', NUMBER(12, 4, True)),
    Column('site_other_fee', NUMBER(12, 4, True)),
    Column('wave_fee', NUMBER(12, 4, True)),
    Column('wlan_fee', NUMBER(12, 4, True)),
    Column('bbutower_fee', NUMBER(12, 4, True)),
    Column('site_share_info', NUMBER(8, 0, False)),
    Column('field_share_info', NUMBER(8, 0, False)),
    Column('room_share_info', NUMBER(8, 0, False)),
    Column('earliest_service_begin_date', DateTime),
    Column('count_region_grade', NUMBER(8, 0, False)),
    Column('adjusted_high_class_serv_fee', NUMBER(12, 4, True)),
    Column('adjusted_battery_ext_fee', NUMBER(12, 4, True)),
    Column('non_elec_ensure_fee_have_tax', NUMBER(12, 4, True)),
    Column('bill_type', NUMBER(8, 0, False)),
    Column('chamber_cur_cust_num', NUMBER(8, 0, False)),
    Column('trans_cur_cust_num', NUMBER(8, 0, False)),
    Column('chamber_rent_charge', NUMBER(12, 4, True)),
    Column('trans_rent_charge', NUMBER(12, 4, True)),
    Column('chamber_prod', NUMBER(8, 0, False))
)


class TwOperatingDetailYear(Base):
    __tablename__ = 'tw_operating_detail_year'

    detail_id = Column(NUMBER(12, 0, False), primary_key=True)
    year_month = Column(NUMBER(6, 0, False))
    province_name = Column(VARCHAR(30))
    province_code = Column(VARCHAR(4))
    latn_id = Column(NUMBER(6, 0, False))
    latn_name = Column(VARCHAR(30))
    region_id = Column(CHAR(24))
    address_id = Column(CHAR(24))
    address_name = Column(VARCHAR(80))
    address_no = Column(VARCHAR(50))
    address_location = Column(VARCHAR(200))
    tw_type = Column(NUMBER(8, 0, False))
    ranking = Column(NUMBER(8, 0, False))
    prev_ranking = Column(NUMBER(8, 0, False))
    depreciation_fee = Column(NUMBER(16, 2, True))
    power_fee = Column(NUMBER(16, 2, True))
    build_fee = Column(NUMBER(16, 2, True))
    field_fee = Column(NUMBER(16, 2, True))
    mnt_fee = Column(NUMBER(16, 2, True))
    elec_in_fee = Column(NUMBER(16, 2, True))
    other_fee = Column(NUMBER(16, 2, True))
    total_cost_fee = Column(NUMBER(16, 2, True))
    rent_fee = Column(NUMBER(16, 2, True))
    create_date = Column(DateTime)
    state = Column(NUMBER(12, 0, False), server_default=text("9680104"))
    oilgenpower_charge = Column(NUMBER(16, 2, True))
    room_config = Column(NUMBER(8, 0, False))
    tw_cur_cust_num = Column(NUMBER(8, 0, False))
    share_info = Column(NUMBER(8, 0, False))
    data_source = Column(CHAR(3))
    province_id = Column(CHAR(24))
    city_id = Column(CHAR(24))
    room_id = Column(CHAR(24))
    tower_id = Column(CHAR(24))
    site_cur_cust_num = Column(NUMBER(8, 0, False))
    elec_ensure_fee = Column(NUMBER(16, 4, True))
    non_elec_ensure_fee = Column(NUMBER(16, 4, True))
    tower_rent_charge = Column(NUMBER(16, 4, True))
    room_rent_charge = Column(NUMBER(16, 4, True))
    pt_rent_charge = Column(NUMBER(16, 4, True))
    oil_pw_fixed_fee = Column(NUMBER(16, 4, True))
    non_oil_pw_fixed_fee = Column(NUMBER(16, 4, True))
    site_other_fee = Column(NUMBER(16, 4, True))
    wave_fee = Column(NUMBER(16, 4, True))
    wlan_fee = Column(NUMBER(16, 4, True))
    bbutower_fee = Column(NUMBER(16, 4, True))
    site_share_info = Column(NUMBER(8, 0, False))
    field_share_info = Column(NUMBER(8, 0, False))
    room_share_info = Column(NUMBER(8, 0, False))
    earliest_service_begin_date = Column(DateTime)
    count_region_grade = Column(NUMBER(8, 0, False))
    adjusted_high_class_serv_fee = Column(NUMBER(16, 4, True))
    adjusted_battery_ext_fee = Column(NUMBER(16, 4, True))
    non_elec_ensure_fee_have_tax = Column(NUMBER(16, 4, True))
    bill_type = Column(NUMBER(12, 0, False))
    chamber_cur_cust_num = Column(NUMBER(12, 0, False))
    trans_cur_cust_num = Column(NUMBER(12, 0, False))
    chamber_rent_charge = Column(NUMBER(12, 0, False))
    trans_rent_charge = Column(NUMBER(12, 0, False))
    chamber_prod = Column(NUMBER(12, 0, False))


t_tw_operating_detail_year_1234 = Table(
    'tw_operating_detail_year_1234', metadata,
    Column('detail_id', NUMBER(12, 0, False), nullable=False),
    Column('year_month', NUMBER(6, 0, False)),
    Column('province_name', VARCHAR(30)),
    Column('province_code', VARCHAR(4)),
    Column('latn_id', NUMBER(6, 0, False)),
    Column('latn_name', VARCHAR(30)),
    Column('region_id', CHAR(24)),
    Column('address_id', CHAR(24)),
    Column('address_name', VARCHAR(80)),
    Column('address_no', VARCHAR(50)),
    Column('address_location', VARCHAR(200)),
    Column('tw_type', NUMBER(8, 0, False)),
    Column('ranking', NUMBER(8, 0, False)),
    Column('prev_ranking', NUMBER(8, 0, False)),
    Column('depreciation_fee', NUMBER(16, 2, True)),
    Column('power_fee', NUMBER(16, 2, True)),
    Column('build_fee', NUMBER(16, 2, True)),
    Column('field_fee', NUMBER(16, 2, True)),
    Column('mnt_fee', NUMBER(16, 2, True)),
    Column('elec_in_fee', NUMBER(16, 2, True)),
    Column('other_fee', NUMBER(16, 2, True)),
    Column('total_cost_fee', NUMBER(16, 2, True)),
    Column('rent_fee', NUMBER(16, 2, True)),
    Column('create_date', DateTime),
    Column('state', NUMBER(12, 0, False)),
    Column('oilgenpower_charge', NUMBER(16, 2, True)),
    Column('room_config', NUMBER(8, 0, False)),
    Column('tw_cur_cust_num', NUMBER(8, 0, False)),
    Column('share_info', NUMBER(8, 0, False)),
    Column('data_source', CHAR(3)),
    Column('province_id', CHAR(24)),
    Column('city_id', CHAR(24)),
    Column('room_id', CHAR(24)),
    Column('tower_id', CHAR(24)),
    Column('site_cur_cust_num', NUMBER(8, 0, False)),
    Column('elec_ensure_fee', NUMBER(16, 4, True)),
    Column('non_elec_ensure_fee', NUMBER(16, 4, True)),
    Column('tower_rent_charge', NUMBER(16, 4, True)),
    Column('room_rent_charge', NUMBER(16, 4, True)),
    Column('pt_rent_charge', NUMBER(16, 4, True)),
    Column('oil_pw_fixed_fee', NUMBER(16, 4, True)),
    Column('non_oil_pw_fixed_fee', NUMBER(16, 4, True)),
    Column('site_other_fee', NUMBER(16, 4, True)),
    Column('wave_fee', NUMBER(16, 4, True)),
    Column('wlan_fee', NUMBER(16, 4, True)),
    Column('bbutower_fee', NUMBER(16, 4, True)),
    Column('site_share_info', NUMBER(8, 0, False)),
    Column('field_share_info', NUMBER(8, 0, False)),
    Column('room_share_info', NUMBER(8, 0, False)),
    Column('earliest_service_begin_date', DateTime),
    Column('count_region_grade', NUMBER(8, 0, False)),
    Column('adjusted_high_class_serv_fee', NUMBER(16, 4, True)),
    Column('adjusted_battery_ext_fee', NUMBER(16, 4, True)),
    Column('non_elec_ensure_fee_have_tax', NUMBER(16, 4, True)),
    Column('bill_type', NUMBER(12, 0, False)),
    Column('chamber_cur_cust_num', NUMBER(12, 0, False)),
    Column('trans_cur_cust_num', NUMBER(12, 0, False)),
    Column('chamber_rent_charge', NUMBER(12, 0, False)),
    Column('trans_rent_charge', NUMBER(12, 0, False)),
    Column('chamber_prod', NUMBER(12, 0, False))
)


class TwProductHeightStatistic(Base):
    __tablename__ = 'tw_product_height_statistics'

    id = Column(NUMBER(12, 0, False), primary_key=True)
    year_month = Column(NUMBER(6, 0, False))
    parent_region_id = Column(CHAR(24))
    region_id = Column(CHAR(24))
    tower_type = Column(NUMBER(8, 0, False))
    antenna_height_range = Column(NUMBER(8, 0, False))
    total_rent_num = Column(NUMBER(14, 0, False))
    rent_fee = Column(NUMBER(16, 2, True))
    build_fee = Column(NUMBER(16, 2, True))
    field_fee = Column(NUMBER(16, 2, True))
    mnt_fee = Column(NUMBER(16, 2, True))
    elec_in_fee = Column(NUMBER(16, 2, True))
    other_fee = Column(NUMBER(16, 2, True))
    cl_rent_fee = Column(NUMBER(16, 2, True))
    cl_build_fee = Column(NUMBER(16, 2, True))
    cl_field_fee = Column(NUMBER(16, 2, True))
    cl_mnt_fee = Column(NUMBER(16, 2, True))
    cl_elec_in_fee = Column(NUMBER(16, 2, True))
    cl_clother_fee = Column(NUMBER(16, 2, True))
    xj_rent_fee = Column(NUMBER(16, 2, True))
    xj_build_fee = Column(NUMBER(16, 2, True))
    xj_field_fee = Column(NUMBER(16, 2, True))
    xj_mnt_fee = Column(NUMBER(16, 2, True))
    xj_elec_in_fee = Column(NUMBER(16, 2, True))
    xj_clother_fee = Column(NUMBER(16, 2, True))
    bqxj_rent_fee = Column(NUMBER(16, 2, True))
    bqxj_build_fee = Column(NUMBER(16, 2, True))
    bqxj_field_fee = Column(NUMBER(16, 2, True))
    bqxj_mnt_fee = Column(NUMBER(16, 2, True))
    bqxj_elec_in_fee = Column(NUMBER(16, 2, True))
    bqxj_clother_fee = Column(NUMBER(16, 2, True))
    create_date = Column(DateTime, nullable=False, server_default=text("sysdate "))
    state = Column(NUMBER(12, 0, False), nullable=False, server_default=text("9680104 "))


class TwProvinceOperating(Base):
    __tablename__ = 'tw_province_operating'

    province_oper_id = Column(NUMBER(12, 0, False), primary_key=True)
    year_month = Column(NUMBER(6, 0, False))
    province_name = Column(VARCHAR(30))
    province_code = Column(VARCHAR(50))
    latn_id = Column(VARCHAR(24))
    latn_name = Column(VARCHAR(30))
    region_id = Column(CHAR(24))
    ranking = Column(NUMBER(8, 0, False))
    prev_ranking = Column(NUMBER(8, 0, False))
    depreciation_fee = Column(NUMBER(16, 2, True))
    power_fee = Column(NUMBER(16, 2, True))
    build_fee = Column(NUMBER(16, 2, True))
    field_fee = Column(NUMBER(16, 2, True))
    mnt_fee = Column(NUMBER(16, 2, True))
    elec_in_fee = Column(NUMBER(16, 2, True))
    other_fee = Column(NUMBER(16, 2, True))
    total_cost_fee = Column(NUMBER(16, 2, True))
    rent_fee = Column(NUMBER(16, 2, True))
    cdr_2g_num = Column(NUMBER(14, 0, False))
    ps_2g_num = Column(NUMBER(14, 0, False))
    total_2g_business_volume = Column(NUMBER(16, 2, True))
    bts_2g_num = Column(NUMBER(14, 0, False))
    cdr_3g_num = Column(NUMBER(14, 0, False))
    ps_3g_num = Column(NUMBER(14, 0, False))
    total_3g_business_volume = Column(NUMBER(16, 2, True))
    bts_3g_num = Column(NUMBER(14, 0, False))
    cdr_4g_num = Column(NUMBER(14, 0, False))
    ps_4g_num = Column(NUMBER(14, 0, False))
    total_4g_business_volume = Column(NUMBER(16, 2, True))
    bts_4g_num = Column(NUMBER(14, 0, False))
    cdr_5g_num = Column(NUMBER(14, 0, False))
    ps_5g_num = Column(NUMBER(14, 0, False))
    total_5g_business_volume = Column(NUMBER(16, 2, True))
    bts_5g_num = Column(NUMBER(14, 0, False))
    total_business_volume = Column(NUMBER(16, 2, True))
    total_bts = Column(NUMBER(14, 0, False))
    only_share_bts_num = Column(NUMBER(14, 0, False))
    two_share_bts_num = Column(NUMBER(14, 0, False))
    three_share_bts_num = Column(NUMBER(14, 0, False))
    create_date = Column(DateTime, server_default=text("sysdate"))
    state = Column(NUMBER(12, 0, False), server_default=text("9680104"))
    parent_region_id = Column(CHAR(24))
    oilgenpower_charge = Column(NUMBER(16, 2, True))
    rent_contract_num = Column(NUMBER(14, 0, False))
    ptdm_tw_num = Column(NUMBER(14, 0, False))
    jg_tw_num = Column(NUMBER(14, 0, False))
    jy_tw_num = Column(NUMBER(14, 0, False))
    ptlm_tw_num = Column(NUMBER(14, 0, False))
    lmbg_num = Column(NUMBER(14, 0, False))
    tw_1_num = Column(NUMBER(14, 0, False))
    tw_2_num = Column(NUMBER(14, 0, False))
    tw_3_num = Column(NUMBER(14, 0, False))
    zjzh_room_num = Column(NUMBER(14, 0, False))
    zjkj_room_num = Column(NUMBER(14, 0, False))
    zjcg_room_num = Column(NUMBER(14, 0, False))
    yth_room_num = Column(NUMBER(14, 0, False))
    zy_room_num = Column(NUMBER(14, 0, False))
    yth_jg_num = Column(NUMBER(14, 0, False))
    rru_num = Column(NUMBER(14, 0, False))
    no_room_num = Column(NUMBER(14, 0, False))
    room_1_num = Column(NUMBER(14, 0, False))
    room_2_num = Column(NUMBER(14, 0, False))
    room_3_num = Column(NUMBER(14, 0, False))
    cljy_share_num = Column(NUMBER(14, 0, False))
    clxz_share_num = Column(NUMBER(14, 0, False))
    xjsj_share_num = Column(NUMBER(14, 0, False))
    xjgx_share_num = Column(NUMBER(14, 0, False))
    zw_share_num = Column(NUMBER(14, 0, False))
    share_1_num = Column(NUMBER(14, 0, False))
    share_2_num = Column(NUMBER(14, 0, False))
    share_3_num = Column(NUMBER(14, 0, False))
    qt_room_num = Column(NUMBER(14, 0, False))
    elec_ensure_fee = Column(NUMBER(16, 4, True))
    non_elec_ensure_fee = Column(NUMBER(16, 4, True))
    tower_rent_charge = Column(NUMBER(16, 4, True))
    room_rent_charge = Column(NUMBER(16, 4, True))
    pt_rent_charge = Column(NUMBER(16, 4, True))
    oil_pw_fixed_fee = Column(NUMBER(16, 4, True))
    non_oil_pw_fixed_fee = Column(NUMBER(16, 4, True))
    site_other_fee = Column(NUMBER(16, 4, True))
    wave_fee = Column(NUMBER(16, 4, True))
    wlan_fee = Column(NUMBER(16, 4, True))
    bbutower_fee = Column(NUMBER(16, 4, True))
    his_wait_refund_fee = Column(NUMBER(16, 4, True))
    maintain_of_fine = Column(NUMBER(16, 4, True))
    adjusted_high_class_serv_fee = Column(NUMBER(16, 4, True))
    adjusted_battery_ext_fee = Column(NUMBER(16, 4, True))
    non_elec_ensure_fee_have_tax = Column(NUMBER(16, 4, True))
    yjyycf_share_num = Column(NUMBER(14, 0, False))
    wjyycf_share_num = Column(NUMBER(14, 0, False))
    bill_type = Column(NUMBER(8, 0, False))
    chamber_rent_charge = Column(NUMBER(12, 4, True))
    trans_rent_charge = Column(NUMBER(12, 4, True))
    business_chamber_num = Column(NUMBER(14, 0, False))
    venue_chamber_num = Column(NUMBER(14, 0, False))
    other_chamber_num = Column(NUMBER(14, 0, False))
    metro_tunnel_num = Column(NUMBER(14, 0, False))
    railway_tunnel_num = Column(NUMBER(14, 0, False))
    highway_tunnel_num = Column(NUMBER(14, 0, False))
    other_tunnel_num = Column(NUMBER(14, 0, False))
    trans_num = Column(NUMBER(14, 0, False))


class UosTache(Base):
    __tablename__ = 'uos_tache'

    id = Column(NUMBER(12, 0, False), primary_key=True)
    tache_catalog_id = Column(NUMBER(12, 0, False))
    tache_name = Column(VARCHAR(60))
    tache_code = Column(VARCHAR(60), index=True)
    tache_param = Column(VARCHAR(60))
    tache_param2 = Column(VARCHAR(60))
    current_edition = Column(VARCHAR(60), nullable=False)
    create_date = Column(DateTime, nullable=False)
    state = Column(VARCHAR(3), nullable=False, index=True)
    state_date = Column(DateTime, nullable=False)
