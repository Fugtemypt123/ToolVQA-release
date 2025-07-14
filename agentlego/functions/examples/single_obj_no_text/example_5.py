# 1. [Caption]
# Q: What is a specific type of the animal in the picture?
# A: fish


SONT_EXAMPLES_5 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": None,
        "input": {
            "image": 'image/input.png'
        },
        "output": """The image shows a tidy, modern desktop setup. There is a large monitor displaying an image of a red car, with a set of silver speakers on both sides of the screen. In front of the monitor, there is a keyboard, mouse, and a docked smartphone. To the left, there is a round fishbowl with some plants inside, while on the right, there’s a small gadget, likely a personal media player with a docking station. The desk is minimalistic, with clean lines and a glass top, against a blue wall.""",
        "thought": """To provide an accurate answer, I need to know what type of animal is in the image. I will use the ImageDescription tool to identify the animal in the provided image."""
    },
    {
        "name": "Question",
        "thought": "The last tool used is ImageDescription, which tells us there are several objects in the image, including a red car, speakers, a keyboard, mouse, smartphone, fishbowl, plants, and a personal media player. We can propose an interesting Brain Teasers question based on this information, asking for a specific type of animal in the image. This question requires analyzing the image to determine the answer, since the fishbowl indicates the presence of a fish.",
        "ori_question": "What is a specific type of the animal in the picture?",
        "question": "What is a specific type of the animal in the picture?",
        "rethink": None,
        "answer": "fish"
    }
]