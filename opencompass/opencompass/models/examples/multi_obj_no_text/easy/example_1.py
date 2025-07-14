# 0. [Caption, CountGivenObject]
# Q: How many men are in the picture?
# A: 1


MONT_EXAMPLES_1 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": None,
        "input": {
            "image": 'image/input.png'
        },
        "output": """The image shows three people sitting on a couch in a living room, engaged with what appears to be a video game. The person in the middle is holding a video game controller, and there is a table in front of them with various items, including a drink can, some snacks, and a laptop. A framed portrait hangs on the wall in the background, and a floor lamp is providing light to the room. The setting has a casual and cozy atmosphere, with people focusing on the game.""",
        "thought": "To answer the question, we first need to use the ImageDescription tool to identify the persons in the image."
    },
     {
        "name": "CountGivenObject",
        "thought_query": "Now we know the image shows three people sitting on a couch in a living room. We can use the CountGivenObject tool to count the number of men",
        "thought_choose": None,
        "input": {
            "image": 'image/input.png',
            "text": 'men'
        },
        "output": """1""",
        "thought": "Now we know the image shows three people sitting on a couch in a living room. We can use the CountGivenObject tool to count the number"
    },
    {
        "name": "Question",
        "thought": "The last tool used is CountGivenObject, which determined the number of the men in the image. Based on this result, we can formulate a question about it. To ensure the answer requires viewing the image, we should avoid directly mentioning the object name.",
        "ori_question": "How many men are in the picture?",
        "question": "How many men are in the picture?",
        "rethink": None,
        "answer": "1"
    }
]