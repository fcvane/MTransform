#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 16:22
# @Author  : Fcvane
# @Param   :
# @File    : Main.py

import os
import VariableUtil
import LogUtil

name = os.path.basename(__file__)
log = LogUtil.Logger(name)

# 数据库表对象生产器 sqlacodegen
log.info('Start execute sqlacodegen')
os.system(
    "sqlacodegen oracle://tower_analy:tower_analy@10.45.15.201:1521/orcl --outfile  %s/SourceDB_Model.py" % VariableUtil.TMP_PATH)
log.info('Execute sqlacodegen success')
# Model.py文件替换成目标库类
log.info('Start replace sourcedb model with targetdb model')
os.system("python %s/ModelFile.py" % VariableUtil.BIN_PATH)
log.info('Replace sourcedb model with targetdb model success')

log.info('Add sqlalchemy create_engine')
TFile = 'TargetDB_Model.py'
with  open(VariableUtil.RLT_PATH + os.sep + TFile, 'a', encoding='utf-8') as tf:
    tf.write('\n')
    tf.write('from sqlalchemy import create_engine \n')
    tf.write("engine = create_engine('mysql://test:abc123@10.45.59.163:3306/mc_test?charset=utf8')\n")
    tf.write('Base.metadata.create_all(engine)\n')

# log.info('Start execute targetdb model')
# os.system("python %s/%s" % (VariableUtil.RLT_PATH, TFile))
