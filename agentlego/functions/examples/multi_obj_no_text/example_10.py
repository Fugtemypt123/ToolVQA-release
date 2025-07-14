# 0. [Caption, CountGivenObject]
# Q: How many sinks are there?
# A: 1


MONT_EXAMPLES_10 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": None,
        "input": {
            "image": 'image/input.png'
        },
        "output": """The image shows an old-fashioned kitchen with wooden cabinets and a yellow-painted wall. There is a white oven built into the cabinetry and a stovetop with four burners to the right. Above the stovetop is a white range hood. A chandelier with multiple lights hangs from the ceiling, and there is a small window with vertical blinds near the back wall. The overall appearance suggests a dated or retro-style kitchen.""",
        "thought": "To answer the question, we first need to use the ImageDescription tool to identify the number of sinks in the image."
    },
    {
        "name": "CountGivenObject",
        "thought_query": "Now we know the image shows an old-fashioned kitchen. We can use the CountGivenObject tool to count the number of sinks in the image.",
        "thought_choose": None,
        "input": {
            "image": 'image/input.png',
            "text": 'sink'
        },
        "output": """1""",
        "thought": "Now we know the image shows an old-fashioned kitchen. We can use the CountGivenObject tool to count the number of sinks in the image."
    },
    {
        "name": "Question",
        "thought": "The last tool used is CountGivenObject, which determined the number of sinks in the image. Based on this result, we can formulate a question about the number of sinks. To ensure the answer requires viewing the image, we should avoid directly mentioning the object name.",
        "ori_question": "How many sinks are there?",
        "question": "How many sinks are there?",
        "rethink": None,
        "answer": "1"
    }
]