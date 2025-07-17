"""
Non-terminal expressions for the Math Interpreter.
"""

from math_interpreter.expression import Expression


class Addition(Expression):
    """
    A non-terminal expression representing addition operation.
    """
    
    def __init__(self, left, right):
        """
        Initialize an addition expression with left and right operands.
        
        Args:
            left: The left operand (Expression).
            right: The right operand (Expression).
        """
        self.left = left
        self.right = right
    
    def interpret(self, context):
        """
        Interpret the addition expression.
        
        Args:
            context: The context containing variable definitions.
            
        Returns:
            float: The sum of the left and right operands.
        """
        return self.left.interpret(context) + self.right.interpret(context)
    
    def __str__(self):
        """
        String representation of the addition expression.
        
        Returns:
            str: A string representation of the addition operation.
        """
        return f"({self.left} + {self.right})"


class Multiplication(Expression):
    """
    A non-terminal expression representing multiplication operation.
    """
    
    def __init__(self, left, right):
        """
        Initialize a multiplication expression with left and right operands.
        
        Args:
            left: The left operand (Expression).
            right: The right operand (Expression).
        """
        self.left = left
        self.right = right
    
    def interpret(self, context):
        """
        Interpret the multiplication expression.
        
        Args:
            context: The context containing variable definitions.
            
        Returns:
            float: The product of the left and right operands.
        """
        return self.left.interpret(context) * self.right.interpret(context)
    
    def __str__(self):
        """
        String representation of the multiplication expression.
        
        Returns:
            str: A string representation of the multiplication operation.
        """
        return f"({self.left} * {self.right})"