"""
Tests for terminal expressions in the Math Interpreter.
"""

import unittest
from math_interpreter.terminal_expressions import Constant, Variable
from math_interpreter.context import Context
from math_interpreter.exceptions import VariableNotDefinedError


class TestConstant(unittest.TestCase):
    """Test cases for the Constant terminal expression."""
    
    def test_constant_integer(self):
        """Test Constant with integer value."""
        constant = Constant(5)
        context = Context()
        
        # Test interpretation
        self.assertEqual(constant.interpret(context), 5.0)
        
        # Test string representation
        self.assertEqual(str(constant), "5")
    
    def test_constant_float(self):
        """Test Constant with floating-point value."""
        constant = Constant(3.14)
        context = Context()
        
        # Test interpretation
        self.assertEqual(constant.interpret(context), 3.14)
        
        # Test string representation
        self.assertEqual(str(constant), "3.14")
    
    def test_constant_integer_equivalent(self):
        """Test Constant with float that is equivalent to an integer."""
        constant = Constant(5.0)
        context = Context()
        
        # Test interpretation
        self.assertEqual(constant.interpret(context), 5.0)
        
        # Test string representation (should be "5", not "5.0")
        self.assertEqual(str(constant), "5")


class TestVariable(unittest.TestCase):
    """Test cases for the Variable terminal expression."""
    
    def test_variable_defined(self):
        """Test Variable with defined variable."""
        variable = Variable("x")
        context = Context()
        context.set_variable("x", 10)
        
        # Test interpretation
        self.assertEqual(variable.interpret(context), 10)
        
        # Test string representation
        self.assertEqual(str(variable), "x")
    
    def test_variable_undefined(self):
        """Test Variable with undefined variable."""
        variable = Variable("y")
        context = Context()
        
        # Test interpretation raises VariableNotDefinedError
        with self.assertRaises(VariableNotDefinedError):
            variable.interpret(context)
    
    def test_variable_update(self):
        """Test Variable with updated value."""
        variable = Variable("z")
        context = Context()
        
        # Set initial value
        context.set_variable("z", 5)
        self.assertEqual(variable.interpret(context), 5)
        
        # Update value
        context.set_variable("z", 15)
        self.assertEqual(variable.interpret(context), 15)


if __name__ == "__main__":
    unittest.main()