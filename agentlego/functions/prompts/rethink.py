RETHINK_QUESTION_PROMPT = """You are a smart question improver. I will provide you with an original question related to an image, along with some information about the image. Now you need to replace the proper nouns that appear in the ImageDescription in the question with pronouns. For example, if the ImageDescription contains 'zebra', then you need to replace 'zebra' in the question with 'the animal in the image'. 

Your response should consist of two parts:
1. **Thought:** Explain your reasoning process on how you adjusted the question.
2. **Adjusted Question:** Present the modified question. If no adjustment was necessary, just restate the original question.

Here are some examples for clarity:

Example 1:
```
ImageDescription: The image shows a close-up of a Rolex Submariner wristwatch. The watch has a stainless steel band and a black dial with large luminous markers and white hands. Notably, it features a green bezel and displays text indicating water resistance of 1000 ft = 300 meters. The watch is being held by a gloved hand.
Original Question: How many hours is the power reserve of this Rolex Submariner watch?

Thought: The noun 'this Rolex Submariner watch' appears in the ImageDescription, I will replace it with a pronoun 'this watch'.
Adjusted Question: How many hours is the power reserve of this watch?
```

Example 2:
```
ImageDescription: The image shows a serene African savanna landscape with five elephants walking in the grass. They are positioned near a large Acacia tree, which provides some shade. The open grassland extends into the horizon, suggesting a vast and open area typical of a savanna ecosystem.
Original Question: What is the ecological role of elephants in the African savanna and how do they impact other species?

Thought: The noun 'elephants' appears in the ImageDescription, I will replace it with a pronoun 'this animal'.
Adjusted Question: What is the ecological role of this animal in the African savanna and how does it impact other species?
```

Example 3:
```
ImageDescription: The image shows a close-up of a Rolex Submariner wristwatch. The watch has a stainless steel band and a black dial with large luminous markers and white hands. Notably, it features a green bezel and displays text indicating water resistance of 1000 ft = 300 meters. The watch is being held by a gloved hand.
Original Question: Can this watch be worn while swimming?

Thought: The noun 'this watch' is already a pronoun and does not need adjustment.
Adjusted Question: Can this watch be worn while swimming?
```

Now, I will provide you with the information to be handled. Please make the necessary adjustments and respond using the above format.

{context}
"""


# RETHINK_QUESTION_PROMPT = """You are a smart question improver. I will provide you with an original question related to an image, along with some information about the image. Please optimize the original question to meet the following requirements: 

# 1. The question must require viewing the image to answer. If the question directly reveals information from the image, that information needs to be concealed. For example, if the image describes 'zebras,' and the question is 'What is the typical grazing behavior of zebras?', it should be adjusted to 'What is the typical grazing behavior of this animal?'

# 2. The question must not directly contain the answer. For instance, if the question is 'What is the significance of the proximity between airports and industrial ports in relation to trade?' and the answer is 'trade,' it should be changed to 'What is the significance of the proximity between airports and industrial ports?'" 

# Your response should consist of two parts:
# 1. **Thought:** Explain your reasoning process on how you adjusted the question.
# 2. **Adjusted Question:** Present the modified question. If no adjustment was necessary, just restate the original question.

# Here are some examples for clarity:

# Example 1:
# ```
# {example1}
# ```

# Example 2:
# ```
# {example2}
# ```

# Now, I will provide you with the information to be handled. Please make the necessary adjustments and respond using the above format.

# {context}
# """

# RETHINK_QUESTION_PROMPT = """You are a smart question improver. I will provide you with an original question related to an image, along with some information about the image. Now you need to replace the proper nouns that appear in the ImageDescription in the question with pronouns. For example, if the ImageDescription contains 'zebra', then you need to replace 'zebra' in the question with 'the animal in the image'. 

# Your response should consist of two parts:
# 1. **Thought:** Explain your reasoning process on how you adjusted the question.
# 2. **Adjusted Question:** Present the modified question. If no adjustment was necessary, just restate the original question.

# Here are some examples for clarity:

# Example 1:
# ```
# ImageDescription: The image shows a close-up of a Rolex Submariner wristwatch. The watch has a stainless steel band and a black dial with large luminous markers and white hands. Notably, it features a green bezel and displays text indicating water resistance of 1000 ft = 300 meters. The watch is being held by a gloved hand.
# Original Question: How many hours is the power reserve of this Rolex Submariner watch?

# Thought: The noun 'this Rolex Submariner watch' appears in the ImageDescription, I will replace it with a pronoun 'this watch'.
# Adjusted Question: How many hours is the power reserve of this watch?
# ```

# Example 2:
# ```
# ImageDescription: The image shows a serene African savanna landscape with five elephants walking in the grass. They are positioned near a large Acacia tree, which provides some shade. The open grassland extends into the horizon, suggesting a vast and open area typical of a savanna ecosystem.
# Original Question: What is the ecological role of elephants in the African savanna and how do they impact other species?

# Thought: The noun 'elephants' appears in the ImageDescription, I will replace it with a pronoun 'this animal'.
# Adjusted Question: What is the ecological role of this animal in the African savanna and how does it impact other species?
# ```

# Example 3:
# ```
# ImageDescription: The image shows a close-up of a Rolex Submariner wristwatch. The watch has a stainless steel band and a black dial with large luminous markers and white hands. Notably, it features a green bezel and displays text indicating water resistance of 1000 ft = 300 meters. The watch is being held by a gloved hand.
# Original Question: Can this watch be worn while swimming?

# Thought: The noun 'this watch' is already a pronoun and does not need adjustment.
# Adjusted Question: Can this watch be worn while swimming?
# ```

# Now, I will provide you with the information to be handled. Please make the necessary adjustments and respond using the above format.

# {context}
# """


# Original Question: If you want to buy 3 Apple Magic Mouses, according to the search results, how many dollars will you need to spend in total?

# Image Description: The image shows a close-up view of a white Apple mouse placed near a white keyboard. The mouse has a sleek, curved design and features the Apple logo. The keyboard has a modern, compact design with white keys. Both devices are connected with cables.

# Thought: The original question explicitly mentions 'Apple Magic Mouses,' which directly refers to the image. To ensure the model must look at the image, the mention of 'Apple Magic Mouses' should be replaced with a description that implicitly references the mouse in the image.
# Adjusted Question: If you want to buy 3 Mouses in the picture, according to the search results, how many dollars will you need to spend in total?

# Original Question: What are the possible functions of zebra stripes based on their significance in their natural habitat?

# ImageDescription: The image shows the rear view of two zebras standing side by side. Their distinctive black and white striped patterns are clearly visible. The background features a fence and some dried leaves on the ground.

# Thought: The original question directly mentions 'zebra stripes,' which are visible in the image. To ensure the model must look at the image, the question should be adjusted to refer to the stripes implicitly.
# Adjusted Question: What are the possible functions of the stripes on the animal in the picture based on their significance in their natural habitat?

# Original Question: How many visible items in this image are specifically related to coffee?

# ImageDescription: This photo shows a table in a restaurant with a dessert menu prominently displayed in the foreground. The menu features an image of a dessert with ice cream on top. A yellow coffee cup filled with a drink is placed on the table, along with a coffee creamer and a spoon. There are also various items such as salt and pepper shakers, cutlery, and multiple glasses of water. People can be seen reading the menu in the background. The table looks cluttered, indicating a busy dining scene.

# Thought: The question implicitly mentions the information in the picture, so no adjustment is needed.
# Adjusted Question: How many visible items in this image are specifically related to coffee?

# You are a smart question improver. I will provide you with an original question related to an image, along with some information about the image. Please optimize the original question to meet the following requirements: 

# 1. The question must require viewing the image to answer. If the question directly reveals information from the image, that information needs to be concealed. For example, if the image describes 'zebras,' and the question is 'What is the typical grazing behavior of zebras?', it should be adjusted to 'What is the typical grazing behavior of this animal?'

# 2. The question must not directly contain the answer. For instance, if the question is 'What is the significance of the proximity between airports and industrial ports in relation to trade?' and the answer is 'trade,' it should be changed to 'What is the significance of the proximity between airports and industrial ports?'" 

# Your response should consist of two parts:
# 1. **Thought:** Explain your reasoning process on how you adjusted the question.
# 2. **Adjusted Question:** Present the modified question. If no adjustment was necessary, just restate the original question.

# Here are some examples for clarity: