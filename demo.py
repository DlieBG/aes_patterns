#!/usr/bin/env python3
"""
Math Interpreter Demo Script

This script demonstrates the usage of the Math Interpreter with various examples
showing constants, variables, and operations (addition and multiplication).
"""

from math_interpreter.context import Context
from math_interpreter.terminal_expressions import Constant, Variable
from math_interpreter.non_terminal_expressions import Addition, Multiplication
from math_interpreter.exceptions import VariableNotDefinedError


def print_section(title):
    """Print a section title with decorative formatting."""
    print("\n" + "=" * 60)
    print(f" {title} ".center(60, "-"))
    print("=" * 60)


def evaluate_and_print(expression, context, description=None):
    """Evaluate an expression and print the result with optional description."""
    if description:
        print(f"\n{description}:")
    
    print(f"Expression: {expression}")
    try:
        result = expression.interpret(context)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main demo function showcasing the Math Interpreter."""
    # Create a context for storing variables
    context = Context()
    
    print_section("MATH INTERPRETER DEMONSTRATION")
    print("This demo shows how to use the Math Interpreter to evaluate expressions")
    print("with constants, variables, and operations (addition and multiplication).")
    
    # SECTION 1: Constants
    print_section("1. CONSTANTS")
    
    # Integer constant
    int_const = Constant(5)
    evaluate_and_print(int_const, context, "Integer constant")
    
    # Floating-point constant
    float_const = Constant(3.14)
    evaluate_and_print(float_const, context, "Floating-point constant")
    
    # SECTION 2: Variables
    print_section("2. VARIABLES")
    
    # Set variables in the context
    context.set_variable("x", 10)
    context.set_variable("y", 5.5)
    print("Variables set in context:")
    print("  x = 10")
    print("  y = 5.5")
    
    # Access defined variable
    var_x = Variable("x")
    evaluate_and_print(var_x, context, "Accessing defined variable 'x'")
    
    # Access undefined variable
    var_z = Variable("z")
    evaluate_and_print(var_z, context, "Attempting to access undefined variable 'z'")
    
    # Update variable value
    print("\nUpdating variable 'x' from 10 to 20")
    context.set_variable("x", 20)
    evaluate_and_print(var_x, context, "Accessing updated variable 'x'")
    
    # SECTION 3: Addition
    print_section("3. ADDITION")
    
    # Addition of constants
    add_const = Addition(Constant(2), Constant(3))
    evaluate_and_print(add_const, context, "Addition of constants: 2 + 3")
    
    # Addition of variables
    add_vars = Addition(Variable("x"), Variable("y"))
    evaluate_and_print(add_vars, context, "Addition of variables: x + y")
    
    # Mixed addition (constants and variables)
    add_mixed = Addition(Constant(7), Variable("x"))
    evaluate_and_print(add_mixed, context, "Mixed addition: 7 + x")
    
    # Chained addition
    add_chain = Addition(Addition(Constant(1), Constant(2)), Constant(3))
    evaluate_and_print(add_chain, context, "Chained addition: (1 + 2) + 3")
    
    # SECTION 4: Multiplication
    print_section("4. MULTIPLICATION")
    
    # Multiplication of constants
    mul_const = Multiplication(Constant(4), Constant(5))
    evaluate_and_print(mul_const, context, "Multiplication of constants: 4 * 5")
    
    # Multiplication of variables
    mul_vars = Multiplication(Variable("x"), Variable("y"))
    evaluate_and_print(mul_vars, context, "Multiplication of variables: x * y")
    
    # Mixed multiplication (constants and variables)
    mul_mixed = Multiplication(Constant(3), Variable("x"))
    evaluate_and_print(mul_mixed, context, "Mixed multiplication: 3 * x")
    
    # Chained multiplication
    mul_chain = Multiplication(Multiplication(Constant(2), Constant(3)), Constant(4))
    evaluate_and_print(mul_chain, context, "Chained multiplication: (2 * 3) * 4")
    
    # SECTION 5: Complex Expressions
    print_section("5. COMPLEX EXPRESSIONS")
    
    # Addition and multiplication (operator precedence)
    # Expression: 2 + x * 3 (where x = 20)
    complex_expr1 = Addition(
        Constant(2),
        Multiplication(Variable("x"), Constant(3))
    )
    evaluate_and_print(complex_expr1, context, 
                      "Complex expression with precedence: 2 + x * 3 (where x = 20)")
    
    # Nested operations
    # Expression: (5 + y) * (x + 2) (where y = 5.5, x = 20)
    complex_expr2 = Multiplication(
        Addition(Constant(5), Variable("y")),
        Addition(Variable("x"), Constant(2))
    )
    evaluate_and_print(complex_expr2, context, 
                      "Nested operations: (5 + y) * (x + 2) (where y = 5.5, x = 20)")
    
    # Multiple operations
    # Expression: x * y + 2 * 3 (where x = 20, y = 5.5)
    complex_expr3 = Addition(
        Multiplication(Variable("x"), Variable("y")),
        Multiplication(Constant(2), Constant(3))
    )
    evaluate_and_print(complex_expr3, context, 
                      "Multiple operations: x * y + 2 * 3 (where x = 20, y = 5.5)")
    
    print("\nDemonstration complete!")


if __name__ == "__main__":
    main()