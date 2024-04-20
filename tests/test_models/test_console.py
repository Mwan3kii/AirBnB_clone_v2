import unittest
from console import HBNBCommand
from models import storage
from datetime import datetime


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


if __name__ == "__main__":
    unittest.main()
