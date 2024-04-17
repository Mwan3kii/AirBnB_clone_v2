#!/usr/bin/python3
"""This has DBStorage and Filestorage"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
storage.reload()
