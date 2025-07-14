# 1. [Caption, OCR]
# Q: what store sign is this?
# A: katz


OT_EXAMPLES_1 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": None,
        "input": {
            "image": 'image/input.png'
        },
        "output": """The image shows a vintage-style storefront sign for "Katz Drugs." The sign prominently displays services such as "Prescriptions," "Cosmetics," and "Farmacia." There is also a sign for "Western Union" on the lower part of the facade. The building has a retro aesthetic with bold signage and is colored in teal with large, lit-up lettering.""",
        "thought": "To answer the question, we first need to use the ImageDescription tool to identify the information of the storefront sign in the image."
    },
    {
        "name": "OCR",
        "thought_query": "Now we know the store sign in the image is for 'Katz Drugs.' We can use the OCR tool to extract more information from the image.",
        "thought_choose": None,
        "input": {
            "image": 'image/input.png'
        },
        "output": """(116, 198, 155, 234) KATZ
(212, 123, 888, 398) Kaig DRUGS
(309, 344, 777, 449) PRESCRIPTIONS
(347, 435, 737, 516) COSMETICS
(768, 527, 919, 556) G
(674, 536, 856, 577) WESTERN
(729, 559, 858, 597) UNION
(205, 583, 540, 658) TARMACIA
(695, 591, 838, 620) Lamaneramas rapida
(668, 603, 869, 635) de eniar dinero a todo el mumdo.
""",
        "thought": "Now we know the store sign in the image is for 'Katz Drugs.' We can use the OCR tool to further confirm the store name."
    },
    {
        "name": "Question",
        "thought": "The last tool used is OCR, which confirmed the store sign in the image. Based on this result, we can formulate a question about the store sign. To ensure the answer requires viewing the image, we should avoid directly mentioning the store name.",
        "ori_question": "What store sign is this?",
        "question": "What store sign is this?",
        "rethink": None,
        "answer": "Katz"
    }
]