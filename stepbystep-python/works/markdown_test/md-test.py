__author__ = 'patrick'
# !/usr/bin/python
import sys
import subprocess
import os
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-f", "--file", dest="file", help="The markdown file to convert")
(options, args) = parser.parse_args()


def main():
    print
    'Converting', os.path.abspath(options.file)

    if not (options.file):
        print
        "No file specified, exiting"
        sys.exit(1)

    # with  as output_f:
    # print 'Output will goto %s.html' % os.path.abspath(options.file)
    p = subprocess.Popen('markdown %s' % options.file,
                         stdout=subprocess.PIPE,
                         shell=True)

    output_file = open('%s.html' % options.file, 'w+')  # TODO Add date or something too?

    output_file.write("""<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>test.md.html</title>
		<script type="text/javascript" src="mootools.js"></script>
		<script type="text/javascript" src="tests.js"></script>
		<link href="tests.css" rel='stylesheet' type='text/css'>
	</head>
	<body>
	""")
    output_file.write(p.stdout.read())
    output_file.write("""
	</body>
</html>
	""")


main()
