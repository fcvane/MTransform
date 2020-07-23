#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 13:47
# @Author  : Fcvane
# @Param   : 根据源和目标数据库替换Model.py
# @File    : ModelFile.py

# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# # MySQL
# from sqlalchemy import CHAR, Column, DECIMAL, Date, ForeignKey, String, TIMESTAMP, Table, Text, text
# from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT
# # Oracle
# from sqlalchemy import CHAR, Column, DateTime, ForeignKey, Index, Table, Text, VARCHAR, text
# from sqlalchemy.dialects.oracle import NUMBER, RAW

import os
import re
import VariableUtil

SFile = 'SourceDB_Model.py'
TFile = 'TargetDB_Model.py'

# Target file is or not exists
if os.path.exists(TFile):
    os.remove(TFile)

with open(VariableUtil.TMP_PATH + os.sep + SFile, 'r', encoding='utf-8') as sf, open(
                        VariableUtil.RLT_PATH + os.sep + TFile, 'a',
        encoding='utf-8') as tf:
    for line in sf.readlines():
        line = line.replace(' "', '"')
        # 匹配后替换
        # 模块替换
        if re.match('from sqlalchemy import .*', line):
            tf.write(re.sub('from sqlalchemy import .*',
                            'from sqlalchemy import CHAR, Column, DECIMAL, Date, ForeignKey, Index, String, TIMESTAMP, Table, Text, text, BLOB, DateTime,ForeignKeyConstraint',
                            line))
        elif re.match('from sqlalchemy.dialects.oracle import .*', line):
            tf.write(re.sub('from sqlalchemy.dialects.oracle import .*',
                            'from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT',
                            line))
        # 特殊处理
        elif re.match('.*nullable=False, server_default=text\("NULL"\).*', line):
            tf.write(re.sub('nullable=False, server_default=text\("NULL"\)', 'nullable=False', line))
        elif re.match('.*primary_key=True, server_default=text\("NULL"\).*', line):
            tf.write(re.sub('primary_key=True, server_default=text\("NULL"\)', 'primary_key=True', line))
        # 字段类型替换
        # 整型替换NUMBER(8) -> INTEGER
        elif re.match('.*NUMBER\(\d+, 0, False\).*', line):
            if int(line.split('NUMBER(')[1].split(',')[0]) < 10:
                tf.write(re.sub('NUMBER\(\d+, 0, False\)', 'INTEGER', line))
            else:
                length = line.split('NUMBER(')[1].split(',')[0]
                tf.write(re.sub('NUMBER\(\d+, 0, False\)', 'DECIMAL(%s)' % length, line))
        # 浮点型替换NUMBER(12，4) -> DECIMAL(12,4)
        elif re.match('.*NUMBER\(\d+, \d+, True\).*', line):
            tf.write(re.sub('NUMBER\(', 'DECIMAL(', line).replace(', True', ''))
        elif re.match('.*, LONG.*', line):
            tf.write(re.sub(', LONG', ', BIGINT', line))
        # No Length 整形替换 NUMBER(asdecimal=False) -> INTEGER
        elif re.match('.*NUMBER\(.*asdecimal=False\).*', line):
            tf.write(re.sub('NUMBER\(.*asdecimal=False\)', 'INTEGER', line))
        # VARCHAR替换 VARCHAR(200) -> String(200)
        # Length >= 1000替换为text
        elif re.match('.*VARCHAR\(\d+\).*', line):
            if int(line.split('VARCHAR(')[1].split(')')[0]) >= 1000:
                # 主键字段需要指定长度
                if re.match('.*primary_key=True.*', line):
                    tf.write(re.sub('VARCHAR\(', 'String(', line))
                else:
                    tf.write(re.sub('VARCHAR\(\d+\)', 'Text', line))
            else:
                tf.write(re.sub('VARCHAR\(', 'String(', line))
        # char >255 处理
        elif re.match('.*CHAR\(\d+\).*', line):
            if int(line.split('CHAR(')[1].split(')')[0]) > 255:
                tf.write(re.sub('CHAR\(', 'String(', line))
            else:
                tf.write(line)
        # DateTime替换 DateTim -> Date
        elif re.match('.*DateTime.*', line):
            # 时间默认值替换
            if re.match('.*nullable=False, server_default=text\("sysdate"\).*', line):
                # tf.write(re.sub('DateTime', 'TIMESTAMP', line).replace(
                #     'text("sysdate")', 'text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")'))
                tf.write(line.replace(
                    'text("sysdate")', 'text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")'))
            elif re.match('.*nullable=False*', line) and re.match('.*server_default.*', line) is None:
                # tf.write(re.sub('DateTime', 'TIMESTAMP', line).replace(
                #     'nullable=False',
                #     'nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")'))
                tf.write(line.replace(
                    'nullable=False',
                    'nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")'))
            elif re.match('.*server_default=text\("sysdate"\).*', line):
                # tf.write(re.sub('DateTime', 'TIMESTAMP', line).replace(
                #     'text("sysdate")', 'text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")'))
                tf.write(line.replace(
                    'text("sysdate")', 'text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")'))
            elif re.match('.*server_default=text\("SYSDATE"\).*', line):
                # tf.write(re.sub('DateTime', 'TIMESTAMP', line).replace(
                #     'text("sysdate")', 'text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")'))
                tf.write(line.replace(
                    'text("SYSDATE")', 'text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")'))
            else:
                #     tf.write(re.sub('DateTime', 'TIMESTAMP', line))
                tf.write(line)
        # No Length 整形替换 NUMBER(asdecimal=False) -> INTEGER
        # elif re.match('.*NUMBER\(asdecimal=False\).*', line):
        #     tf.write(re.sub('NUMBER\(asdecimal=False\)', 'INTEGER', line))
        # 二进制类型处理  RAW BLOB -> BLOG
        elif re.match('.*, RAW.*', line):
            tf.write(re.sub(', RAW', ', BLOB', line))
        # elif re.match('.*, BLOB.*', line):
        #     tf.write(re.sub(', BLOB', ', BLOG', line))
        # CLOB -> Text
        elif re.match('.*, CLOB.*', line):
            tf.write(re.sub(', CLOB', ', Text', line))
        # LargeBinary(blob) -> BLOB
        elif re.match('.*LargeBinary.*', line):
            tf.write(re.sub('LargeBinary', 'BLOB', line))
        # Unicode(nvarchar) -> varchar
        elif re.match('.*Unicode\(.*', line):
            tf.write(re.sub('Unicode', 'String', line))
        # float -> decimal
        elif re.match('.*Float\).*', line):
            tf.write(re.sub('Float', 'DECIMAL', line))
        else:
            tf.write(line)

TFile = 'TargetDB_Model.py'
with  open(VariableUtil.RLT_PATH + os.sep + TFile, 'a', encoding='utf-8') as tf:
    tf.write('\n')
    tf.write('from sqlalchemy import create_engine \n')
    tf.write("engine = create_engine('mysql://root:root123@10.45.59.208:9014/jzjk?charset=utf8')\n")
    tf.write('Base.metadata.create_all(engine)\n')
