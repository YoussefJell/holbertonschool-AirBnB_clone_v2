#!/usr/bin/python3
"""1-pack_web_static Module"""
from datetime import datetime
from fabric.api import local
from os.path import exists


def do_pack():
    """generates a .tgz archive from the contents of the
        web_static folder of repo"""
    date = datetime.now()
    filedate = date.strftime('%Y%m%d%H%M%S')
    local("mkdir -p versions")
    local(
        "tar -cvzf versions/web_static_{0}.tgz web_static".format(filedate))
    if exists("versions/web_static_{0}.tgz".format(filedate)):
        return "versions/web_static_{0}.tgz".format(filedate)
    return False
