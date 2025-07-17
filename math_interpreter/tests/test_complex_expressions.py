"""
Integration tests for complex expressions in the Math Interpreter.

This module contains comprehensive tests for complex expressions that combine
multiple operations, testing operator precedence, parentheses handling, and
nested operations as specified in requirements 5.1, 5.2, 5.3, and 5.4.
"""

import unittest
from math_interpreter.terminal_expressions import Constant, Variable
from math_interpreter.non_terminal_expressions import Addition, Multiplication
from math_interpreter.context import Context
from math_interpreter.exceptions import VariableNotDefinedError


class TestComplexExpressions(unittest.TestCase):
    """Test cases for complex expressions combining multiple operations."""
    
    def setUp(self):
        """Set up a context with common variables for testing."""
        self.context = Context()
        self.context.set_variable("x", 5)
        self.context.set_variable("y", 3)
        self.context.set_variable("z", 2)
    
    def test_operator_precedence(self):
        """
        Test operator precedence (multiplication before addition).
        
        This tests requirement 5.1: WHEN an expression contains both addition and 
        multiplication THEN the system SHALL follow standard mathematical precedence 
        (multiplication before addition).
        
        Examples:
        - x + y * z = 5 + (3 * 2) = 5 + 6 = 11
        - x * y + z = (5 * 3) + 2 = 15 + 2 = 17
        """
        # x + y * z = 5 + (3 * 2) = 5 + 6 = 11
        expr1 = Addition(
            Variable("x"),
            Multiplication(Variable("y"), Variable("z"))
        )
        self.assertEqual(expr1.interpret(self.context), 11.0)
        self.assertEqual(str(expr1), "(x + (y * z))")
        
        # x * y + z = (5 * 3) + 2 = 15 + 2 = 17
        expr2 = Addition(
            Multiplication(Variable("x"), Variable("y")),
            Variable("z")
        )
        self.assertEqual(expr2.interpret(self.context), 17.0)
        self.assertEqual(str(expr2), "((x * y) + z)")
        
        # 2 + 3 * 4 + 5 = 2 + 12 + 5 = 19
        expr3 = Addition(
            Addition(
                Constant(2),
                Multiplication(Constant(3), Constant(4))
            ),
            Constant(5)
        )
        self.assertEqual(expr3.interpret(self.context), 19.0)
        self.assertEqual(str(expr3), "((2 + (3 * 4)) + 5)")
    
    def test_parenthesized_expressions(self):
        """
        Test expressions with parentheses.
        
        This tests requirement 5.2: WHEN parentheses are used THEN the system SHALL 
        evaluate grouped expressions first.
        
        Examples:
        - (x + y) * z = (5 + 3) * 2 = 8 * 2 = 16
        - x * (y + z) = 5 * (3 + 2) = 5 * 5 = 25
        """
        # (x + y) * z = (5 + 3) * 2 = 8 * 2 = 16
        expr1 = Multiplication(
            Addition(Variable("x"), Variable("y")),
            Variable("z")
        )
        self.assertEqual(expr1.interpret(self.context), 16.0)
        self.assertEqual(str(expr1), "((x + y) * z)")
        
        # x * (y + z) = 5 * (3 + 2) = 5 * 5 = 25
        expr2 = Multiplication(
            Variable("x"),
            Addition(Variable("y"), Variable("z"))
        )
        self.assertEqual(expr2.interpret(self.context), 25.0)
        self.assertEqual(str(expr2), "(x * (y + z))")
        
        # (2 + 3) * (4 + 5) = 5 * 9 = 45
        expr3 = Multiplication(
            Addition(Constant(2), Constant(3)),
            Addition(Constant(4), Constant(5))
        )
        self.assertEqual(expr3.interpret(self.context), 45.0)
        self.assertEqual(str(expr3), "((2 + 3) * (4 + 5))")
    
    def test_nested_operations(self):
        """
        Test nested operations.
        
        This tests requirement 5.3: WHEN nested operations occur THEN the system SHALL 
        evaluate from innermost to outermost.
        
        Examples:
        - ((x + y) * z) + x = ((5 + 3) * 2) + 5 = (8 * 2) + 5 = 16 + 5 = 21
        - x * ((y + z) * y) = 5 * ((3 + 2) * 3) = 5 * (5 * 3) = 5 * 15 = 75
        """
        # ((x + y) * z) + x = ((5 + 3) * 2) + 5 = (8 * 2) + 5 = 16 + 5 = 21
        expr1 = Addition(
            Multiplication(
                Addition(Variable("x"), Variable("y")),
                Variable("z")
            ),
            Variable("x")
        )
        self.assertEqual(expr1.interpret(self.context), 21.0)
        self.assertEqual(str(expr1), "(((x + y) * z) + x)")
        
        # x * ((y + z) * y) = 5 * ((3 + 2) * 3) = 5 * (5 * 3) = 5 * 15 = 75
        expr2 = Multiplication(
            Variable("x"),
            Multiplication(
                Addition(Variable("y"), Variable("z")),
                Variable("y")
            )
        )
        self.assertEqual(expr2.interpret(self.context), 75.0)
        self.assertEqual(str(expr2), "(x * ((y + z) * y))")
        
        # (2 * (3 + 4)) * (5 + (6 * 7)) = (2 * 7) * (5 + 42) = 14 * 47 = 658
        expr3 = Multiplication(
            Multiplication(
                Constant(2),
                Addition(Constant(3), Constant(4))
            ),
            Addition(
                Constant(5),
                Multiplication(Constant(6), Constant(7))
            )
        )
        self.assertEqual(expr3.interpret(self.context), 658.0)
        self.assertEqual(str(expr3), "((2 * (3 + 4)) * (5 + (6 * 7)))")
    
    def test_complex_mathematical_expressions(self):
        """
        Test complex mathematical expressions.
        
        This tests requirement 5.4: WHEN complex expressions are evaluated THEN the system 
        SHALL return mathematically correct results.
        
        Examples:
        - x * y + z * x = (5 * 3) + (2 * 5) = 15 + 10 = 25
        - (x + y) * (z + x) = (5 + 3) * (2 + 5) = 8 * 7 = 56
        - x * (y + z * (x + y)) = 5 * (3 + 2 * (5 + 3)) = 5 * (3 + 2 * 8) = 5 * (3 + 16) = 5 * 19 = 95
        """
        # x * y + z * x = (5 * 3) + (2 * 5) = 15 + 10 = 25
        expr1 = Addition(
            Multiplication(Variable("x"), Variable("y")),
            Multiplication(Variable("z"), Variable("x"))
        )
        self.assertEqual(expr1.interpret(self.context), 25.0)
        self.assertEqual(str(expr1), "((x * y) + (z * x))")
        
        # (x + y) * (z + x) = (5 + 3) * (2 + 5) = 8 * 7 = 56
        expr2 = Multiplication(
            Addition(Variable("x"), Variable("y")),
            Addition(Variable("z"), Variable("x"))
        )
        self.assertEqual(expr2.interpret(self.context), 56.0)
        self.assertEqual(str(expr2), "((x + y) * (z + x))")
        
        # x * (y + z * (x + y)) = 5 * (3 + 2 * (5 + 3)) = 5 * (3 + 2 * 8) = 5 * (3 + 16) = 5 * 19 = 95
        expr3 = Multiplication(
            Variable("x"),
            Addition(
                Variable("y"),
                Multiplication(
                    Variable("z"),
                    Addition(Variable("x"), Variable("y"))
                )
            )
        )
        self.assertEqual(expr3.interpret(self.context), 95.0)
        self.assertEqual(str(expr3), "(x * (y + (z * (x + y))))")
    
    def test_variable_updates_in_complex_expressions(self):
        """
        Test complex expressions with variable updates.
        
        This verifies that when variables are updated, the expressions are evaluated
        with the new values.
        """
        # (x + y) * z = (5 + 3) * 2 = 8 * 2 = 16
        expr = Multiplication(
            Addition(Variable("x"), Variable("y")),
            Variable("z")
        )
        self.assertEqual(expr.interpret(self.context), 16.0)
        
        # Update variables and re-evaluate
        self.context.set_variable("x", 10)
        self.context.set_variable("z", 4)
        
        # (x + y) * z = (10 + 3) * 4 = 13 * 4 = 52
        self.assertEqual(expr.interpret(self.context), 52.0)
    
    def test_error_handling_in_complex_expressions(self):
        """
        Test error handling in complex expressions.
        
        This verifies that errors are properly propagated from nested expressions.
        """
        # x * (y + w) where w is undefined
        expr = Multiplication(
            Variable("x"),
            Addition(Variable("y"), Variable("w"))  # w is undefined
        )
        
        with self.assertRaises(VariableNotDefinedError) as context:
            expr.interpret(self.context)
        
        self.assertIn("Variable 'w' is not defined", str(context.exception))
    
    def test_mixed_numeric_types(self):
        """
        Test complex expressions with mixed numeric types (integers and floats).
        
        This verifies that expressions with mixed numeric types are evaluated correctly.
        """
        # Set up variables with different numeric types
        self.context.set_variable("a", 2.5)  # float
        self.context.set_variable("b", 3)    # int
        
        # a * (b + x) = 2.5 * (3 + 5) = 2.5 * 8 = 20.0
        expr = Multiplication(
            Variable("a"),
            Addition(Variable("b"), Variable("x"))
        )
        
        self.assertEqual(expr.interpret(self.context), 20.0)
        self.assertEqual(str(expr), "(a * (b + x))")


if __name__ == "__main__":
    unittest.main()