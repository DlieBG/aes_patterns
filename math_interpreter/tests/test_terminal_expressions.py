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
        
    def test_constant_negative(self):
        """Test Constant with negative value."""
        constant = Constant(-10)
        context = Context()
        
        # Test interpretation
        self.assertEqual(constant.interpret(context), -10.0)
        
        # Test string representation
        self.assertEqual(str(constant), "-10")
        
    def test_constant_zero(self):
        """Test Constant with zero value."""
        constant = Constant(0)
        context = Context()
        
        # Test interpretation
        self.assertEqual(constant.interpret(context), 0.0)
        
        # Test string representation
        self.assertEqual(str(constant), "0")
        
    def test_constant_large_number(self):
        """Test Constant with a large number."""
        large_value = 1000000.5
        constant = Constant(large_value)
        context = Context()
        
        # Test interpretation
        self.assertEqual(constant.interpret(context), large_value)
        
        # Test string representation
        self.assertEqual(str(constant), "1000000.5")


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
        
    def test_variable_with_special_characters(self):
        """Test Variable with special characters in name."""
        variable = Variable("var_1")
        context = Context()
        context.set_variable("var_1", 42)
        
        # Test interpretation
        self.assertEqual(variable.interpret(context), 42)
        
        # Test string representation
        self.assertEqual(str(variable), "var_1")
        
    def test_multiple_variables(self):
        """Test multiple variables in the same context."""
        var_x = Variable("x")
        var_y = Variable("y")
        context = Context()
        
        # Set variables
        context.set_variable("x", 10)
        context.set_variable("y", 20)
        
        # Test interpretation
        self.assertEqual(var_x.interpret(context), 10)
        self.assertEqual(var_y.interpret(context), 20)
        
    def test_variable_with_float_value(self):
        """Test Variable with floating-point value."""
        variable = Variable("pi")
        context = Context()
        context.set_variable("pi", 3.14159)
        
        # Test interpretation
        self.assertEqual(variable.interpret(context), 3.14159)
        
    def test_variable_with_negative_value(self):
        """Test Variable with negative value."""
        variable = Variable("neg")
        context = Context()
        context.set_variable("neg", -25.5)
        
        # Test interpretation
        self.assertEqual(variable.interpret(context), -25.5)


if __name__ == "__main__":
    unittest.main()