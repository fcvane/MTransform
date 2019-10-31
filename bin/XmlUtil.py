#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 8:47
# @Author  : IWC
# @Param   : 配置文件解析
# @File    : XmlAnalysis.py


import PasswdUtil
import os, sys
import LogUtil
import VariableUtil

try:
    import xml.etree.cElementTree as etree
except ImportError:
    import xml.etree.ElementTree as etree

name = os.path.basename(__file__)
log = LogUtil.Logger(name)

'''
解析数据库参数集目录为：../conf/dbParams
格式为：
<?xml version='1.0' encoding='utf-8'?>
<configuration>
    <auth id="SOURCEDB">
        <dbType>ORACLE</dbType>
        <host>10.45.15.201</host>
        <port>1521</port>
        <sid>orcl</sid>
        <serverName></serverName>
        <userName>tower_analy</userName>
        <passWord>2geflYJwrEixn0sP9FxFrU2wJyEJAtQgAu5CgaGnZ0idBgN6Bp0RzUuGduA5S8cihGoAxi7HtSoDIHrxO8J6YA==</passWord>
        <enable>Ture</enable>
    </auth>
</configuration>
'''


def dbCFGInfo(auth):
    taskName = VariableUtil.DB_PATH + os.sep + 'db_commondb.xml'
    log.info('Start to analysis {taskName}'.format(taskName=taskName))
    result = {}
    try:
        tree = etree.parse(taskName)
        # 获得子元素
        elemlist = tree.findall('auth[@id="%s"]' % auth)
        # 遍历task所有子元素
        for elem in elemlist:
            array = {}
            for child in elem.getchildren():
                # print(child.tag, ":", child.text)
                if child.tag == "passWord":
                    if child.text is not None:
                        array[child.tag] = PasswdUtil.decrypt(child.text)
                    else:
                        array[child.tag] = ''
                else:
                    array[child.tag] = child.text
            result[elem.attrib['id']] = array
            log.info('File {taskName} analysis sucessful '.format(taskName=taskName))
    except Exception as e:
        log.error('File {taskName} analysis failure '.format(taskName=taskName))
        sys.exit()
    # print(result)
    return result


if __name__ == '__main__':
    dbConfig = dbCFGInfo('SOURCEDB')
    print(dbConfig)
