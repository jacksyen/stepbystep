# -*- coding: utf8 -*-

import MySQLdb

class SlowLogDAO():
    def __init__(self, slowlog):
        self.conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="test",charset="utf8")
        self.cursor = self.conn.cursor()
        self.slowlog = slowlog
        self.conn.autocommit(1)


    def update(self):
        try:
            sql ="INSERT INTO test.slow_logs "
            sql += "	(query_time, "
            sql += "	lock_time, "
            sql += "	rows_sent, "
            sql += "	rows_examined, "
            sql += "	rows_affected, "
            sql += "	sql_detail, "
            sql += "	created_time, "
            sql += "	update_time"
            sql += "	)"
            sql += "	VALUES"
            sql += "	("+self.slowlog._query_time+", "
            sql += "	"+self.slowlog._lock_time+", "
            sql += "	"+self.slowlog._rows_sent+", "
            sql += "	"+self.slowlog._rows_examined+", "
            sql += "	"+self.slowlog._rows_affected+", "
            sql += "	\""+self.slowlog._sql + "\", "
            sql += "	NOW(), "
            sql += "	NOW()"
            sql += "	)"
            print sql
            n= self.cursor.execute(sql)
            print n
            self.conn.commit()
            print "insert successfully"

        except Exception,data:
            print Exception,":",data
            self.conn.rollback()
        finally:
            self.cursor.close
            self.conn.close()


