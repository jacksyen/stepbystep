#!/usr/bin/env python

### Set of usefull scripts for everyday work

#### Setup
# Copy or make symlinks to `/usr/bin` or `/home/{your-username}/bin`

##### tomcat
# Script for controlling tomcat :starting, shutting down, restarting, deploying apps. `CATALINA_HOME` enviroment variable is required for this script to work correctly.

#   tomcat deploy 1.war 2.war 3.war # deploy all listed files and restart
#   tomcat stop                     # stop
#   tomcat start                    # start
#   tomcat restart                  # restart

##### builddoc
# Build projects `README` (written in [markdown](http://daringfireball.net/projects/markdown/)) to html.
# Uses [ReMarkdown](http://fvsch.com/code/remarkdown/) for styling.

#  builddoc README.markdown > README.html

import argparse
import os
import shutil
import sys
import time

TOM = 'CATALINA_HOME'


def main(args):
    tomcat = argparse.ArgumentParser(prog='tomcat', description='tomcat helper script')
    cmds = tomcat.add_subparsers(title='commands')

    deploy = add_sub(cmds, 'deploy', 'Deploy all listed `files` and restart.')
    deploy.add_argument('files', nargs='+', type=argparse.FileType('r'),
                        help='list of files to process')
    add_sub(cmds, 'restart', 'Restart tomcat.')
    add_sub(cmds, 'start', 'Start tomcat.')
    add_sub(cmds, 'stop', 'Stop tomcat.')

    a = tomcat.parse_args(args)
    switch_exec(a, ['deploy',
                    'restart',
                    'start',
                    'stop'])


def add_sub(cmds, name, help=''):
    cmd = cmds.add_parser(name, help=help)
    cmd.add_argument(name, action='store_true')
    return cmd


def switch_exec(a, commands):
    def deploy(a):
        for f in a.files:
            shutil.copy(f.name, '{}/webapps'.format(tomcat_path()))
        restart()

    def restart(a=None):
        stop()
        time.sleep(2)
        start()

    def stop(a=None):
        os.system("sh {}/bin/catalina.sh stop".format(tomcat_path()))

    def start(a=None):
        os.system("sh {}/bin/catalina.sh start".format(tomcat_path()))

    for cmd in commands:
        if hasattr(a, cmd):
            locals()[cmd](a)


def tomcat_path():
    try:
        return os.environ[TOM]
    except KeyError as e:
        raise Exception('{0} variable should be specified'.format(TOM), e)


if __name__ == '__main__':
    main(sys.argv[1:])
