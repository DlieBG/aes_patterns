"""
Tests for non-terminal expressions in the Math Interpreter.

This module contains comprehensive tests for the non-terminal expressions
(Addition and Multiplication) in the Math Interpreter, covering requirements
3.1, 3.2, 3.3, 4.1, 4.2, and 4.3.
"""

import unittest
from math_interpreter.terminal_expressions import Constant, Variable
from math_interpreter.non_terminal_expressions import Addition, Multiplication
from math_interpreter.context import Context
from math_interpreter.exceptions import VariableNotDefinedError


class TestAddition(unittest.TestCase):
    """Test cases for the Addition non-terminal expression."""
    
    def test_addition_constants(self):
        """Test Addition with two constants (Requirement 3.1)."""
        # 2 + 3 = 5
        expr = Addition(Constant(2), Constant(3))
        context = Context()
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 5.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(2 + 3)")
    
    def test_addition_variables(self):
        """Test Addition with two variables (Requirement 3.2)."""
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
        """Test Addition with mixed operands (constant and variable) (Requirement 3.3)."""
        # 7 + z where z = 3
        expr = Addition(Constant(7), Variable("z"))
        context = Context()
        context.set_variable("z", 3)
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 10.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(7 + z)")
    
    def test_addition_chained(self):
        """Test chained Addition operations (Requirement 3.4)."""
        # (2 + 3) + 4 = 9
        expr = Addition(Addition(Constant(2), Constant(3)), Constant(4))
        context = Context()
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 9.0)
        
        # Test string representation
        self.assertEqual(str(expr), "((2 + 3) + 4)")
    
    def test_addition_floating_point(self):
        """Test Addition with floating-point numbers."""
        # 2.5 + 3.7 = 6.2
        expr = Addition(Constant(2.5), Constant(3.7))
        context = Context()
        
        # Test interpretation
        self.assertAlmostEqual(expr.interpret(context), 6.2)
        
        # Test string representation
        self.assertEqual(str(expr), "(2.5 + 3.7)")
    
    def test_addition_negative_numbers(self):
        """Test Addition with negative numbers."""
        # -5 + 3 = -2
        expr = Addition(Constant(-5), Constant(3))
        context = Context()
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), -2.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(-5 + 3)")
    
    def test_addition_with_zero(self):
        """Test Addition with zero."""
        # 0 + x where x = 42
        expr = Addition(Constant(0), Variable("x"))
        context = Context()
        context.set_variable("x", 42)
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 42.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(0 + x)")
    
    def test_addition_undefined_variable(self):
        """Test Addition with undefined variable."""
        # 5 + y where y is undefined
        expr = Addition(Constant(5), Variable("y"))
        context = Context()
        
        # Test interpretation raises VariableNotDefinedError
        with self.assertRaises(VariableNotDefinedError):
            expr.interpret(context)
    
    def test_addition_complex_expression(self):
        """Test Addition in a more complex expression."""
        # (x + y) + (a + b) where x=1, y=2, a=3, b=4
        expr = Addition(
            Addition(Variable("x"), Variable("y")),
            Addition(Variable("a"), Variable("b"))
        )
        context = Context()
        context.set_variable("x", 1)
        context.set_variable("y", 2)
        context.set_variable("a", 3)
        context.set_variable("b", 4)
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 10.0)
        
        # Test string representation
        self.assertEqual(str(expr), "((x + y) + (a + b))")


class TestMultiplication(unittest.TestCase):
    """Test cases for the Multiplication non-terminal expression."""
    
    def test_multiplication_constants(self):
        """Test Multiplication with two constants (Requirement 4.1)."""
        # 2 * 3 = 6
        expr = Multiplication(Constant(2), Constant(3))
        context = Context()
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 6.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(2 * 3)")
    
    def test_multiplication_variables(self):
        """Test Multiplication with two variables (Requirement 4.2)."""
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
        """Test Multiplication with mixed operands (constant and variable) (Requirement 4.3)."""
        # 7 * z where z = 3
        expr = Multiplication(Constant(7), Variable("z"))
        context = Context()
        context.set_variable("z", 3)
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 21.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(7 * z)")
    
    def test_multiplication_chained(self):
        """Test chained Multiplication operations (Requirement 4.4)."""
        # (2 * 3) * 4 = 24
        expr = Multiplication(Multiplication(Constant(2), Constant(3)), Constant(4))
        context = Context()
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 24.0)
        
        # Test string representation
        self.assertEqual(str(expr), "((2 * 3) * 4)")
    
    def test_multiplication_floating_point(self):
        """Test Multiplication with floating-point numbers."""
        # 2.5 * 3.2 = 8.0
        expr = Multiplication(Constant(2.5), Constant(3.2))
        context = Context()
        
        # Test interpretation
        self.assertAlmostEqual(expr.interpret(context), 8.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(2.5 * 3.2)")
    
    def test_multiplication_negative_numbers(self):
        """Test Multiplication with negative numbers."""
        # -5 * 3 = -15
        expr = Multiplication(Constant(-5), Constant(3))
        context = Context()
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), -15.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(-5 * 3)")
        
        # -5 * -3 = 15
        expr2 = Multiplication(Constant(-5), Constant(-3))
        self.assertEqual(expr2.interpret(context), 15.0)
    
    def test_multiplication_with_zero(self):
        """Test Multiplication with zero."""
        # 0 * x where x = 42
        expr = Multiplication(Constant(0), Variable("x"))
        context = Context()
        context.set_variable("x", 42)
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 0.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(0 * x)")
    
    def test_multiplication_with_one(self):
        """Test Multiplication with one."""
        # 1 * x where x = 42
        expr = Multiplication(Constant(1), Variable("x"))
        context = Context()
        context.set_variable("x", 42)
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 42.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(1 * x)")
    
    def test_multiplication_undefined_variable(self):
        """Test Multiplication with undefined variable."""
        # 5 * y where y is undefined
        expr = Multiplication(Constant(5), Variable("y"))
        context = Context()
        
        # Test interpretation raises VariableNotDefinedError
        with self.assertRaises(VariableNotDefinedError):
            expr.interpret(context)
    
    def test_multiplication_complex_expression(self):
        """Test Multiplication in a more complex expression."""
        # (x * y) * (a * b) where x=2, y=3, a=4, b=5
        expr = Multiplication(
            Multiplication(Variable("x"), Variable("y")),
            Multiplication(Variable("a"), Variable("b"))
        )
        context = Context()
        context.set_variable("x", 2)
        context.set_variable("y", 3)
        context.set_variable("a", 4)
        context.set_variable("b", 5)
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 120.0)
        
        # Test string representation
        self.assertEqual(str(expr), "((x * y) * (a * b))")


class TestMixedOperations(unittest.TestCase):
    """Test cases for mixed operations (Addition and Multiplication)."""
    
    def test_addition_and_multiplication(self):
        """Test mixed Addition and Multiplication operations."""
        # 2 + 3 * 4 = 2 + 12 = 14
        expr = Addition(
            Constant(2),
            Multiplication(Constant(3), Constant(4))
        )
        context = Context()
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 14.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(2 + (3 * 4))")
    
    def test_multiplication_and_addition(self):
        """Test mixed Multiplication and Addition operations."""
        # 2 * (3 + 4) = 2 * 7 = 14
        expr = Multiplication(
            Constant(2),
            Addition(Constant(3), Constant(4))
        )
        context = Context()
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 14.0)
        
        # Test string representation
        self.assertEqual(str(expr), "(2 * (3 + 4))")
    
    def test_complex_mixed_expression(self):
        """Test complex expression with mixed operations and variables."""
        # (x + y) * (a + b) where x=1, y=2, a=3, b=4
        # (1 + 2) * (3 + 4) = 3 * 7 = 21
        expr = Multiplication(
            Addition(Variable("x"), Variable("y")),
            Addition(Variable("a"), Variable("b"))
        )
        context = Context()
        context.set_variable("x", 1)
        context.set_variable("y", 2)
        context.set_variable("a", 3)
        context.set_variable("b", 4)
        
        # Test interpretation
        self.assertEqual(expr.interpret(context), 21.0)
        
        # Test string representation
        self.assertEqual(str(expr), "((x + y) * (a + b))")


if __name__ == "__main__":
    unittest.main()