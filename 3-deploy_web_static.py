#!/usr/bin/python3
"""3-deploy_web_static Module"""
from datetime import datetime
from fabric.api import *
from os.path import exists

env.hosts = [
    '3.80.219.47',
    '54.152.66.53'
]


@runs_once
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


def do_deploy(archive_path):
    """distributes an archive to your web servers
    using the function do_deploy"""
    if exists(archive_path):

        archive_name = archive_path.split('/')[-1]
        my_folder = archive_name.split('.')[0]
        releases_path = "/data/web_static/releases/{0}/".format(my_folder)
        archive_remote_path = "/tmp/{0}".format(archive_name)

        put(archive_path, archive_remote_path)

        run("mkdir -p {}".format(releases_path))

        run("tar -zxf {0} -C {1}".format(archive_remote_path,
                                         releases_path))

        run("rm {0}".format(archive_remote_path))

        run("mv -f {}web_static/* {}".format(releases_path, releases_path))

        run("rm -rf {}web_static".format(releases_path))

        run("rm -rf /data/web_static/current")

        run("ln -s {0} /data/web_static/current".format(releases_path))

        return True

    return False


def deploy():
    """creates and distributes an archive to your web servers
    using the function deploy"""
    created_archive = do_pack()
    if created_archive is False:
        return False
    return do_deploy(created_archive)
