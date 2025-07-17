"""
Expression interface for the Math Interpreter.

This module defines the abstract base class for all expressions in the interpreter pattern.
Following the Interpreter Pattern design, all concrete expressions will inherit from this class.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .context import Context


class Expression(ABC):
    """
    Abstract base class for all expressions in the interpreter pattern.
    
    This class defines the interface that all expression types must implement.
    It follows requirement 6.1 (classic Interpreter Pattern structure) and
    supports requirement 6.2 (extensibility for new operators).
    """
    
    @abstractmethod
    def interpret(self, context: 'Context') -> float:
        """
        Interpret the expression and return numeric result.
        
        Args:
            context: The context containing variable definitions.
            
        Returns:
            float: The result of interpreting the expression.
            
        Raises:
            Various exceptions may be raised by concrete implementations.
        """
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """
        String representation of the expression.
        
        This method allows expressions to be printed in a human-readable format,
        which is useful for debugging and visualization of the abstract syntax tree.
        
        Returns:
            str: A string representation of the expression.
        """
        pass