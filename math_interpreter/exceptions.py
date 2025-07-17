"""
Custom exceptions for the Math Interpreter.
"""


class InterpreterError(Exception):
    """Base exception for interpreter errors."""
    pass


class VariableNotDefinedError(InterpreterError):
    """Raised when accessing an undefined variable."""
    pass


class InvalidExpressionError(InterpreterError):
    """Raised for malformed expressions."""
    pass