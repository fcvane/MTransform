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

'''
海南电信
10.45.59.184:1521/resdb
USER_JZJK:USER_JZJK

大榕产品库
10.45.59.246:9999/orcl 
FICUS_R9:FICUS_R9
'''



# 数据库表对象生产器 sqlacodegen
log.info('Start execute sqlacodegen')
os.system(
    "sqlacodegen oracle://USER_JZJK:USER_JZJK@10.45.59.184:1521/resdb --outfile  %s/SourceDB_Model.py --tables bfm_event_code,global_bo_temp,global_object " % VariableUtil.TMP_PATH)
log.info('Execute sqlacodegen success')
# Model.py文件替换成目标库类
log.info('Start replace sourcedb model with targetdb model')
os.system("python %s/ModelFile.py" % VariableUtil.BIN_PATH)
log.info('Replace sourcedb model with targetdb model success')

# log.info('Add sqlalchemy create_engine')
# TFile = 'TargetDB_Model.py'
# with  open(VariableUtil.RLT_PATH + os.sep + TFile, 'a', encoding='utf-8') as tf:
#     tf.write('\n')
#     tf.write('from sqlalchemy import create_engine \n')
#     tf.write("engine = create_engine('mysql://cmsx_bdta:iwhalecloud123@10.45.59.211:3306/cmsx_bdta?charset=utf8')\n")
#     tf.write('Base.metadata.create_all(engine)\n')

# log.info('Start execute targetdb model')
# os.system("python %s/%s" % (VariableUtil.RLT_PATH, TFile))
