#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 13:38
# @Author  : Fcvane
# @Param   : 数据库表对象生产器 sqlacodegen
# @File    : ModelFile.py

import os

os.system("sqlacodegen oracle://tower_analy:tower_analy@10.45.15.201:1521/orcl --outfile  OraModel.py")