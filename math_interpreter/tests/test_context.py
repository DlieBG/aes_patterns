"""
Tests for the Context class.
"""

import unittest
from math_interpreter.context import Context
from math_interpreter.exceptions import VariableNotDefinedError


class TestContext(unittest.TestCase):
    """Test cases for the Context class."""

    def setUp(self):
        """Set up a new context for each test."""
        self.context = Context()

    def test_set_and_get_variable(self):
        """Test setting and getting a variable."""
        self.context.set_variable("x", 10.5)
        self.assertEqual(self.context.get_variable("x"), 10.5)

    def test_has_variable(self):
        """Test checking if a variable exists."""
        self.context.set_variable("y", 20)
        self.assertTrue(self.context.has_variable("y"))
        self.assertFalse(self.context.has_variable("z"))

    def test_get_undefined_variable(self):
        """Test getting an undefined variable raises an error."""
        with self.assertRaises(VariableNotDefinedError):
            self.context.get_variable("undefined")

    def test_update_variable(self):
        """Test updating a variable value."""
        self.context.set_variable("a", 5)
        self.assertEqual(self.context.get_variable("a"), 5)
        
        # Update the variable
        self.context.set_variable("a", 10)
        self.assertEqual(self.context.get_variable("a"), 10)


if __name__ == "__main__":
    unittest.main()