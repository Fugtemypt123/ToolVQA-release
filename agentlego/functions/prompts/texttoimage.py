TEXTTOIMAGE_PROMPT = """You are a smart information processor. I will provide you with some information extracted from a picture using tools. Now you need to use your imagination to create a new picture based on the information provided. Please generate the keywords to describe the new picture you will create.

Your response should consist of two parts:

1. **Thought:** Explain your reasoning for selecting the keywords based on the information.
2. **Keywords:** Provide the keywords to describe the new picture you will create. No more than 4 keywords.
**NOTE:** You must NOT copy the information provided, instead, use it as inspiration to imagine a new scene. 

Here are some examples to guide you:

Example 1:
```
{example1}
```

Example 2:
```
{example2}
```

Now that you understand the format, I will provide you with the information. Please generate your keywords accordingly.

Information:  
{context}
"""


# Information:
# ImageDescription: The image features a dining table with a variety of food items and drinks arranged on it. There are several apples, grapes, and strawberries spread across the table, along with a bottle of apple juice. The table also has a bowl filled with grapes, and a cup placed nearby. 

# Thought: The description highlights the presence of apples, grapes, strawberries, and apple juice. I will use these food items as inspiration to create an image centered around a fruit-themed picnic.
# Keywords: picnic, apples, grapes, strawberries, juice, table

# Information:
# ImageDescription: The image shows a bear and a tiger in a grassy area. The tiger is lying on its side with a paw raised, while the bear is standing on all fours next to it. There is also a large rock in the background.
# GoogleSearch: The search results for 'What characters are included in 'Winnie-the-Pooh'?' are as follows:
# 1 - Answer box: Characters from the original books ___Winnie-the-Pooh. Main articles: Winnie-the-Pooh and Winnie the Pooh (Disney character) ... ___Christopher Robin. Main article: Christopher Robin. ... ___Tigger. Main article: Tigger. ... ___Piglet. Main article: Piglet (Winnie-the-Pooh) ... ___Rabbit. Main article: Rabbit (Winnie-the-Pooh) ... ___Kanga. ... ___Roo. ... ___Owl.

# Thought: Now that we have gathered all the characters from "Winnie-the-Pooh," we can create an image of these characters enjoying a meal together."
# Keywords: Winnie-the-Pooh, Christopher Robin, Tigger, Piglet, Rabbit, Kanga, Roo, Owl, enjoy meal


# PROMPT = """You are a smart information processor. Now I will provide you with some information that was extracted from a picture using tools. Please give some keywords based on the information to create a picture. Your response should contain two parts:
# ```
# Thought: The thinking process of how you select the keywords.
# Keywords: The keywords you generate based on the information.
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
# ImageDescription: The image features a dining table with a variety of food items and drinks arranged on it. There are several apples, grapes, and strawberries spread across the table, along with a bottle of apple juice. The table also has a bowl filled with grapes, and a cup placed nearby.\nIn addition to the food and drinks, there are two bottles on the table, one of which is likely containing apple juice. The table

# Thought: Based on the description from the image analysis, it seems the image contains apples, grapes, and strawberries, along with a bottle of apple juice. I will interpret this information creatively to generate a cake that might include fruit and juice as ingredients or themes.
# Keywords: cake, apples, grapes strawberries, juice"""

# EXAMPLE2 = """Information:
# ImageDescription: The image features a woman wearing a pink jacket, running on a sandy beach. She appears to be enjoying her time outdoors, possibly participating in a beach run or simply exercising. The woman is wearing a blue and white outfit, which complements her pink jacket. The scene captures her movement and energy as she runs across the sandy terrain.

# Thought: Based on the image description, the girl in the picture is wearing a pink top. I can generate an image of a boy walking on the grass, wearing a T-shirt in the same pink color.
# Keywords: boy walking on grass, pink T-shirt"""

# FINAL_PROMPT = """Now that you have learned the method and format of the reply through examples, I will provide you with the information to be handled, please make your answer.
# NOTE: You would better use the information provided in the LAST paragraph to make your answer, so that the information would become a complete process.

# Information: 
# {content}
# """

# TEXTTOIMAGE_PROMPT = """You are a smart information processor. I will provide you with some information extracted from a picture using tools. Your task is to generate meaningful keywords based on the information provided to create a new picture.

# Your response should consist of two parts:

# 1. **Thought:** Explain your reasoning for selecting the keywords based on the information.
# 2. **Keywords:** Provide the specific keywords you generated from the information.

# Here are some examples to guide you:

# Example 1:
# ```
# Information:
# ImageDescription: The image features a dining table with a variety of food items and drinks arranged on it. There are several apples, grapes, and strawberries spread across the table, along with a bottle of apple juice. The table also has a bowl filled with grapes, and a cup placed nearby. 

# Thought: The description highlights the presence of apples, grapes, strawberries, and apple juice. I will use these food items as inspiration to create an image centered around a fruit-themed picnic.
# Keywords: picnic, apples, grapes, strawberries, juice, table
# ```

# Example 2:
# ```
# Information:
# ImageDescription: The image features a woman wearing a pink jacket, running on a sandy beach. She appears to be enjoying her time outdoors, possibly participating in a beach run or simply exercising. The woman is wearing a blue and white outfit, which complements her pink jacket. The scene captures her movement and energy as she runs across the sandy terrain.

# Thought: The beach setting and the woman's vibrant pink jacket are key elements. I will use these details to create an image of a sunset beach scene with a person running.
# Keywords: sunset, beach, running, pink jacket
# ```

# Now that you understand the format, I will provide you with the information. Please generate your keywords accordingly.

# Information:  
# {content}
# """