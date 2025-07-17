"""
Terminal expressions for the Math Interpreter.
"""

from math_interpreter.expression import Expression
from math_interpreter.context import Context


class Constant(Expression):
    """
    A terminal expression representing a constant numeric value.
    """
    
    def __init__(self, value):
        """
        Initialize a constant with a numeric value.
        
        Args:
            value: The numeric value (int or float).
        """
        self.value = float(value)
    
    def interpret(self, context):
        """
        Interpret the constant expression.
        
        Args:
            context: The context (unused for constants).
            
        Returns:
            float: The constant value.
        """
        return self.value
    
    def __str__(self):
        """
        String representation of the constant.
        
        Returns:
            str: A string representation of the constant value.
        """
        # Check if the value is an integer equivalent
        if self.value == int(self.value):
            return str(int(self.value))
        return str(self.value)


class Variable(Expression):
    """
    A terminal expression representing a variable.
    """
    
    def __init__(self, name):
        """
        Initialize a variable with a name.
        
        Args:
            name: The variable name.
        """
        self.name = name
    
    def interpret(self, context):
        """
        Interpret the variable expression by looking up its value in the context.
        
        Args:
            context: The context containing variable definitions.
            
        Returns:
            float: The variable value.
            
        Raises:
            VariableNotDefinedError: If the variable is not defined in the context.
        """
        return context.get_variable(self.name)
    
    def __str__(self):
        """
        String representation of the variable.
        
        Returns:
            str: The variable name.
        """
        return self.name