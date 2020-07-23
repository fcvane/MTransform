# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 9:12
# @Author  : Fcvane
# @Param   : 
# @File    : OutPutPSQL.py

import os
import VariableUtil
import LogUtil

name = os.path.basename(__file__)
log = LogUtil.Logger(name)
# 数据库表对象生产器 sqlacodegen
log.info('Start execute sqlacodegen')
os.system(
    "sqlacodegen oracle://JZJK_HN_DEV:JZJK_HN_DEV@10.45.59.246:9999/orcl --outfile  %s/PSQL_SourceDB_Model.py --tables rme_card " % VariableUtil.TMP_PATH)
log.info('Execute sqlacodegen success')

# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
# metadata = Base.metadata
#
# from sqlalchemy import create_engine
#
# engine = create_engine('postgresql://pgtest:pgtest@172.21.86.205:5432/test')
# Base.metadata.create_all(engine)

# sh OraToPg.sh 10.45.59.246 9999 orcl JZJK_HN_DEV JZJK_HN_DEV 172.21.86.201 5432 test pgtest abc123