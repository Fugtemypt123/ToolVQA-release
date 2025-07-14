# 3. [Caption, Search, TextToImage]
# Q: Can you generate a picture of a shirt containing the above animals and plants, using the most popular art style of 2024?
# A: image/output.png


SONT_EXAMPLES_3 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "The image features a black and white drawing of a panda bear holding a bamboo branch. We can use GoogleSearch to find some external information.",
        "input": {
            "image": 'image/input.png'
        },
        "output": "The image features a black and white drawing of a panda bear, which is holding a bamboo branch in its mouth. The panda bear is positioned in the center of the scene, with the bamboo branch extending from its mouth towards the bottom of the image. The drawing is quite detailed, capturing the essence of the panda bear and its natural habitat.",
        "thought": "To generate a picture as requested, I need to first understand what the images contain to accurately use the \"TextToImage\" tool. I will start by analyzing the image provided to identify the animals and plants mentioned."
    },
    {
        "name": "GoogleSearch",
        "thought_query": "Now that we have identified the animals and plants in the image. In addition to this information, we can consider searching for some external knowledge. For example, if we want to convert this picture into a certain art style, we can search for the most popular art style in 2024.",
        "thought_choose": "Now that we have found the most popular art style of 2024, we can use TextToImage to generate a picture of a shirt containing the above animals and plants.",
        "input": {
            "query": "the most popular art style of 2024"
        },
        "output": """1 - Answer box: Top 8 Hottest Art Trends for 2024 | iCanvas Predictions ___Embrace Old-Fashioned Comfort With Grandpa Chic Art. ... ___Get A Bit Rugged With Brutalism Art. ... ___Dive Into Soft Luxury With Minimaluxe Art. ... ___Feel Happy With Dopamine Decor Art. ... ___Connect With The World Through Nature Renewal Art. ... ___Mix The Old & New With Authentic Eclectic Art.""",
        "thought": "Now that we have identified the animals and plants in the image, the next step is to search for the most popular art style of 2024. This information will help us create a picture that aligns with current artistic trends."
    },
    {
        "name": "TextToImage",
        "thought_query": "Now that we have identified the animals and plants in the image and the most popular art style of 2024, we can combine this information to generate a picture of a shirt containing the panda bear, bamboo branch, and Grandpa Chic Art style.",
        "thought_choose": "Now that we have successfully generated an image, we can conclude the tool call process.",
        "input": {
            "keywords": "panda bear, bamboo branch, shirt, Grandpa Chic Art",
        },
        "output": "image/output.png",
        "thought": "Now that we have identified the animals and plants in the image and the most popular art style of 2024, we can combine this information to generate a picture of a shirt containing the panda bear, bamboo branch, and Grandpa Chic Art style."
    },
    {
        "name": "Question",
        "thought": "The last tool used is TextToImage, which generated an image of a shirt containing a panda bear, bamboo branch, and the Grandpa Chic Art style. Based on this result, we can formulate a question to generate an image. To ensure the question requires viewing the image for an answer, we should avoid mentioning the specific animals, plants, or art style and instead refer to them indirectly.",
        "ori_question": "Can you generate a picture of a shirt containing a panda and a bamboo, using the Grandpa Chic Art style?",
        "question": "Can you generate a picture of a shirt containing the above animals and plants, using the most popular art style of 2024?",
        "rethink": "The original question directly mentioned the animals, plants, and art style, which can be inferred from the image information. To ensure the answer must refer to the image, the question should be adjusted to implicitly reference the animals, plants, and art style.",
        "answer": "image/output.png"
    }
]