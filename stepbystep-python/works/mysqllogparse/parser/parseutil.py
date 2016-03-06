# -*- coding: utf8 -*-

import re
import string

from works.mysqllogparse.parser.slowlogdao import SlowLogDAO


_DATE_PAT = r"\d{6}\s+\d{1,2}:\d{2}:\d{2}"

_HEADER_VERSION_CRE = re.compile(r"(.+), Version: (\d+)\.(\d+)\.(\d+)(?:-(\S+))?")
_HEADER_SERVER_CRE = re.compile(r"Tcp port:\s*(\d+)\s+Unix socket:\s+(.*)")

_SLOW_TIMESTAMP_CRE = re.compile(r"#\s+Time:\s+(" + _DATE_PAT + r")")
_SLOW_USERHOST_CRE = re.compile(r"#\s+User@Host:\s+"
                                r"(?:([\w\d]+))?\s*"
                                r"\[\s*([\w\d]+)\s*\]\s*"
                                r"@\s*"
                                r"([\w\d]*)\s*"
                                r"\[\s*([\d.]*)\s*\]")

_SLOW_SCHEMA_INFO = re.compile(r"#\s+Schema:")
_SLOW_BYTES = re.compile(r"#\s+Bytes_sent:")
_SLOW_STATS_CRE = re.compile(r"#\sQuery_time:\s(\d*\.\d{1,6})\s*"
                             r"Lock_time:\s(\d*\.\d{1,6})\s*"
                             r"Rows_sent:\s(\d*)\s*"
                             r"Rows_examined:\s(\d*)")
_SLOW_COMMAND = re.compile(r"Time")
_SET_TIMESTAMP = re.compile(r"SET timestamp=")
_USE_DB = re.compile(r"use")

_GENERAL_ENTRY_CRE = re.compile(
    r'(?:(' + _DATE_PAT + '))?\s*'
                          r'(\d+)\s([\w ]+)\t*(?:(.+))?$')

_CSV_HEADER = "Query_time,Lock_time,Rows_sent,Rows_examined,Rows_affected,sql"

class SlowLogParser(object):
    def __init__(self):
        self.init_data()
        self.is_header_written = False

    @staticmethod
    def is_header_info(self, line):
        return _HEADER_VERSION_CRE.match(line)

    @staticmethod
    def is_server_info(self, line):
        return _HEADER_SERVER_CRE.match(line)

    @staticmethod
    def is_timestamp_info(self, line):
        return _SLOW_TIMESTAMP_CRE.match(line)

    staticmethod
    def is_slow_host_info(self, line):
        return _SLOW_USERHOST_CRE.match(line)

    @staticmethod
    def is_slow_state_trace(self, line):
        return _SLOW_STATS_CRE.match(line)

    @staticmethod
    def is_slow_log_command(self, line):
        return _SLOW_COMMAND.match(line)

    @staticmethod
    def is_slow_log_schema(self, line):
        return _SLOW_SCHEMA_INFO.match(line)

    @staticmethod
    def is_slow_log_byte(self, line):
        return _SLOW_BYTES.match(line)

    @staticmethod
    def is_set_timestamp(self, line):
        return _SET_TIMESTAMP.match(line)

    @staticmethod
    def is_use_statement(self, line):
        return _USE_DB.match(line)


    def is_sql_info(self, line):
        if self.is_header_info(line):
            return False
        if self.is_server_info(line):
            return False
        if self.is_slow_host_info(line):
            return False
        if self.is_timestamp_info(line):
            return False
        if self.is_slow_state_trace(line):
            return False
        if self.is_slow_log_byte(line):
            return False
        if self.is_slow_log_command(line):
            return False
        if self.is_slow_log_schema(line):
            return False
        if self.is_set_timestamp(line):
            return False
        if self.is_use_statement(line):
            return False
        return True

    def parse(self, line):
        """
            get the query time and other info
            output to a csv file
            only output the query time and sql info
            the parse step:
        :param line:
        :return:
        """
        # parser header
        if self.is_slow_state_trace(line):
            if self._query_stat is None:
                self._query_stat = line
            else:
                self.write_to_file()
                self.init_data()
                self._query_stat = line
        if self.is_sql_info(line):
            if self._sql is None:
                self._sql = line
            else:
                self._sql = self._sql +" "+str(line.strip().replace("\n","").replace("\t",""))


    def write_to_file(self):
        #print self._query_stat
        #print self._sql
        print self.parse_query_stat()+self._sql
        f = open("mysql_log.csv","a")
        if not self.is_header_written:
            f.writelines(_CSV_HEADER)
            f.write("\n")
            self.is_header_written = True
        else:
            f.writelines(self.parse_query_stat()+self._sql)

    def init_data(self):
        self._query_time = None
        self._lock_time = None
        self._rows_sent = None
        self._rows_examined = None
        self._sql = None
        self.is_full_log = False
        self._query_stat = None
        self._rows_affected = None


    def parse_query_stat(self):
        temp = string.replace(self._query_stat,"#","")
        temp = string.split(temp)
        stat_out=""
        for i in range(len(temp)):

            if(i%2!=0):
                stat_out=stat_out+temp[i]+","
        return stat_out

    # todo add to mysql database

    def parse_for_db(self):
        temp = string.replace(self._query_stat,"#","")
        temp = string.split(temp)
        self._query_time = string.strip(temp[1])
        self._lock_time=string.strip(temp[3])
        self._rows_sent=string.strip(temp[5])
        self._rows_examined=string.strip(temp[7])
        self._rows_affected=string.strip(temp[9])


    def write_to_db(self,query_time_threshold):
        #print self._query_stat
        #print self._sql
        self.parse_for_db()
        if float(self._query_time) > query_time_threshold:
            print query_time_threshold
            print self._query_time
            dao = SlowLogDAO(self)
            dao.update()


    def parse_to_db(self, line, query_time_threshold=0):
        """
            get the query time and other info
            output to a csv file
            only output the query time and sql info
            the parse step:
        :param line:
        :return:
        """
        # parser header
        if self.is_slow_state_trace(line):
            if self._query_stat is None:
                self._query_stat = line
            else:
               self.write_to_db(query_time_threshold)
               self.init_data()
               self._query_stat = line

        if self.is_sql_info(line):
            if self._sql is None:
                self._sql = line
            else:
                self._sql = self._sql +" "+str(line.strip().replace("\n","").replace("\t",""))


count = 0
parser = SlowLogParser()
with open("mysql-slow-61.log", "r") as log:
    for line in log:
        count += 1
<<<<<<< HEAD
        try:
            parser.parse_to_db(line)
        except BaseException,e:
            print e.args,e.message
=======
        parser.parse_to_db(line, 5)

>>>>>>> 7052cefef9edeeb7bfdb9636701b9550682608b1
print count