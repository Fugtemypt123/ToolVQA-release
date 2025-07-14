# 0. [Caption, OCR]
# Q: which school does the cheerleaders represent?
# A: HUDSON


OT_EXAMPLES_0 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": None,
        "input": {
            "image": 'image/input.png'
        },
        "output": """The image shows a group of cheerleaders wearing matching navy blue and white uniforms with the word "HUDSON" written on the front. They appear to be performing or preparing for a cheer routine, walking forward in a gymnasium. Some of the cheerleaders are smiling, and their hair is tied up with white bows.""",
        "thought": "To answer the question, we first need to use the ImageDescription tool to identify the information of the cheerleaders in the image."
    },
    {
        "name": "OCR",
        "thought_query": "Now we know there are cheerleaders representing a school named 'HUDSON' in the image. We can use the OCR tool to extract more information from the image.",
        "thought_choose": None,
        "input": {
            "image": 'image/input.png'
        },
        "output": """(654, 212, 896, 263) HUDSON
(91, 238, 142, 261) HUA
(145, 233, 258, 283) HUDSON
(559, 244, 675, 292) HUDSON
(360, 269, 492, 327) HUDSON
""",
        "thought": "Now we know there are cheerleaders representing a school named 'HUDSON' in the image. We can use the OCR tool to further confirm the school name."
    },
    {
        "name": "Question",
        "thought": "The last tool used is OCR, which confirmed the school name represented by the cheerleaders in the image. Based on this result, we can formulate a question about the school represented by the cheerleaders. To ensure the answer requires viewing the image, we should avoid directly mentioning the school name.",
        "ori_question": "Which school does the cheerleaders represent?",
        "question": "Which school does the cheerleaders represent?",
        "rethink": None,
        "answer": "HUDSON"
    }
]