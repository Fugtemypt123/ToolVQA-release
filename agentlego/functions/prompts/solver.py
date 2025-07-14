SOLVER_PROMPT = """You are a smart information processor and programmer. I will provide you with some information extracted from a picture using tools. Your task is to generate Python code using the **sympy** library to solve an equation based on the provided information.

Your response should consist of two parts:

1. **Thought:** Explain your reasoning for choosing the equation to solve and the method for solving it.
2. **Code:** Provide the Python code to solve the equation using the **sympy** library. The code should include a function named `solution`, and the function should return the solution as a string. Avoid printing the result.

Here are some examples to help guide you:

Example 1:
```
{example1}
```

Example 2:
```
{example2}
```

Now that you understand the method and format, I will provide you with the information. Please generate your Python code accordingly.

Information:  
{context}
"""


# Information: 
# MathOCR: The mathematical expression in the image is $\\frac{{3}}{{4}}\\left[\\frac{{4}}{{3}}\\left(\\frac{{1}}{{4}} x-1\\right)+4\\right]=\\frac{{1}}{{3}}+\\frac{{2 x}}{{3}}$.

# Thought: This equation can be solved algebraically to find the value of $x$. I will use **sympy** to solve it.
# Code: 
# from sympy import symbols, Eq, solve
# def solution():
#     x = symbols('x')
#     equation = Eq(3/4*(4/3*(1/4*x-1)+4), 1/3+2*x/3)    
#     solutions = solve(equation, x)    
#     return str(solutions)

# Information: 
# MathOCR: The mathematical expression in the image is $(x+4)^{{3}}=27$.

# Thought: This equation is simple enough to solve directly using sympy. I will solve it to find the value of $x$.
# Code:
# from sympy import symbols, Eq, solve
# def solution():    
#     x = symbols('x')    
#     equation = Eq((x + 4) ** 3, 27)    
#     solutions = solve(equation, x)
#     return str(solutions)


# PROMPT = """You are a smart information processor and programmer. Now I will provide you with some information that was extracted from a picture using tools. Please generate a python code that uses sympy library to solve an equation from the information. Your response should contain two parts:
# ```
# Thought: The thinking process of which equation to solve and how to solve it.
# Code: The python code you use to solve the equation. The code should include a function named 'solution'. You should use the `sympy` library in your code to solve the equations. The function should return its answer in str format. Avoid printing the answer.
# ```
# Below I will provide you with some examples to help you answer:

# Example 1:
# ```
# {example1}
# ```

# Example 2:
# ```
# {example2}
# ```

# """

# EXAMPLES1 = """Information: 
# MathOCR: The mathematical expression in the image is $\\\\frac{{3}}{{4}}\\\\left[\\\\frac{{4}}{{3}}\\\\left(\\\\frac{{1}}{{4}} x-1\\\\right)+4\\\\right]=\\\\frac{{1}}{{3}}+\\\\frac{{2 x}}{{3}}$.

# Thought: We can directly solve the equation $\\\\frac{{3}}{{4}}\\\\left[\\\\frac{{4}}{{3}}\\\\left(\\\\frac{{1}}{{4}} x-1\\\\right)+4\\\\right]=\\\\frac{{1}}{{3}}+\\\\frac{{2 x}}{{3}}$ to find the value of $x$.
# Code: 
# from sympy import symbols, Eq, solve
# def solution():
#     x = symbols('x')
#     equation = Eq(3/4*(4/3*(1/4*x-1)+4), 1/3+2*x/3)    
#     solutions = solve(equation, x)    
#     return str(solutions)"""

# EXAMPLES2 = """Information: 
# MathOCR: The mathematical expression in the image is $(x+4)^{{3}}=27$.

# Thought: We can directly solve the equation $(x+4)^{{3}}=27$ to find the value of $x$.
# Code:
# # import packages
# from sympy import symbols, Eq, solve
# def solution():    
#     # Define symbols    
#     x = symbols('x')    
    
#     # Define equation    
#     equation = Eq((x + 4) ** 3 - 27, 0)
    
#     # Solve the equation
#     solutions = solve(equation, x)
    
#     # Return solutions as strings
#     return str(solutions)"""

# FINAL_PROMPT = """Now that you have learned the method and format of the reply through examples, I will provide you with the information to be handled, please make your answer.
# NOTE: You would better use the information provided in the LAST paragraph to make your answer, so that the information would become a complete process.

# Information: 
# {content}
# """