THOUGHT_PROMPT = """You are a smart information processor. I will provide you with a problem, an answer, and a process for solving the problem using different tools. Your task is to describe the thinking behind solving the problem, specifically explaining the purpose of using each tool.

Your response should include several lines, one for each tool, and each line should contain two parts:

1. **Tool Name:** The name of the tool used.
2. **Thought:** Explain the purpose of using the tool, including the information you expect to get from it to solve the problem.

Here are some examples to guide you:

Example 1:
```
{example1}
```

Example 2:
```
{example2}
```

Now that you understand the format, I will provide you with the information. Please generate your response accordingly.

Question: {question}

Solving Process:
{context}

Answer: {answer}
"""


# Question: {question}

# Solving Process: 
# {content} 

# Answer: {answer} 

# Thinking Process:

# PROMPT = """You are a smart information processor. I will provide you with a problem, an answer, and a process for solving the problem using different tools. Your task is to describe the thinking behind solving the problem, specifically explaining the purpose of using each tool.

# Your response should include several lines, one for each tool, and each line should contain two parts:

# 1. **Tool Name:** The name of the tool used.
# 2. **Thought:** The purpose of using this tool, including the information you expect to get from it to solve the problem.

# Here are some examples to guide you:

# Example 1:
# ```
# {example1}
# ```

# Example 2:
# ```
# {example2}
# ```

# """

# EXAMPLE1 = """Question: The men in the picture want to buy one NVIDIA GeForce RTX 4070 SUPER each. According to NVIDIA's official website in January, how many dollars will they need to spend in total?

# Solving Process:
# CountGivenObject: 
# Input: {{'image': image/input.png, 'text': men}}
# Output: The number of 'men' in the image is 3.
# GoogleSearch: 
# Input: {{'query': NVIDIA GeForce RTX 4070 SUPER price January 2023}}
# Output: The search results for 'NVIDIA GeForce RTX 4070 SUPER price January 2023' are as follows:
# 1 - Answer box: The RTX 4070 SUPER arrives with 20% more cores than the RTX 4070, making it faster than an RTX 3090 at a fraction of the power. With DLSS 3, its lead stretches to 1.5x faster. It will be available starting Jan. 17 at $599.\\n\\n2 - GeForce RTX 40 SUPER Series Graphics Cards Launching This ...: The GeForce RTX 4070 SUPER launches January 17th, starting at $599. It boasts 20% more CUDA Cores than the GeForce RTX 4070, and is great for ...\\n\\n3 - Graphics Card Prices Drop Following Nvidia's RTX 4070 ... - Forbes: In fact, ASRock has some super-keen pricing already online with the Phanton Gaming RX 7900 XT sitting at just $709.99 reduced from $799 while ...\\n\\n4 - Review: Nvidia's $600 GeForce RTX 4070 Super is one of its best ...: Judging by the comments on YouTube reviews, you'd think Nvidia's RTX 4070, launched in April 2023 for $599, was a terrible graphics card.\\n\\n5 - NVIDIA GeForce RTX 4070 SUPER marks its first price drop to $589: ZOTAC RTX 4070 SUPER: $589.99 Newegg. ZOTAC has taken the lead in making a price adjustment for their model, becoming the first brand to do so.\\n\\n
# Calculator:
# Input: {{'expression': 599 * 3}}
# Output: The result of 599 * 3 is 1797.

# Answer: 1797

# Thinking Process:
# CountGivenObject: Before proceeding to calculate the total cost, I need to know how many men are in the picture. I will use the 'CountGivenObject' tool to count the number of men in the image. After knowing the count, I will use the 'GoogleSearch' tool to find the price of one NVIDIA GeForce RTX 4070 SUPER according to NVIDIA's official website in January.
# GoogleSearch: Now that I know there are 3 men in the picture, the next step is to find the price of one NVIDIA GeForce RTX 4070 SUPER according to NVIDIA's official website in January. For this, I will use the 'GoogleSearch' tool.
# Calculator: To calculate the total cost, multiply the number of men (3) by the cost of one NVIDIA GeForce RTX 4070 SUPER ($599)."""

# EXAMPLE2 = """Question: Please plot the graph of this function.

# Solving Process:
# MathOCR: 
# Input: {{'image': image/input.png}}
# Output: The mathematical expression in the image is $(x+4)^{{3}}=27$.
# Plot:
# Input: {{'command': \nimport matplotlib.pyplot as plt\nimport numpy as np\ndef solution():\n    x = np.linspace(-10, 2, 400)\n    y = (x + 4)**3\n    figure = plt.figure()\n    plt.plot(x, y, label='(x+4)^3')\n    plt.title('Graph of the function (x+4)^3')\n    plt.xlabel('x')\n    plt.ylabel('y')\n    plt.legend()\n    plt.grid(True)\n    return figure\n}}
# Output: The plot result is saved in path 'image/dummy_generated_image.jpg'

# Answer: image/dummy_generated_image.jpg

# Thinking Process:
# MathOCR: To plot the graph of the function described in the image, I need to use the MathOCR tool to recognize the math expression from the image provided.
# Plot: The MathOCR tool has provided the LaTeX styled expression for the function from the image, which is \\((x+4)^{{3}}=27\\). To plot the graph of this function, I need to first isolate \\(x\\) and then create a range of \\(x\\) values to plot the corresponding \\(y\\) values.\n\nFirst, I'll solve the equation for \\(x\\):\n\n\\((x+4)^{{3}}=27\\)\n\nTake the cube root of both sides:\n\n\\(x+4 = \\sqrt[3]{{27}}\\)\n\n\\(x+4 = 3\\)\n\n\\(x = 3 - 4\\)\n\n\\(x = -1\\)\n\nNow that we have the \\(x\\) value for which the function equals 27, we can plot the graph of the function \\((x+4)^{{3}}\\) around this point."""

# FINAL_PROMPT = """Now that you have learned the method and format of the reply through examples, I will provide you with the information to be handled, please make your answer.

# Question: {question}

# Solving Process:
# {content}

# Answer: {answer}

# Thinking Process:
# """

# THOUGHT_PROMPT = """You are a smart information processor. I will provide you with a problem, an answer, and a process for solving the problem using different tools. Your task is to describe the thinking behind solving the problem, specifically explaining the purpose of using each tool.

# Your response should include several lines, one for each tool, and each line should contain two parts:

# 1. **Tool Name:** The name of the tool used.
# 2. **Thought:** Explain the purpose of using the tool, including the information you expect to get from it to solve the problem.

# Here are some examples to guide you:

# Example 1:
# ```
# Question: The men in the picture want to buy one NVIDIA GeForce RTX 4070 SUPER each. According to NVIDIA's official website in January, how many dollars will they need to spend in total?

# Solving Process:
# CountGivenObject: 
# Input: {{'image': image/input.png, 'text': men}}
# Output: The number of 'men' in the image is 3.
# GoogleSearch: 
# Input: {{'query': NVIDIA GeForce RTX 4070 SUPER price January 2023}}
# Output: The search results for 'NVIDIA GeForce RTX 4070 SUPER price January 2023' are as follows:
# 1 - Answer box: The RTX 4070 SUPER arrives with 20% more cores than the RTX 4070, making it faster than an RTX 3090 at a fraction of the power. With DLSS 3, its lead stretches to 1.5x faster. It will be available starting Jan. 17 at $599.\\n\\n2 - GeForce RTX 40 SUPER Series Graphics Cards Launching This ...: The GeForce RTX 4070 SUPER launches January 17th, starting at $599. It boasts 20% more CUDA Cores than the GeForce RTX 4070, and is great for ...\\n\\n3 - Graphics Card Prices Drop Following Nvidia's RTX 4070 ... - Forbes: In fact, ASRock has some super-keen pricing already online with the Phanton Gaming RX 7900 XT sitting at just $709.99 reduced from $799 while ...\\n\\n4 - Review: Nvidia's $600 GeForce RTX 4070 Super is one of its best ...: Judging by the comments on YouTube reviews, you'd think Nvidia's RTX 4070, launched in April 2023 for $599, was a terrible graphics card.\\n\\n5 - NVIDIA GeForce RTX 4070 SUPER marks its first price drop to $589: ZOTAC RTX 4070 SUPER: $589.99 Newegg. ZOTAC has taken the lead in making a price adjustment for their model, becoming the first brand to do so.\\n\\n
# Calculator:
# Input: {{'expression': 599 * 3}}
# Output: The result of 599 * 3 is 1797.

# Answer: 1797

# Thinking Process:
# CountGivenObject: Before proceeding to calculate the total cost, I need to know how many men are in the picture. I will use the 'CountGivenObject' tool to count the number of men in the image. After knowing the count, I will use the 'GoogleSearch' tool to find the price of one NVIDIA GeForce RTX 4070 SUPER according to NVIDIA's official website in January.
# GoogleSearch: Now that I know there are 3 men in the picture, the next step is to find the price of one NVIDIA GeForce RTX 4070 SUPER according to NVIDIA's official website in January. For this, I will use the 'GoogleSearch' tool.
# Calculator: To calculate the total cost, multiply the number of men (3) by the cost of one NVIDIA GeForce RTX 4070 SUPER ($599).
# ```

# Example 2:
# ```
# Question: Please plot the graph of this function.

# Solving Process:
# MathOCR: 
# Input: {{'image': image/input.png}}
# Output: The mathematical expression in the image is $(x+4)^{{3}}=27$.
# Plot:
# Input: {{'command': \nimport matplotlib.pyplot as plt\nimport numpy as np\ndef solution():\n    x = np.linspace(-10, 2, 400)\n    y = (x + 4)**3\n    figure = plt.figure()\n    plt.plot(x, y, label='(x+4)^3')\n    plt.title('Graph of the function (x+4)^3')\n    plt.xlabel('x')\n    plt.ylabel('y')\n    plt.legend()\n    plt.grid(True)\n    return figure\n}}
# Output: The plot result is saved in path 'image/dummy_generated_image.jpg'

# Answer: image/dummy_generated_image.jpg

# Thinking Process:
# MathOCR: To plot the graph of the function described in the image, I need to use the MathOCR tool to recognize the math expression from the image provided.
# Plot: The MathOCR tool has provided the LaTeX styled expression for the function from the image, which is \\((x+4)^{{3}}=27\\). To plot the graph of this function, I need to first isolate \\(x\\) and then create a range of \\(x\\) values to plot the corresponding \\(y\\) values.\n\nFirst, I'll solve the equation for \\(x\\):\n\n\\((x+4)^{{3}}=27\\)\n\nTake the cube root of both sides:\n\n\\(x+4 = \\sqrt[3]{{27}}\\)\n\n\\(x+4 = 3\\)\n\n\\(x = 3 - 4\\)\n\n\\(x = -1\\)\n\nNow that we have the \\(x\\) value for which the function equals 27, we can plot the graph of the function \\((x+4)^{{3}}\\) around this point.
# ```

# Now that you understand the format, I will provide you with the information. Please generate your response accordingly.

# Question: {question}

# Solving Process: 
# {content} 

# Answer: {answer} 

# Thinking Process:
# """