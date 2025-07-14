GOOGLESEARCH_PROMPT = """You are a smart information processor. I will provide you with some information extracted from a picture using tools, and your task is to propose a valuable online query based on this information.

Your response should consist of two parts:

1. **Thought:** Explain your reasoning for why the query is worth searching, considering the context of the information provided.
2. **Query:** Propose the query, which can be based directly on the information or involve reasonable external knowledge. **NOTE:** It’s best to search for factual content rather than open-ended questions. For example, questions like 'In what year was a certain animal discovered?' or 'Who is the founder of a certain company?' are good search questions, while 'What is the advice for a certain situation?' is not a good search question.

Here are some examples to guide you:

Example 1:
```
{example1}
```

Example 2:
```
{example2}
```

Now that you understand the format, I will provide you with the information. Please propose your query using the same structure.

Information:  
{context}
"""


# Information:
# ImageDescription: The image shows five dogs of different breeds and sizes sitting in a row against a white background. The dogs are a mix of small to large breeds, ranging from a beagle on the left to a larger, dark-colored dog on the right. They are all facing forward with some having their tongues out.
# TextToBbox: The 'dogs' in the image are at (762, 75, 936, 532), (595, 89, 763, 518), (423, 140, 608, 520), (82, 265, 253, 510), (272, 220, 424, 508).
# RegionAttributeDescription: The attribute 'breed' of the region (423, 140, 608, 520) is as follows:
# Golden Retriever

# Thought: Now that we know the breed of the dog in the middle is a Golden Retriever, we can search for information on what to consider when raising this breed.
# Query: What to consider when raising a Golden Retriever?

# Information:
# ImageDescription: The image shows a collection of toy animal figurines arranged in rows. The animals depicted include a deer, lion, polar bear, bison, panda, hippopotamus, leopard, rhinoceros, bear, elephant, tiger, and antelope.

# Thought: Now that we know there are 12 different animals in the image, most of which are wild, an important task for modern humans is to protect wildlife. Therefore, a worthwhile question to search for is which of these animals are endangered species.
# Query: Endangered status of deer, lion, polar bear, bison, panda, hippopotamus, leopard, rhinoceros, bear, elephant, tiger, antelope in 2024

# PROMPT = """You are a smart information processor. Now I will provide you with some information that was extracted from a picture using tools. Please propose a valuable query that needs to be searched online based on the information. Your response should contain two parts: 
# ```
# Thought: The thinking process of which query is worth searching.
# Query: The query you propose, such as 'Vitamin C content in oranges per 100g', 'The price of the iPhone 13 in September 2024'. It can appear in the information, or you can supplement some reasonable external knowledge based on the information.
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
# OCR: The texts and their coordinates in the image are as follows:
# (57, -2, 547, 190) R EGENcy CAFE

# Thought: We know that the café is named "REGENCY CAFE", but if we want to try it, we also need to search for its location.
# Query: Regency Cafe location"""

# EXAMPLES2 = """Information:
# ImageDescription: The image features three individuals standing with their arms crossed. The person on the left is wearing a light blue shirt, the person in the middle is dressed in a striped sweater with shades of grey, and the person on the right is in a light-colored shirt. The background is plain white.
# CountGivenObject: The number of 'men' in the image is 3.

# Thought: If we want to buy a gift for these men that they like, such as NVIDIA GeForce RTX 4070 SUPER GPU, we need to search for the current price of this GPU.
# Query: NVIDIA GeForce RTX 4070 SUPER price September 2024"""

# FINAL_PROMPT = """Now that you have learned the method and format of the reply through examples, I will provide you with the information to be handled, please make your answer.
# NOTE: You would better use the information provided in the LAST paragraph to make your answer, so that the information would become a complete process.

# Information:
# {content}
# """

# TODO: change the 'NVIDIA' example, it appeared too suddenly
# TODO: add multi object examples, like 'mammal animals'*********
# TODO: add icl retrieval examples(?)

# GOOGLESEARCH_PROMPT = """You are a smart information processor. I will provide you with some information extracted from a picture using tools, and your task is to propose a valuable online query based on this information.

# Your response should consist of two parts:

# 1. **Thought:** Explain your reasoning for why the query is worth searching, considering the context of the information provided.
# 2. **Query:** Propose the query, which can be based directly on the information or involve reasonable external knowledge.

# Here are some examples to guide you:

# Example 1:
# ```
# Information:
# OCR: The texts and their coordinates in the image are as follows:
# (57, -2, 547, 190) R EGENcy CAFE

# Thought: The name "REGENCY CAFE" is extracted from the image. If someone wants to visit, they would need to know its location. Searching for the café's location would be useful.
# Query: Regency Cafe location
# ```

# Example 2:
# ```
# Information:
# ImageDescription: The image shows a scene with a sleeping puppy and a kitten sitting next to it. The puppy has a brown fur coat, while the kitten has a mix of white and gray fur. They are on a light surface with a white fabric background, creating a calm and cozy atmosphere.

# Thought: The image highlights a peaceful interaction between a puppy and a kitten, both of which are mammals. A search query to learn more about mammals could provide valuable information.
# Query: Mammal animal characteristics
# ```

# Example 3:
# ```
# Information:
# ImageDescription: The image shows the upper part of a brown bear, with its ears visible and fur clearly seen. The background consists of green grass and some patches of dry grass.

# Thought: The image focuses on a bear, which often appears as a character in works of art or media. A useful query could be to find cartoons that feature bears as main characters.
# Query: Cartoons with bears as main characters
# ```

# Now that you understand the format, I will provide you with the information. Please propose your query using the same structure.

# Information:  
# {content}
# """