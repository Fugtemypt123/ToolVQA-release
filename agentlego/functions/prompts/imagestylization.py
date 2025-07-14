IMAGESTYLIZATION_PROMPT = """You are a smart information processor. I will provide you with some information extracted from an image using tools. Your task is to give a meaningful instruction to transfer the style of the original image.

Your response should consist of two parts:

1. **Thought:** Explain your reasoning behind how you decide to transfer the style of the image.
2. **Instruction:** Provide the specific instruction for how the image should be transformed.

Here are some examples to guide you:

Example 1:
```
{example1}
```

Example 2:
```
{example2}
```

Now that you understand the format, I will provide you with the information. Please propose your style transfer instructions in the same format.

Information:  
{context}
"""


# Information:
# ImageDescription: The image features a large, old building with a distinctive pagoda-style roof, situated on a hillside. The building is surrounded by a beautiful landscape, including a river flowing nearby. The scene is further enhanced by the presence of several trees, adding a touch of nature to the scene.
# In the foreground, there is a small tree with a few pink flowers, adding a pop of color to the otherwise monochromatic scene.

# Thought: Since the image features a traditional building and serene nature, transforming it to an ukiyo-e style would enhance the historical and cultural aesthetic of the scene.
# Instruction: Convert to ukiyo-e style.

# Information:
# ImageDescription: The image features a blue sky with fluffy white clouds, creating a serene and peaceful atmosphere. In the foreground, there is a lush green field with colorful flowers, adding a touch of vibrancy to the scene. The image also includes a small pond with clear water, reflecting the blue sky and white clouds above. The overall composition of the image is balanced and harmonious, creating a sense of tranquility and beauty.

# Thought: The serene landscape with a bright blue sky and clouds suggests an idyllic setting. Adding fireworks in the sky could give it a lively and festive mood, creating a sharp contrast with the peaceful atmosphere.
# Instruction: Add fireworks to the sky.

# PROMPT = """You are a smart information processor. Now I will provide you with some information that was extracted from a picture using tools. Please give an instruction to transfer the style of the original image. Your response should contain two parts:
# ```
# Thought: The thinking process of how you decide to transfer the style of the image.
# Instruction: The specific instruction for the image transfer.
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
# ImageDescription: The image features a large, old building with a distinctive pagoda-style roof, situated on a hillside. The building is surrounded by a beautiful landscape, including a river flowing nearby. The scene is further enhanced by the presence of several trees, adding a touch of nature to the scene.\nIn the foreground, there is a small tree with a few pink flowers, adding a pop of color to the otherwise monochromatic scene. The combination of the old building

# Thought: Based on the description from the image analysis, it seems the image contains a large, old building with a pagoda-style roof, surrounded by a river and trees. I can transfer the style of the image to a ukiyo-e Style, which will enhance the traditional and historical elements of the scene.
# Instruction: convert to ukiyo-e style"""

# EXAMPLE2 = """Information:
# ImageDescription: The image features a blue sky with fluffy white clouds, creating a serene and peaceful atmosphere. In the foreground, there is a lush green field with colorful flowers, adding a touch of vibrancy to the scene. The image also includes a small pond with clear water, reflecting the blue sky and white clouds above. The overall composition of the image is balanced and harmonious, creating a sense of tranquility and beauty.

# Thought: Based on the description from the image analysis, it seems the image contains a serene and peaceful landscape with a blue sky, white clouds, and colorful flowers. I can add fireworks on the sky to create a festive atmosphere.
# Instruction: add fireworks to the sky"""

# FINAL_PROMPT = """Now that you have learned the method and format of the reply through examples, I will provide you with the information to be handled, please make your answer.
# NOTE: You would better use the information provided in the LAST paragraph to make your answer, so that the information would become a complete process.

# Information:
# {content}
# """