TEXTTOBBOX_PROMPT = """You are a smart information processor. I will provide you with some information extracted from a picture using tools. Your task is to identify and extract an object to be located from the information.

Your response should consist of two parts:

1. **Thought:** Explain your reasoning behind how you selected the object.
2. **Object:** Specify the object you extracted, possibly with additional details.

Here are some examples to help guide you:

Example 1:
```
{example1}
```

Example 2:
```
{example2}
```

Now that you understand the format, I will provide you with the information. Please extract the object following the same structure.

Information:  
{context}
"""


# Information:  
# ImageDescription: The image shows five dogs of different breeds and sizes sitting in a row against a white background. From left to right, the first dog appears to be a Beagle, the third dog a Golden Retriever, and the fifth dog is large and dark-colored, possibly a Great Dane.

# Thought: The most prominent objects in the image are dogs. The image description tells us that there are five different breeds of dogs present.
# Object: dog

# Information: 
# ImageDescription: The image is a drawing of four individuals seated on a patterned bus or train with green upholstered seats. The individuals are holding musical instruments, which include a double bass, a guitar, a violin, and a banjo. The scene appears to represent a group of musicians traveling together.

# Thought: The most obvious object is the man sitting in the front of the group, who is part of a larger scene with musical instruments.
# Object: man sitting in the front


# PROMPT = """You are a smart information processor. Now I will provide you with some information that was extracted from a picture using tools. Please extract an object from the information. Your response should contain two parts: 
# ```
# Thought: The thinking process of how you select the countable object.
# Object: The object you extracted, possibly with some additional information.
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
# ImageDescription: The image shows five dogs of different breeds and sizes sitting in a row against a white background. From left to right, the first dog appears to be a Beagle, the third dog a Golden Retriever, and the fifth dog is large and dark-colored, possibly a Great Dane.

# Thought: The most obvious object is the dog.
# Object: dog"""

# EXAMPLES2 = """Information: 
# ImageDescription: The image is a drawing of four individuals seated on a patterned bus or train with green upholstered seats. The individuals are holding musical instruments, which include a double bass, a guitar, a violin, and a banjo. The scene appears to represent a group of musicians traveling together.

# Thought: The most obvious object is the man sitting in the front.
# Object: man sitting in the front"""

# FINAL_PROMPT = """Now that you have learned the method and format of the reply through examples, I will provide you with the information to be handled, please make your answer.
# NOTE: You would better use the information provided in the LAST paragraph to make your answer, so that the information would become a complete process.

# Information: 
# {content}
# """