#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 15:32
# @Author  : Fcvane
# @Param   : 
# @File    : MySQLEngine.py

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import create_engine
engine = create_engine('mysql://test:abc123@10.45.59.163:3306/mc_test?charset=utf8')
Base.metadata.create_all(engine)