# 3. [Caption, Detection, RAD, Search]
# Q: What are the top one producing areas of the fruit on the right in the United States in 2021?
# A: Washington


MONT_EXAMPLES_3 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "The image shows a bunch of ripe yellow bananas next to a single red apple on a white background. We can use the TextToBbox tool to locate the fruit on the right.",
        "input": {
            "image": 'image/input.png'
        },
        "output": "The image shows a bunch of ripe yellow bananas next to a single red apple on a white background.",
        "thought": "To solve this problem, we first need to use the ImageDescription tool to gather information of the fruit on the right."
    },  
    {
        "name": "TextToBbox",
        "thought_query": "Now that we know the image contains a bunch of ripe yellow bananas next to a single red apple, we can locate which fruit is on the right.",
        "thought_choose": "After obtaining the coordinates of the fruit on the right, we can use the RegionAttributeDescription tool to describe the fruit's fine-grained information.",
        "input": {
            "image": 'image/input.png',
            "text": 'fruit'
        },
        "output": """(394, 100, 651, 353), score 81\n(48, 79, 369, 350), score 69""",
        "thought": "To identify the top one producing areas of the fruit in the United States in 2021, I first need to identify the fruit shown in the image provided by the user. I will use the TextToBbox tool to detect the fruit in the image. Then recognize what fruit it is in the right bounding box. Finally I will search for its top producing areas in the US in 2021 using the GoogleSearch tool.\n" 
    },
    {
        "name": "RegionAttributeDescription",
        "thought_query": "Now that we know the location of the fruit on the right is (394, 100, 651, 353), we can further describe which type of fruit it is.",
        "thought_choose": "Now that we know the fruit on the right is an apple, we can use the GoogleSearch tool to search more information about the apples.",
        "input": {
            "image": 'image/input.png',
            "bbox": "(394, 100, 651, 353)",
            "attribute": "the type of fruit"
        },
        "output": "The image shows a red apple. It's a round fruit with a smooth, shiny skin and a small stem on top.",
        "thought": "I will describe the bounding box (394, 100, 651, 353) to ask the type of fruit."
    },
    {
        "name": "GoogleSearch",
        "thought_query": "Now that we know that the fruit on the right side of the picture is an apple, we can search for more factual information about apples, such as the region with the highest apple production in the United States. To ensure the uniqueness of the answer, we need to add a specific time, such as the region with the highest apple production in the United States in 2021",
        "thought_choose": "Now that we have gathered the information for the top one apple producing areas in the United States in 2021, we can formulate a complete question based on this information, allowing us to conclude the tool call process.",
        "input": {
            "query": "top one apple producing areas in the United States 2021"
        },
        "output": """1 - Answer box: At the state level, Washington will remain the nation's top producer with an estimated crop of 176.2 million bushels valued at almost $2.3 billion.""",
        "thought": "Now that I know the fruit is an apple. I'll search for its top producing areas in the US in 2021."
    },
    {
        "name": "Question",
        "thought": "The final tool used is GoogleSearch, which informed us that Washington is the top one producing areas of the fruit on the right in the United States in 2021. Based on this result, we can formulate a question about the top one producing areas of the apple in the United States in 2021. To ensure the answer requires viewing the image, we should avoid directly mentioning the fruit name 'apple,' instead referring to the position of this fruit in the image. Additionally, we need to summarize the information returned by the last tool as a single word to keep the answer concise.",
        "ori_question": "What are the top one producing areas of apple in the United States in 2021?",
        "question": "What are the top one producing areas of the fruit on the right in the United States in 2021?",
        "rethink": "The original question directly mentioned the fruit name 'apple,' which is visible in the image. To ensure the answer must refer to the image, the question should be adjusted to implicitly reference the fruit on the right",
        "answer": "Washington"
    }
]