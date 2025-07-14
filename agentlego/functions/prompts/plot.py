PLOT_PROMPT = """You are a smart information processor and programmer. I will provide you with some information that was extracted from a picture using tools. Your task is to generate Python code using the matplotlib library to draw a meaningful diagram based on the information provided.

Your response should consist of two parts:

1. **Thought:** Explain your reasoning for selecting the information that is worth visualizing. This typically involves mathematical expressions, coordinates, or data that can be better understood through graphical representation.
2. **Code:** Provide the Python code to draw the diagram. The code should include a function named `solution` that returns the matplotlib figure directly. Avoid printing the result.

Here are some examples to help guide you:

Example 1:
```
{example1}
```

Example 2:
```
{example2}
```

Now that you understand the method and format, I will provide you with the information to process. Please generate your Python code in the same format.

Information:  
{context}
"""


# Information: 
# MathOCR: The mathematical expression in the image is $f(x)=x^{{2}}+2 x-8$.

# Thought: This expression is a quadratic function, which can be visualized by plotting its curve. A graph will make the behavior of the function clearer.
# Code: 
# import matplotlib.pyplot as plt
# import numpy as np
# def solution():
#     x = np.linspace(-10, 10, 400)    
#     y = x**2 + 2*x - 8
#     figure = plt.figure(figsize=(8, 6))    
#     plt.plot(x, y, color='blue', label=r'$f(x) = x^{{2}}+2x-8$')    
#     plt.title(r'Graph of $f(x) = x^{{2}}+2x-8$')
#     plt.xlabel(r'x')    
#     plt.ylabel(r'f(x)')   
#     plt.legend()    
#     return figure

# Information: 
# OCR: The texts and their coordinates in the image are as follows:
# (26, 4, 548, 60) x=[5,7,8,7,2, 17,2,9,
# (120, 96, 424, 148) 4,11, 12,9, 6]
# (23, 183, 683, 333) y = [99, 86,87, 88, 100, 86, 103, 87 , 94, 78, 77 , 85, 86]

# Thought: These two lists of numbers represent a set of data points. Plotting a scatter plot will help visualize the relationship between the x and y values.
# Code:
# import matplotlib.pyplot as plt
# def solution():    
#     x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]    
#     y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86]    
#     figure = plt.figure(figsize=(8, 6))    
#     plt.plot(x, y, 'bo')    
#     plt.xlabel('X-axis')    
#     plt.ylabel('Y-axis')    
#     plt.title('Scatter Plot')
#     return figure

# PROMPT = """You are a smart information processor and programmer. Now I will provide you with some information that was extracted from a picture using tools. Please generate a python code that uses matplotlib library to draw a meaningful diagram based on the information. Your response should contain two parts:
# ```
# Thought: The thinking process of what information in the text is worth drawing a diagram. They are usually mathematical expressions or complex numbers. This information will be clearer when presented in the form of a diagram.
# Code: The python code you use to draw the diagram. The code should include a function named 'solution'. The function should return the matplotlib figure directly. Avoid printing the answer.
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
# MathOCR: The mathematical expression in the image is $f(x)=x^{{2}}+2 x-8$.

# Thought: We can directly draw a figure of the expression $f(x)=x^{{2}}+2 x-8$ to visualize the curve.
# Code: 
# import matplotlib.pyplot as plt
# import numpy as np
# def solution():
#     x = np.linspace(-10, 10, 400)    
#     y = x**2 + 2*x - 8
#     figure = plt.figure(figsize=(8, 6))    
#     plt.plot(x, y, color='blue', label=r'$f(x) = x^{{2}}+2x-8$')    
#     plt.title(r'Graph of $f(x) = x^{{2}}+2x-8$')
#     plt.xlabel(r'x')    
#     plt.ylabel(r'f(x)')   
#     plt.legend()    
#     return figure"""

# EXAMPLES2 = """Information: 
# OCR: The texts and their coordinates in the image are as follows:
# (26, 4, 548, 60) x=[5,7,8,7,2, 17,2,9,
# (120, 96, 424, 148) 4,11, 12,9, 6]
# (23, 183, 683, 333) y = [99, 86,87, 88, 100, 86, 103, 87 , 94, 78, 77 , 85, 86]

# Thought: We can draw a scatter plot of the two lists of numbers to visualize the relationship between them.
# Code:
# import matplotlib.pyplot as plt
# def solution():    
#     x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]    
#     y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86]    
#     figure = plt.figure(figsize=(8, 6))    
#     plt.plot(x, y, 'bo')    
#     plt.xlabel('X-axis')    
#     plt.ylabel('Y-axis')    
#     plt.title('Scatter Plot')
#     return figure"""

# FINAL_PROMPT = """Now that you have learned the method and format of the reply through examples, I will provide you with the information to be handled, please make your answer.
# NOTE: You would better use the information provided in the LAST paragraph to make your answer, so that the information would become a complete process.

# Information: 
# {content}
# """