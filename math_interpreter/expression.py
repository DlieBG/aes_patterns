"""
Expression interface for the Math Interpreter.
"""

from abc import ABC, abstractmethod


class Expression(ABC):
    """
    Abstract base class for all expressions in the interpreter pattern.
    """
    
    @abstractmethod
    def interpret(self, context):
        """
        Interpret the expression and return numeric result.
        
        Args:
            context: The context containing variable definitions.
            
        Returns:
            float: The result of interpreting the expression.
        """
        pass
    
    @abstractmethod
    def __str__(self):
        """
        String representation of the expression.
        
        Returns:
            str: A string representation of the expression.
        """
        pass