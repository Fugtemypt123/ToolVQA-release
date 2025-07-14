# 4. [Caption, Detection, RAD]
# Q: What color are the eyes of the white cat in the picture?
# A: blue


MONT_EXAMPLES_4 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "The image contains two cats but does not provide much additional detail. We can use the TextToBbox tool to obtain the coordinates of each cat and further gather fine-grained information.",
        "input": {
            "image": 'image/input.png'
        },
        "output": "The image features two cats snuggling together. The cat on the left is white, while the cat on the right has a grey and black striped pattern. They are close to each other, appearing affectionate and cozy.",
        "thought": "To solve this problem, we first need to use the ImageDescription tool to gather information about the cats in the image."
    },
    {
        "name": "TextToBbox",
        "thought_query": "The most prominent object in the image is a cat. The image description indicates that there are two cats: one white and one gray. Let's choose the white cat.",
        "thought_choose": "After obtaining the coordinates of the cats, we can use the RegionAttributeDescription tool to describe their fine-grained information.",
        "input": {
            "image": 'image/input.png',
            'text': 'white cat'
        },
        "output": "(49, 1, 342, 240), score 72",
        "thought": "Now we know there are 2 cats in the image. I should locate the white cat in the image and then describe the region where the eyes of the cat are located."
    },
    {
        "name": "RegionAttributeDescription",
        "thought_query": "Now that we know the location of the white cat in the image is (423, 140, 608, 520), we can further describe its eye color.",
        "thought_choose": "Now that we know the white cat's eyes in the image are blue, this fine-grained information can be used to formulate a challenging question, allowing us to conclude the tool call process.",
        "input": {
            "image": 'image/input.png',
            "bbox": "(49, 1, 342, 240)",
            "attribute": "eye color"
        },
        "output": "The image features a close-up of a white cat with blue eyes. The cat's eyes are a striking shade of blue, which adds a unique and captivating element to the scene. The cat appears to be looking at the camera, possibly curious or interested in its surroundings. The blue eyes of the cat stand out against the white fur, creating a visually striking contrast.",
        "thought": "I will describe the bounding box (49, 1, 342, 240) to ask the cat's eye color."
    },
    {
        "name": "Question",
        "thought": "The last tool used is RegionAttributeDescription, which provides information about the eye color of the white cat in the image. Based on this result, we can formulate a question about the eye color of the cat. Since there are two cats in the image, we need to specify that we are inquiring about the eye color of the white cat.",
        "ori_question": "What color are the eyes of the white cat with the blue eyes in the picture?",
        "question": "What color are the eyes of the white cat in the picture?",
        "rethink": "The original question directly included the answer. We should adjust the question to remove the answer from it.",
        "answer": "blue"
    }
]