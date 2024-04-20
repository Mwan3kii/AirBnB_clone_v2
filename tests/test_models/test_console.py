import unittest
from console import HBNBCommand
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
import json
import MySQLdb
import os
import sqlalchemy
import unittest
from tests import clear_stream
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Test cases for the command in the console."""
    def test_missing_class_name(self):
        test_output = HBNBCommand().onecmd("create")
        self.assertIn("** class name missing **", test_output)

    def test_non_existent_class_name(self):
        """test"""
        test_output = HBNBCommand().onecmd("create SomeClass")
        self.assertIn("** class doesn't exist **", test_output)

    def test_valid_class_name_with_parameters(self):
        test_output = HBNBCommand().onecmd("create State name=\"California\"")
        self.assertTrue(test_output.startswith("(hbnb)"))

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_fs_create(self):
        """Tests create command with the file storage."""
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            cons.onecmd('create City name="Texas"')
            mdl_id = cout.getvalue().strip()
            clear_stream(cout)
            self.assertIn('City.{}'.format(mdl_id), storage.all().keys())
            cons.onecmd('show City {}'.format(mdl_id))
            self.assertIn("'name': 'Texas'", cout.getvalue().strip())
            clear_stream(cout)
            cons.onecmd('create User name="James" age=17 height=5.9')
            mdl_id = cout.getvalue().strip()
            self.assertIn('User.{}'.format(mdl_id), storage.all().keys())
            clear_stream(cout)
            cons.onecmd('show User {}'.format(mdl_id))
            self.assertIn("'name': 'James'", cout.getvalue().strip())
            self.assertIn("'age': 17", cout.getvalue().strip())
            self.assertIn("'height': 5.9", cout.getvalue().strip())

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_create(self):
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            with self.assertRaises(sqlalchemy.exc.OperationalError):
                cons.onecmd('create User')
            clear_stream(cout)
            cons.onecmd('create User email="john25@gmail.com" password="123"')
            mdl_id = cout.getvalue().strip()
            dbc = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = dbc.cursor()
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(mdl_id))
            result = cursor.fetchone()
            self.assertTrue(result is not None)
            self.assertIn('john25@gmail.com', result)
            self.assertIn('123', result)
            cursor.close()
            dbc.close()


if __name__ == "__main__":
    unittest.main()
