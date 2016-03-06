#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

import optparse
import logging
import os.path
import urlparse

import ConfigParser
import time
from datetime import datetime, date, time, timedelta

version = "0.1.0"
description = "Simple script for analyze HTTP access log"

HOME = os.path.expanduser('~')

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# 180.155.243.1 - - [11/Oct/2014:18:23:33 +0800] "GET /download/xitieapp_last.apk?f=weixin HTTP/1.1" 200 484734 "http://www.gangxu.co/?f=weixin" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0" -

PATTERN = r""".*?\[(?P<date>.*?)\:(?P<time>\d\d\:\d\d\:\d\d).*?\] "(?P<method>\w+) (?P<url>.*?)(?P<querystring>\?.*?)? HTTP\/.*?" """

logLine = re.compile(PATTERN, re.I)


# conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='huweifeng',port=3306,db='XII')
# cur=conn.cursor()

def str2datetime(st):
    """string date in format dd/Mon/aaaa:hh:mm:ss
    11/Apr/2011:16:06:10
    """
    dd, mmm, yyyy, hh, mm, ss = st[:2], st[3:6], st[7:11], st[12:14], st[15:17], st[18:20]
    return datetime(int(yyyy), MONTHS.index(mmm) + 1, int(dd), int(hh), int(mm), int(ss))


def str2date(st):
    dd, mmm, yyyy = st.split('/')
    return date(int(yyyy), MONTHS.index(mmm) + 1, int(dd))


def getTimestamp(st):
    yyyy, mm, dd, hh, ii, ss = st[:4], st[5:7], st[8:10], st[11:13], st[14:16], st[17:20]
    return str(time.mktime((int(yyyy), int(mm), int(dd), int(hh), int(ii), int(ss), 0, 0, 0))), int(yyyy), int(mm), int(
        dd)


def parseQuery(query):
    query_dict = {}
    param_dict = urlparse.parse_qs(query)

    for k in param_dict:
        query_dict[k] = param_dict[k][0]

    return query_dict


def analyze(options, logfile):
    log = open(logfile)

    # if options.verbose:
    #    logger.setLevel(logging.DEBUG)
    basename = os.path.basename(logfile)
    filename = os.path.splitext(basename)[0]

    registry = {}

    cnt = 0
    try:
        for l in log:
            cnt += 1
            matches = logLine.match(l)
            if matches is None:
                print
                "Line %d doesn't match the required format\n%s" % (cnt, l)
                # logger.warn()
                continue

            lineData = matches.groupdict()

            lastProcessedDate = lineData.get('date')
            lastProcessedTime = lineData.get('time')
            firstDateTime = str2datetime("%s:%s" % (lastProcessedDate, lastProcessedTime))

            # print firstDateTime
            if lineData['querystring'] is None:
                continue

            ref_date = str2date(lineData['date'])
            day = ref_date.strftime("%Y%m%d")

            q = parseQuery(lineData['querystring'])

            if not registry.get(day):
                registry[day] = {}
                registry[day]['scan'] = 0
                registry[day]['dowload'] = 0

            if lineData['url'] == '/index.php' and q.get('f') and q.get('f') == 'moka':
                registry[day]['scan'] += 1

            if lineData['url'] == '/download/xitieapp_last.apk' and q.get('f') and q.get('f') == 'moka':
                registry[day]['dowload'] += 1

            """
            if not registry.get(rdtable):
                registry[rdtable] = []
            registry[rdtable].append(sql)
            """
    except KeyboardInterrupt:
        # first CTRL+C don't stop the program
        print
        "\nEnough... stopped by user"
    except:
        # print lineData
        # logger.exception("Error parsing log at line %d\n%s" % (cnt, l))
        raise

    print(registry)
    # conn.commit()
    # conn.close()
    log.close()


def main():
    args = sys.argv[1:]

    defaults = {'size': 50, 'start-date': None, 'includes': [], 'excludes': []}

    usage = "usage: %prog [options] logfile"
    p = optparse.OptionParser(usage=usage, version="%prog " + version, description=description, prog="tinylogan")
    p.remove_option("--help")
    p.add_option('--help', '-h', action="store_true", default=False, help='show this help message and exit')
    p.add_option('--size', '-s', type="int", dest="size", default=10,
                 help="choose the number of record to store in every log")
    p.add_option('--include', '-i', dest="includes", default=defaults['includes'], action="append",
                 metavar="INCLUDE_REGEX")
    p.add_option('--exclude', '-e', dest="excludes", default=defaults['excludes'], action="append",
                 metavar="EXCLUDE_REGEX")
    p.add_option('--start-date', dest="start_date", default=0, help="date where to start analyze and record")

    options, arguments = p.parse_args(args)

    if options.help or not arguments:
        p.print_help()
        sys.exit(0)

    try:
        analyze(options, arguments[0])
    except KeyboardInterrupt:
        print
        "Stopped by user"
        sys.exit(1)


if __name__ == '__main__':
    main()
