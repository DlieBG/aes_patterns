"""
Tests for non-terminal expressions in the Math Interpreter.
"""

import unittest
from math_interpreter.terminal_expressions import Constant, Variable
from math_interpreter.non_terminal_expressions import Addition, Multiplication
from math_interpreter.context import Context


class TestAddition(unittest.TestCase):
    """Test cases for the Addition non-terminal expression."""
    
    def test_addition_constants(self):
        """Test Addition with two constants."""
        # 2 + 3 = 5
        expr = Addition(Constant(2), Constant(3))
        context = Context()
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 5.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(2 + 3)")
    
    def test_addition_variables(self):
        """Test Addition with two variables."""
        # x + y where x = 10, y = 5
        expr = Addition(Variable("x"), Variable("y"))
        context = Context()
        context.set_variable("x", 10)
        context.set_variable("y", 5)
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 15.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(x + y)")
    
    def test_addition_mixed(self):
        """Test Addition with mixed operands (constant and variable)."""
        # 7 + z where z = 3
        expr = Addition(Constant(7), Variable("z"))
        context = Context()
        context.set_variable("z", 3)
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 10.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(7 + z)")
    
    def test_addition_chained(self):
        """Test chained Addition operations."""
        # (2 + 3) + 4 = 9
        expr = Addition(Addition(Constant(2), Constant(3)), Constant(4))
        context = Context()
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 9.0)
        
        # Test string representation
        self.assertEqual(str(expr), "((2 + 3) + 4)")


class TestMultiplication(unittest.TestCase):
    """Test cases for the Multiplication non-terminal expression."""
    
    def test_multiplication_constants(self):
        """Test Multiplication with two constants."""
        # 2 * 3 = 6
        expr = Multiplication(Constant(2), Constant(3))
        context = Context()
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 6.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(2 * 3)")
    
    def test_multiplication_variables(self):
        """Test Multiplication with two variables."""
        # x * y where x = 4, y = 5
        expr = Multiplication(Variable("x"), Variable("y"))
        context = Context()
        context.set_variable("x", 4)
        context.set_variable("y", 5)
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 20.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(x * y)")
    
    def test_multiplication_mixed(self):
        """Test Multiplication with mixed operands (constant and variable)."""
        # 7 * z where z = 3
        expr = Multiplication(Constant(7), Variable("z"))
        context = Context()
        context.set_variable("z", 3)
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 21.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(7 * z)")
    
    def test_multiplication_chained(self):
        """Test chained Multiplication operations."""
        # (2 * 3) * 4 = 24
        expr = Multiplication(Multiplication(Constant(2), Constant(3)), Constant(4))
        context = Context()
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 24.0)
        
        # Test string representation
        self.assertEqual(str(expr), "((2 * 3) * 4)")


if __name__ == "__main__":
    unittest.main()