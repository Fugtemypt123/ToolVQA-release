# 2. [Caption, OCR, Calculator]
# Q: If I buy two of this item, how much do I save compared to the market price?
# A: 624
# image: /network_space/server126/shared/yinshaofeng/ToolLLM/GTA/datasets/MTWI/image_train/T1I01uFk8aXXXXXXXX_!!0-item_pic.jpg.jpg


OT_EXAMPLES_2 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "Now we know the image is an advertisement for Audio-Technica earphones. We can use the OCR tool to extract more information from the image.",
        "input": {
            "image": 'image/input.png'
        },
        "output": """The image is an advertisement for Audio-Technica earphones. It features a close-up of the earphones which have a metallic and red finish combined with black earbuds. The prominent text includes the price "¥288" and mentions a previous market price of "¥600." The advertisement is in Chinese and includes phrases like "疯卖4100条" and "全国独家发售," indicating a special sale, along with other descriptions of features and accolades like "VGP金奖." Various color options and what looks like promotional items or additional features are also highlighted at the bottom.""",
        "thought": "To answer the question, we first need to use the ImageDescription tool to identify the information of the item in the image."
    },
    {
        "name": "OCR",
        "thought_query": "Now we know the image is an advertisement for Audio-Technica earphones. We can use the OCR tool to extract more information from the image.",
        "thought_choose": "Now we have extracted the text from the image, we can use the Calculator tool to calculate the cost related to the price of the earphones.",
        "input": {
            "image": 'image/input.png'
        },
        "output": """(223, 14, 354, 33) alwayslistening
(419, 15, 598, 95) 288
(58, 35, 357, 71) audio-technica
(399, 68, 414, 89) ?
(65, 85, 319, 121) 全国独家发售
(419, 100, 587, 126) 市场价￥：600元
(484, 198, 566, 240) 疯卖
(475, 243, 576, 270) 4100条
(417, 439, 554, 473) VGP金奖
(272, 451, 305, 484) 赠
(427, 511, 547, 539) 女声利器""",
        "thought": "Now we know the image is an advertisement for Audio-Technica earphones. We can use the OCR tool to extract more information from the image."
    },
    {
        "name": "Calculator",
        "thought_query": "Now that we know the image is an advertisement for Audio-Technica earphones and the price is ¥288, and the market price is ¥600. Based on these information, we can use the Calculator tool to calculate the savings compared to the market price. Let' say we buy two of this item and calculate the savings.",
        "thought_choose": "Now we have the calculation result, we can propose a question based on this information, allowing us to conclude the tool call process.",
        "input": {
            "expression": "(600 - 288) * 2"
        },
        "output": "624",
        "thought": "Now that we know the price of the earphones is ¥288 and the market price is ¥600, we can use the Calculator tool to calculate the savings when buying two of this item compared to the market price."
    },
    {
        "name": "Question",
        "thought": "The last tool used is Calculator, which informed us that if we buy two of this item, we would save ¥624 compared to the market price. Based on this result, we can formulate a question about the savings when buying two of this item compared to the market price. To ensure the answer requires viewing the image, we should avoid directly mentioning the price of the earphones and the market",
        "ori_question": "If I buy two of this item, how much do I save compared to the market price? Suppose the price is ¥288 and the market price is ¥600.",
        "question": "If I buy two of this item, how much do I save compared to the market price?",
        "rethink": "The original question directly mentioned the price of the earphones and the market price, which is visible in the image. To ensure the answer must refer to the image, the question should be adjusted to remove the specific price of the earphones and the market price.",
        "answer": "624"
    }
]