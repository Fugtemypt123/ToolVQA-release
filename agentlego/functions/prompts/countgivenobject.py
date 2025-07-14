COUNTGIVENOBJECT_PROMPT = """You are a smart information processor. I will provide you with information that has been extracted from a picture using tools. Your task is to identify a countable object based on the information provided.

Your response should consist of two parts:

1. **Thought:** Explain your reasoning behind how you selected the countable object.
2. **Object:** State the countable object you identified, such as `apple`, `car`, `man`, etc. **NOTE:** If an object has already been identified by the 'CountGivenObject' tool, you should not select that same object again.

Here are some examples to clarify the process:

Example 1:
```
{example1}
```

Example 2:
```
{example2}
```

Now that you understand the method and format, I will provide you with the information to process. Please follow the same structure for your response.

Information:  
{context}
"""


# Information: 
# ImageDescription: The image shows five dogs of different breeds and sizes sitting in a row against a white background. From left to right, the first dog appears to be a Beagle, the third dog a Golden Retriever, and the fifth dog is large and dark-colored, possibly a Great Dane.

# Thought: The most visible and countable object in the image is the dog, as they are clearly distinguishable and mentioned explicitly in the description.
# Object: dog

# Information: 
# ImageDescription: This photo shows a table in a restaurant with a dessert menu prominently displayed in the foreground. The menu features an image of a dessert with ice cream on top. A yellow coffee cup filled with a drink is placed on the table, along with a coffee creamer and a spoon. There are also various items such as salt and pepper shakers, cutlery, and multiple glasses of water. People can be seen reading the menu in the background. The table looks cluttered, indicating a busy dining scene.
# CountGivenObject: The number of 'coffee cup' in the image is 1.

# Thought: Since the tool has already counted the coffee cups, I will select another visible countable object in the image. The coffee creamer is distinct and also related to coffee, making it a suitable choice.
# Object: coffee creamer


# ImageDescription: The image shows an elevated train track with a train moving through it. The train appears to be navigating a complex series of tracks and switches. The surrounding area includes various urban infrastructure elements, such as buildings, additional tracks, and industrial elements. The vantage point is from above, giving a clear view of the train and the rail network.
# CountGivenObject: The number of 'train' in the image is 2.

# Thought: Since the tool has already counted the trains, I will select another visible countable object in the image. The buildings are distinct and prominent, making them a suitable choice.
# Object: buildings


# PROMPT = """You are a smart information processor. Now I will provide you with some information that was extracted from a picture using tools. Please extract a countable object from the information. Your response should contain two parts: 
# ```
# Thought: The thinking process of how you select the countable object.
# Object: The object you extracted, such as `apple`, `car`, `man`, etc.
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

# Thought: The most obvious countable object is the dog.
# Object: dog"""

# EXAMPLES2 = """Information: 
# ImageDescription: The image depicts a serene mountainous landscape with a group of cows grazing in a lush, green meadow. The foreground features evenly spaced cows enjoying the fresh grass, while the middle ground showcases a dense forest of tall pine trees. The background features towering, rugged mountains with a mix of green vegetation and exposed rocky surfaces, all under a clear sky.

# Thought: The most obvious countable object is the cow.
# Object: cow"""

# FINAL_PROMPT = """Now that you have learned the method and format of the reply through examples, I will provide you with the information to be handled, please make your answer.
# NOTE: You would better use the information provided in the LAST paragraph to make your answer, so that the information would become a complete process.

# Information: 
# {content}
# """


# COUNTGIVENOBJECT_PROMPT = """You are a smart information processor. I will provide you with information that has been extracted from a picture using tools. Your task is to identify a countable object based on the information provided.

# Your response should consist of two parts:

# 1. **Thought:** Explain your reasoning behind how you selected the countable object.
# 2. **Object:** State the countable object you identified, such as `apple`, `car`, `man`, etc. **NOTE:** If an object has already been identified by the 'CountGivenObject' tool, you should not select that same object again.

# Here are some examples to clarify the process:

# Example 1:
# ```
# Information: 
# ImageDescription: The image shows five dogs of different breeds and sizes sitting in a row against a white background. From left to right, the first dog appears to be a Beagle, the third dog a Golden Retriever, and the fifth dog is large and dark-colored, possibly a Great Dane.

# Thought: The most visible and countable object in the image is the dog, as they are clearly distinguishable and mentioned explicitly in the description.
# Object: dog
# ```

# Example 2:
# ```
# Information: 
# ImageDescription: This photo shows a table in a restaurant with a dessert menu prominently displayed in the foreground. The menu features an image of a dessert with ice cream on top. A yellow coffee cup filled with a drink is placed on the table, along with a coffee creamer and a spoon. There are also various items such as salt and pepper shakers, cutlery, and multiple glasses of water. People can be seen reading the menu in the background. The table looks cluttered, indicating a busy dining scene.
# CountGivenObject: The number of 'coffee cup' in the image is 1.

# Thought: Since the tool has already counted the coffee cups, I will select another visible countable object in the image. The coffee creamer is distinct and also related to coffee, making it a suitable choice.
# Object: coffee creamer
# ```

# Now that you understand the method and format, I will provide you with the information to process. Please follow the same structure for your response.

# Information:  
# {content}
# """