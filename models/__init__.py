#!/usr/bin/python3
"""This has DBStorage and Filestorage"""
import os
storage_typ = os.getenv('HBNB_TYPE_STORAGE')


if storage_typ == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
