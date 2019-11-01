#/bin/bash
#Usage:
#		Oracle数据批量导入MySQL
#fileName:OraToMySQL.sh

#脚本路径
#filedir=`pwd`
filedir=/home/fcvane
#脚本所在主目录信息
#tmp->临时文件
#log->日志信息
#conf->配置文件目录
#bin->脚本路径

#tabdir=`cd ${filedir}/..&& pwd`
tabdir=/home/fcvane
tmpdir=${tabdir}/tmp
logdir=${tabdir}/log
confdir=${tabdir}/conf
bindir=${filedir}
dataxdir=${tabdir}/datax
jobdir=${tabdir}/job

#oracle数据库客户端
oradir=${tabdir}/instantclient_12_2

#加载环境变量
export ORACLE_HOME=${oradir}
export LD_LIBRARY_PATH=${oradir}
export TNS_ADMIN=${oradir}
export PATH=$PATH:${oradir}

#DataX配置文件初始化


if [ -f ${tmpdir}/ora_ne.log ]
then
	rm -rf ${tmpdir}/ora_ne.log
fi

if [ -f ${tmpdir}/mysql_ne.log ]
then
	rm -rf ${tmpdir}/mysql_ne.log
fi

#创建管道
mkfifo testfifo
exec 6<>testfifo
rm -rf testfifo
#并发数控制
thread=4
for ((i=0;i<=$thread;i++))
do
 echo >&6
done

#OracleToMySQL
OraToMySQL(){
	#加载配置文件
	#判断文件中的表是否都存在
	range=(`cat ${confdir}/tabname.lst`)
	len=${#range[@]}
	#遍历
	for((i=0;i<$len;i++))
	do
	read -u6
    {
		#判断
#		${oradir}/sqlplus scott/abc123@10.45.15.205:1521/orcl <<EOF > #${logdir}/oracnt_${range[$i]}.log
#			select count(1) cnt from user_tables where #table_name=upper('${range[$i]}');
#EOF
		${oradir}/sqlplus ${ORAUSERNAME}/${ORAPASSWORD}@${ORAHOST}:${ORAPORT}/${ORASID} <<EOF > ${logdir}/oracnt_${range[$i]}.log
			select count(1) cnt from user_tables where table_name=upper('${range[$i]}');
EOF
		echo "[OraToMySQL] Check if the table ${range[$i]} exists:"
		#存在则为1 不存在则为0
		n=`cat ${logdir}/oracnt_${range[$i]}.log | grep -A 2 "CNT" | grep -vE "CNT|--" | sed s/[[:space:]]//g`
		if [ $n -eq 1 ]
		then
			echo "[OraToMySQL] ${range[$i]} exists in oracle!"
			#存在则判断mysql中是否存在
			mysql -h${MySQLHOST} -P${MySQLPORT} -u${MySQLUSERNAME} -p${MySQLPASSWORD} -D ${MySQLSCHEMA} <<EOF > ${logdir}/mysqlcnt_${range[$i]}.log
			select count(1) cnt from information_schema.tables where table_schema='${MySQLSCHEMA}' and table_name=lower('${range[$i]}')
EOF
			m=`cat ${logdir}/mysqlcnt_${range[$i]}.log | grep -A 2 "cnt" | grep -vE "cnt|--" | sed s/[[:space:]]//g `
			if [ $m -eq 1 ]
			then
				echo "[OraToMySQL] ${range[$i]} exists in MySQL!"		
				#表字段信息
				mysql -h${MySQLHOST} -P${MySQLPORT} -u${MySQLUSERNAME} -p${MySQLPASSWORD} -D ${MySQLSCHEMA} <<EOF > ${logdir}/mysqlcol_${range[$i]}.log
				SELECT concat('"',UPPER(COLUMN_NAME),'",')  AS column_name FROM information_schema.columns WHERE table_schema='${MySQLSCHEMA}' and table_name = lower('${range[$i]}');
EOF
				#MySQL关键词特殊处理-1
				range_key=(`cat ${confdir}/keyword.lst`)
				len_key=${#range_key[@]}
				for((j=0;j<$len_key;j++))
				do
					flag=`cat ${logdir}/mysqlcol_${range[$i]}.log | grep -w "${range_key[$j]}" | wc -l`
					if [ $flag -ne 0 ]
					then
						cp ${logdir}/mysqlcol_${range[$i]}.log ${logdir}/mysqlcol_${range[$i]}_specil.log
						sed -i "s/${range_key[$j]}/\`${range_key[$j]}\`/g" ${logdir}/mysqlcol_${range[$i]}_specil.log
					fi
				
				done
								
				tmp1=`cat ${logdir}/mysqlcol_${range[$i]}.log | grep "\"," | grep -v "||" | xargs`
				colname=`echo ${tmp1%,*}`
				ORASQL="select ${colname} from ${range[$i]}"
				tmp2=`cat ${logdir}/mysqlcol_${range[$i]}_specil.log | grep "\"" | sed ':a;N;s/\n/ /;t a ;' | sed s/[[:space:]]//g`
				column=`echo ${tmp2%,*}`
				MySQLCOL=$column
				PRESQL="truncate table ${range[$i]}"
				TABLENAME=${range[$i]}
								
				#复制datax xml配置文件模板
				cp ${confdir}/OraToMySQL.xml ${jobdir}/OraToMySQL_${range[$i]}.xml
				#替换配置文件信息
				echo "------------------"${MySQLJDBC}
				sed -i "s!ORAUSERNAME!${ORAUSERNAME}!g" ${jobdir}/OraToMySQL_${range[$i]}.xml
				sed -i "s!ORAPASSWORD!${ORAPASSWORD}!g" ${jobdir}/OraToMySQL_${range[$i]}.xml
				sed -i "s!ORAJDBC!${ORAJDBC}!g" ${jobdir}/OraToMySQL_${range[$i]}.xml
				sed -i "s!ORASQL!${ORASQL}!g" ${jobdir}/OraToMySQL_${range[$i]}.xml
				sed -i "s!MySQLUSERNAME!${MySQLUSERNAME}!g" ${jobdir}/OraToMySQL_${range[$i]}.xml
				sed -i "s!MySQLPASSWORD!${MySQLPASSWORD}!g" ${jobdir}/OraToMySQL_${range[$i]}.xml
				sed -i "s!MySQLJDBC!${MySQLJDBC}!g" ${jobdir}/OraToMySQL_${range[$i]}.xml
				sed -i "s!MySQLCOL!${MySQLCOL}!g" ${jobdir}/OraToMySQL_${range[$i]}.xml
				sed -i "s!PRESQL!${PRESQL}!g" ${jobdir}/OraToMySQL_${range[$i]}.xml
				sed -i "s!TABLENAME!${TABLENAME}!g" ${jobdir}/OraToMySQL_${range[$i]}.xml
				echo "[OraToMySQL] Configuration file processing completed !"
				echo "[OraToMySQL] Start data synchronization ..."
				#MySQL关键词特殊处理-2
				sed -i 's/|/\\/g' ${jobdir}/OraToMySQL_${range[$i]}.xml
				#python ${dataxdir}/bin/datax.py ${jobdir}/OraToMySQL_${range[$i]}.xml
				echo "[OraToMySQL] Finish data synchronization !"
			else
				echo ${range[$i]} >>${tmpdir}/mysql_ne.log
				echo "[OraToMySQL] ${range[$i]} not exists in MySQL, data synchronization failure ,please check and try again!"
			fi
		else
			echo ${range[$i]} >>${tmpdir}/ora_ne.log
			echo "[OraToMySQL] ${range[$i]} not exists in oracle, please check and try again!"
		
		fi
	 echo >&6
    }&
done
wait

exec 6>&-
exec 6<&-

}

#---------------------参数
if [ $# == 10 ]
 then
  echo "Usage:
   sh OraToMySQL.sh ORAHOST ORAPORT ORASID ORAUSERNAME ORAPASSWORD MySQLHOST MySQLPORT MySQLSCHEMA MySQLUSERNAME MySQLPASSWORD
   ORAHOST: 	ORACLE服务器IP地址
   ORAPORT:		ORACLE端口
   ORASID：		ORACLE实例名称
   ORAUSERNAME:	ORACLE用户名
   ORAPASSWORD:	ORACLE密码
   MySQLHOST: 		MySQLHOST服务器IP地址
   MySQLPORT:		MySQLPORT端口
   MySQLSCHEMA:		MySQLSCHEMA数据库(Schema)
   MySQLUSERNAME:	MySQLUSERNAME用户名
   MySQLPASSWORD:	MySQLPASSWORD密码"
   
  ORAHOST=$1
  ORAPORT=$2
  ORASID=$3
  ORAUSERNAME=$4
  ORAPASSWORD=$5
  ORAJDBC="jdbc:oracle:thin:@${ORAHOST}:${ORAPORT}:${ORASID}"
  ORASQL=""
  
  MySQLHOST=$6
  MySQLPORT=$7
  MySQLSCHEMA=$8
  MySQLUSERNAME=$9
  MySQLPASSWORD=${10}
  MySQLJDBC="jdbc:mysql://${MySQLHOST}:${MySQLPORT}/${MySQLSCHEMA}"
  MySQLCOL=""
  MySQLSQL=""
  MySQLNAME=""
  #执行主程序
  OraToMySQL
else
  echo "
   入参错误,请参考
   Usage:
   sh OraToMySQL.sh ORAHOST ORAPORT ORASID ORAUSERNAME ORAPASSWORD MySQLHOST MySQLPORT MySQLSCHEMA MySQLUSERNAME MySQLPASSWORD
   ORAHOST: 	ORACLE服务器IP地址
   ORAPORT:		ORACLE端口
   ORASID：		ORACLE实例名称
   ORAUSERNAME:	ORACLE用户名
   ORAPASSWORD:	ORACLE密码
   MySQLHOST: 		MySQLHOST服务器IP地址
   MySQLPORT:		MySQLPORT端口
   MySQLSCHEMA:		MySQLSCHEMA数据库(Schema)
   MySQLUSERNAME:	MySQLUSERNAME用户名
   MySQLPASSWORD:	MySQLPASSWORD密码
   eg sh OraToMySQL.sh 10.45.15.201 1521 orcl tower_analy tower_analy 10.45.59.163 3306 mc_test test abc123"
   exit 0
fi



 



