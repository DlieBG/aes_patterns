# Design Document

## Overview

The mathematical interpreter will implement the classic Interpreter Pattern to evaluate mathematical expressions containing constants, variables, and arithmetic operations (addition and multiplication). The system uses an Abstract Syntax Tree (AST) approach where each node represents either a terminal expression (constants, variables) or non-terminal expression (operations).

The design follows the Interpreter Pattern's core principle: define a grammar for the language and create an interpreter that uses the representation to interpret sentences in the language.

## Architecture

The system consists of four main components:

1. **Expression Interface**: Abstract base class defining the interpretation contract
2. **Terminal Expressions**: Concrete implementations for constants and variables
3. **Non-Terminal Expressions**: Concrete implementations for operations (addition, multiplication)
4. **Context**: Manages variable storage and retrieval
5. **Parser**: Converts string expressions into AST (future extension point)

### Class Hierarchy

```
Expression (ABC)
├── TerminalExpression (ABC)
│   ├── Constant
│   └── Variable
└── NonTerminalExpression (ABC)
    ├── Addition
    └── Multiplication
```

## Components and Interfaces

### Expression Interface

The `abc` module (Abstract Base Classes) is Python's built-in module for creating abstract classes. It ensures that subclasses implement required methods, providing compile-time checking for interface compliance.

```python
from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self, context: 'Context') -> float:
        """Interpret the expression and return numeric result"""
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """String representation of the expression"""
        pass
```

The `ABC` class provides the abstract base class functionality, while `@abstractmethod` decorator marks methods that must be implemented by concrete subclasses. Python will raise a `TypeError` if you try to instantiate a class that doesn't implement all abstract methods.

### Context Class

```python
class Context:
    def __init__(self):
        self._variables: Dict[str, float] = {}
    
    def set_variable(self, name: str, value: float) -> None:
        """Set variable value"""
        pass
    
    def get_variable(self, name: str) -> float:
        """Get variable value, raise error if undefined"""
        pass
    
    def has_variable(self, name: str) -> bool:
        """Check if variable exists"""
        pass
```

### Terminal Expressions

#### Constant Class
- Stores a numeric value
- Returns the value directly during interpretation
- Immutable once created

#### Variable Class
- Stores a variable name
- Looks up value in context during interpretation
- Raises VariableNotDefinedError if variable doesn't exist

### Non-Terminal Expressions

#### Addition Class
- Holds two Expression objects (left and right operands)
- Interprets both operands and returns their sum
- Supports operator precedence through tree structure

#### Multiplication Class
- Holds two Expression objects (left and right operands)
- Interprets both operands and returns their product
- Supports operator precedence through tree structure

## Data Models

### Expression Tree Structure

The interpreter builds expressions as binary trees where:
- Leaf nodes are terminal expressions (constants/variables)
- Internal nodes are operations (addition/multiplication)
- Tree structure naturally handles operator precedence

Example: `2 + x * 3` becomes:
```
    Addition
   /        \
Constant(2)  Multiplication
            /            \
      Variable(x)    Constant(3)
```

### Context Storage

Variables are stored in a dictionary mapping string names to float values:
```python
{
    "x": 5.0,
    "y": 10.5,
    "result": 42.0
}
```

## Error Handling

### Custom Exceptions

```python
class InterpreterError(Exception):
    """Base exception for interpreter errors"""
    pass

class VariableNotDefinedError(InterpreterError):
    """Raised when accessing undefined variable"""
    pass

class InvalidExpressionError(InterpreterError):
    """Raised for malformed expressions"""
    pass
```

### Error Scenarios

1. **Undefined Variable Access**: When Variable.interpret() cannot find variable in context
2. **Type Errors**: When non-numeric values are encountered
3. **Invalid Operations**: When operations receive invalid operands

## Testing Strategy

### Unit Testing Approach

1. **Terminal Expression Tests**
   - Constant: Test value storage and retrieval
   - Variable: Test context lookup, undefined variable errors

2. **Non-Terminal Expression Tests**
   - Addition: Test with constants, variables, and mixed operands
   - Multiplication: Test with constants, variables, and mixed operands

3. **Context Tests**
   - Variable storage and retrieval
   - Error handling for undefined variables
   - Variable updates and persistence

4. **Integration Tests**
   - Complex expressions with multiple operations
   - Operator precedence verification
   - Mixed constant and variable expressions

### Test Data Strategy

- Use both integer and floating-point numbers
- Test edge cases (zero, negative numbers)
- Test variable name variations (single char, multi-char)
- Test expression complexity (nested operations)

### Example Test Cases

```python
# Simple constant
expr = Constant(5)
assert expr.interpret(context) == 5

# Variable lookup
context.set_variable("x", 10)
expr = Variable("x")
assert expr.interpret(context) == 10

# Addition
expr = Addition(Constant(2), Constant(3))
assert expr.interpret(context) == 5

# Complex expression: 2 + x * 3 where x = 4
context.set_variable("x", 4)
expr = Addition(
    Constant(2),
    Multiplication(Variable("x"), Constant(3))
)
assert expr.interpret(context) == 14
```

## Extension Points

The design supports future extensions:

1. **New Operators**: Implement NonTerminalExpression for subtraction, division, power, etc.
2. **Functions**: Add function call expressions (sin, cos, sqrt)
3. **Parser**: Add string-to-AST parsing capability
4. **Type System**: Support different numeric types (int, complex)
5. **Optimization**: Add expression simplification and caching