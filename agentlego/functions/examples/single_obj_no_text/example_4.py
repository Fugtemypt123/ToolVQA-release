# 0. [Caption]
# Q: Which vehicle holds the most people?
# A: train


SONT_EXAMPLES_4 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": None,
        "input": {
            "image": 'image/input.png'
        },
        "output": """The image depicts a scene near a harbor with several parked boats and cars. In the background, there is a blue and red "Southwest" train crossing a bridge. A few people can be seen walking or standing nearby, and the atmosphere appears cloudy with overcast skies. The setting seems to combine transportation (train and boats) and leisure activities near the water.""",
        "thought": "To provide an accurate answer, I need to know what type of vehicle holds the most people. I will use the ImageDescription tool to identify the vehicles in the provided image."
    },
    {
        "name": "Question",
        "thought": "The last tool used is ImageDescription, which tells us there are several vehicles in the image, including several cars and a train. We can propose an interesting Brain Teasers question based on this information, asking which vehicle holds the most people. This question requires analyzing the image to determine the answer, since the common sense knowledge indicates that a train can carry more passengers than a car.",
        "ori_question": "Which vehicle holds the most people?",
        "question": "Which vehicle holds the most people?",
        "rethink": None,
        "answer": "train"
    }
]