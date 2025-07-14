REGIONATTRIBUTEDESCRIPTION_PROMPT = """You are a smart information processor. I will provide you with some information extracted from a picture using tools. Your task is to extract a bounding box for a relevant object in the image and select an attribute of the object within the box.

Your response should consist of three parts:

1. **Thought:** Explain your reasoning behind selecting the bounding box and the attribute you choose to extract.
2. **Bounding Box:** Provide the coordinates of the bounding box in the format (x1, y1, x2, y2).
3. **Attribute:** Specify the attribute you are selecting, such as color, size, breed, or what is held in the hand.

Here are some examples to guide you:

Example 1:
```
{example1}
```

Example 2:
```
{example2}
```

Now that you understand the format, I will provide you with the information. Please provide your answer in the same structure.

Information:  
{context}
"""


# Information:
# ImageDescription: The image shows five dogs of different breeds sitting side by side. The dogs exhibit a variety of colors and sizes, with the smallest on the left and the largest on the right. The background is plain white.
# TextToBbox: The 'dogs' in the image is at (762, 75, 936, 532), (595, 89, 763, 518), (423, 140, 608, 520), (82, 265, 253, 510), (272, 220, 424, 508).

# Thought: Now that we know there are 5 dogs of different breeds in the image, one detail worth observing is the breed of one specific dog. Based on the available information, let's focus on the dog in the middle, located at (423, 140, 608, 520), and determine its breed.
# Bounding Box: (423, 140, 608, 520)
# Attribute: breed

# Information:
# ImageDescription: The image is a drawing of four individuals seated on a patterned bus or train with green upholstered seats. The individuals are holding musical instruments, which include a double bass, a guitar, a violin, and a banjo. The scene appears to represent a group of musicians traveling together.
# TextToBbox: The 'man sitting in the front' in the image is at (353, 253, 1047, 924).

# Thought: The man sitting in the front of the bus at (353, 253, 1047, 924) is holding an object. I want to know what instrument he is holding.
# Bounding Box: (353, 253, 1047, 924)
# Attribute: what is held in the hand

# PROMPT = """You are a smart information processor. Now I will provide you with some information that was extracted from a picture using tools. Please extract a bounding box from the information and select an attribute of the object within the box. Your response should contain three parts:
# ```
# Thought: The thinking process of how you select the bounding box and attribute.
# Bounding Box: The coordinates of the bounding box in the format (x1, y1, x2, y2).
# Attribute: The attribute that you select.
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
# ImageDescription: The image shows five dogs of different breeds sitting side by side. The dogs exhibit a variety of colors and sizes, with the smallest on the left and the largest on the right. The background is plain white.
# TextToBbox: The 'dogs' in the image is at (762, 75, 936, 532), (595, 89, 763, 518), (423, 140, 608, 520), (82, 265, 253, 510), (272, 220, 424, 508).

# Thought: The dog in the middle is at (423, 140, 608, 520), I would like to know the breed of this dog.
# Bounding Box: (423, 140, 608, 520)
# Attribute: breed"""

# EXAMPLE2 = """Information:
# ImageDescription: The image is a drawing of four individuals seated on a patterned bus or train with green upholstered seats. The individuals are holding musical instruments, which include a double bass, a guitar, a violin, and a banjo. The scene appears to represent a group of musicians traveling together.
# TextToBbox: The 'man sitting in the front' in the image is at (353, 253, 1047, 924).

# Thought: The man in the front is at (353, 253, 1047, 924), and he is holding a musical instrument. I would like to know what is held in his hand.
# Bounding Box: (353, 253, 1047, 924)
# Attribute: what is held in the hand"""

# FINAL_PROMPT = """Now that you have learned the method and format of the reply through examples, I will provide you with the information to be handled, please make your answer.
# NOTE: You would better use the information provided in the LAST paragraph to make your answer, so that the information would become a complete process.

# Information: 
# {content}
# """

# REGIONATTRIBUTEDESCRIPTION_PROMPT = """You are a smart information processor. I will provide you with some information extracted from a picture using tools. Your task is to extract a bounding box for a relevant object in the image and select an attribute of the object within the box.

# Your response should consist of three parts:

# 1. **Thought:** Explain your reasoning behind selecting the bounding box and the attribute you choose to extract.
# 2. **Bounding Box:** Provide the coordinates of the bounding box in the format (x1, y1, x2, y2).
# 3. **Attribute:** Specify the attribute you are selecting, such as color, size, breed, or what is held in the hand.

# Here are some examples to guide you:

# Example 1:
# ```
# Information:
# ImageDescription: The image shows five dogs of different breeds sitting side by side. The dogs exhibit a variety of colors and sizes, with the smallest on the left and the largest on the right. The background is plain white.
# TextToBbox: The 'dogs' in the image is at (762, 75, 936, 532), (595, 89, 763, 518), (423, 140, 608, 520), (82, 265, 253, 510), (272, 220, 424, 508).

# Thought: I will select the middle dog located at (423, 140, 608, 520) because its size and position make it distinct. I would like to know the breed of this dog.
# Bounding Box: (423, 140, 608, 520)
# Attribute: breed
# ```

# Example 2:
# ```
# Information:
# ImageDescription: The image is a drawing of four individuals seated on a patterned bus or train with green upholstered seats. The individuals are holding musical instruments, which include a double bass, a guitar, a violin, and a banjo. The scene appears to represent a group of musicians traveling together.
# TextToBbox: The 'man sitting in the front' in the image is at (353, 253, 1047, 924).

# Thought: The man sitting in the front of the bus at (353, 253, 1047, 924) is holding an object. I want to know what instrument he is holding.
# Bounding Box: (353, 253, 1047, 924)
# Attribute: what is held in the hand
# ```

# Now that you understand the format, I will provide you with the information. Please provide your answer in the same structure.

# Information:  
# {content}
# """