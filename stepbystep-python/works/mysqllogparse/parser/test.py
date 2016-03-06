# -*- coding: utf8 -*-
import string

result = []
test = "# Query_time: 59.594316  Lock_time: 0.001526  Rows_sent: 0  Rows_examined: 181440  Rows_affected: 0"
test = string.replace(test, "#", "")
test = string.split(test)

for i in range(len(test)):
#    if(i%2!=0):
#        print test[i]
    if(i%2==0):
        print test[i]


header = "Query_time,Lock_time,Rows_sent,Rows_examined,Rows_affected,sql"