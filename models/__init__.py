#!/usr/bin/python3
"""This has DBStorage and Filestorage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
