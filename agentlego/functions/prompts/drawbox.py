DRAWBOX_PROMPT = """You are a smart information processor. I will provide you with information extracted from a picture using tools, and your task is to identify a bounding box for a relevant object or text in the image.

Your response should consist of two parts:

1. **Thought:** Explain your reasoning behind how you selected the bounding box.
2. **Bounding Box:** Provide the coordinates of the bounding box in the format (x1, y1, x2, y2).

Here are some examples to help you understand:

Example 1:
```
{example1}
```

Example 2:
```
{example2}
```

Now that you understand the format, I will provide you with the information to process. Please give your answer in the same format.

Information:  
{context}
"""


# Information:
# OCR: The texts and their coordinates in the image are as follows:
# (531, 5, 944, 91) Italv Greece Turkey Syria AMalta Mediterranean Sea Cypruzebanod Iraq Israg
# (34, 38, 194, 66) Atlantic Ocean
# (469, 33, 483, 91) 1
# (1044, 38, 1098, 66) Iran

# Thought: The bounding box (34, 38, 194, 66) corresponds to the text "Atlantic Ocean," and I can use this box to identify the location of the ocean label in the image.
# Bounding Box: (34, 38, 194, 66)

# Information:
# ImageDescription: The image is a drawing of four individuals seated on a patterned bus or train with green upholstered seats. The individuals are holding musical instruments, which include a double bass, a guitar, a violin, and a banjo. The scene appears to represent a group of musicians traveling together.
# TextToBbox: The 'man sitting in the front' in the image is at (353, 253, 1047, 924).

# Thought: The bounding box (353, 253, 1047, 924) corresponds to the man sitting in the front of the bus, clearly identifying the individual in the image.
# Bounding Box: (353, 253, 1047, 924)


# PROMPT = """You are a smart information processor. Now I will provide you with some information that was extracted from a picture using tools. Please extract a bounding box from the information. Your response should contain two parts:
# ```
# Thought: The thinking process of how you select the bounding box.
# Bounding Box: The coordinates of the bounding box in the format (x1, y1, x2, y2). 
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

# EXAMPLE1 = """Information:
# OCR: The texts and their coordinates in the image are as follows:
# (531, 5, 944, 91) Italv Greece Turkey Syria AMalta Mediterranean Sea Cypruzebanod Iraq Israg
# (34, 38, 194, 66) Atlantic Ocean
# (469, 33, 483, 91) 1
# (1044, 38, 1098, 66) Iran

# Thought: The bounding box (34, 38, 194, 66) corresponds to the text "Atlantic Ocean" in the OCR text. I can extract the bounding box to identify the location of the Atlantic Ocean.
# Bounding Box: (34, 38, 194, 66)"""

# EXAMPLE2 = """Information:
# ImageDescription: The image is a drawing of four individuals seated on a patterned bus or train with green upholstered seats. The individuals are holding musical instruments, which include a double bass, a guitar, a violin, and a banjo. The scene appears to represent a group of musicians traveling together.
# TextToBbox: The 'man sitting in the front' in the image is at (353, 253, 1047, 924).

# Thought: The bounding box (353, 253, 1047, 924) corresponds to the man sitting in the front in the image. I can extract the bounding box to identify the individual in the image.
# Bounding Box: (353, 253, 1047, 924)"""

# FINAL_PROMPT = """Now that you have learned the method and format of the reply through examples, I will provide you with the information to be handled, please make your answer.
# NOTE: You would better use the information provided in the LAST paragraph to make your answer, so that the information would become a complete process.

# Information: 
# {content}
# """