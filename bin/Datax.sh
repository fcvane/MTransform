#!/bin/bash
#Usage 批量执行xml

tabdir=/home/script/job
dataxdir=/home/script/datax/bin

#创建管道
mkfifo testfifo
exec 6<>testfifo
rm -rf testfifo
#并发数控制
thread=6
for ((i=0;i<=$thread;i++))
do
 echo >&6
done


range=(`ls -l ${tabdir} | awk '{print $9}'`)
len=${#range[@]}
#遍历
for ((i=0;i<$len;i++))
do
    read -u6
    {
		python ${dataxdir}/datax.py ${tabdir}/${range[$i]}
		echo >&6
    }&
done
wait

exec 6>&-
exec 6<&-
