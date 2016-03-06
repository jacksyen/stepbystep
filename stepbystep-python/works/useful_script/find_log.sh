#!/usr/bin/env bash

if [ $# -eq 0 ]; then
	cat << HELP
Usage: run.sh LOGPATH [filename]
HELP
	exit 0;
fi

ROOTPATH=`pwd`
ANALYSISBIN="$ROOTPATH/analysis.py"

LOGPATH=$1
filename=$2

if [ ! -d $LOGPATH ]; then
	echo "ERROR: ${LOGPATH} does not exist"
	exit 0;
fi

if [ ! $filename ]; then
	ymd=`date +%Y%m%d`
	filename=`echo "$ymd - 1" | bc`	
fi

echo "searching file $filename ...."

filelist=`find $LOGPATH -name *.log`

for file in $filelist;do

	str=`basename $file`
	
	if [ $filename = ${str%.*} ];then
		echo "analysis $file ... please wait"
		python $ANALYSISBIN $file
	fi
done

echo "done"