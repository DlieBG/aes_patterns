"""
Context class for managing variables in the Math Interpreter.
"""

from typing import Dict


class Context:
    """
    Context class for storing and retrieving variables during expression interpretation.
    """
    
    def __init__(self):
        """
        Initialize an empty context with no variables.
        """
        self._variables: Dict[str, float] = {}
    
    def set_variable(self, name: str, value: float) -> None:
        """
        Set a variable value in the context.
        
        Args:
            name: The variable name.
            value: The variable value.
        """
        self._variables[name] = value
    
    def get_variable(self, name: str) -> float:
        """
        Get a variable value from the context.
        
        Args:
            name: The variable name.
            
        Returns:
            float: The variable value.
            
        Raises:
            VariableNotDefinedError: If the variable is not defined.
        """
        from math_interpreter.exceptions import VariableNotDefinedError
        
        if name not in self._variables:
            raise VariableNotDefinedError(f"Variable '{name}' is not defined")
        
        return self._variables[name]
    
    def has_variable(self, name: str) -> bool:
        """
        Check if a variable exists in the context.
        
        Args:
            name: The variable name.
            
        Returns:
            bool: True if the variable exists, False otherwise.
        """
        return name in self._variables