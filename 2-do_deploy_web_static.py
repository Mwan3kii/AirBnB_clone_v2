#!/usr/bin/python3
"""Fabric script thats distributes archive web servers"""
from fabric.api import local
from datetime import datetime
import os
from fabric.api import *
import os
env.hosts = ["35.174.176.33", "54.152.129.84"]
env.user = 'ubuntu'


def do_pack():
    """Returns path to the created archive"""
    if not os.path.exists("versions"):
        os.makedirs("versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    stamp_name = f"versions/web_static_{timestamp}.tgz"
    result = local(f"tar -cvzf {stamp_name} web_static")
    if result.failed:
        return None
    return stamp_name


def do_deploy(archive_path):
    """False if the file at the path archive_path doesn’t exist"""
    if not os.path.exists(archive_path):
        return False
    archive_name = os.path.basename(archive_path)
    folder = archive_name.split(".")[0]
    put(archive_path, f"/tmp/{archive_name}")
    run(f"mkdir -p /data/web_static/releases/{folder}/")
    run(f"tar -xzf /tmp/{archive_name} -C /data/web_static/releases/{folder}/")
    run(f"rm -rf /data/web_static/releases/{folder}/web_static")
    run(f"rm /tmp/{archive_name}")
    run(f"rm -rf /data/web_static/current")
    run(f"ln -s /data/web_static/releases/{folder}/ /data/web_static/current")
    return True
