#!/usr/bin/python3
"""generates a .tgz archive from web_static folder of AirBnB using do pack"""
from fabric.api import local
from datetime import datetime
import os


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
