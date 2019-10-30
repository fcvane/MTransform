#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 16:22
# @Author  : Fcvane
# @Param   : 
# @File    : Main.py

from sqlalchemy import CHAR, Column, DECIMAL, Date, ForeignKey, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

metadata = Base.metadata

from sqlalchemy import create_engine

engine = create_engine('mysql://test:abc123@10.45.59.163:3306/mc_test?charset=utf8')
Base.metadata.create_all(engine)
