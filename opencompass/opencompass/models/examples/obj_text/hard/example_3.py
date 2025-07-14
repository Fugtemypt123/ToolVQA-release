# 3. [Caption, OCR, Calculator]
# Q: If I want to buy 200 (2 packs) of balloons and 1 pump, how much should I pay?
# A: 15.6
# image: /network_space/server126/shared/yinshaofeng/ToolLLM/GTA/datasets/MTWI/image_train/T1bQ1NFtxiXXXXXXXX_!!0-item_pic.jpg.jpg


OT_EXAMPLES_3 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "Now we know the image shows a cluster of purple and silver balloons. There is text in Chinese and large red numbers '7.8元/100个' indicating a price, suggesting a sale or promotion for balloons. We can use the Calculator tool to calculate the total cost of purchasing 200 balloons.",
        "input": {
            "image": 'image/input.png'
        },
        "output": """The image shows a cluster of purple and silver balloons. There is text in Chinese and large red numbers "7.8元/100个" indicating a price, suggesting a sale or promotion for balloons.""",
        "thought": "To answer the question, I need to extract the information about the price of the balloons from the image provided. I will use the ImageDescription tool to describe the image and identify the relevant details."
    },
    {
        "name": "OCR",
        "thought_query": "The image shows a cluster of purple and silver balloons. There is text in Chinese and large red numbers '7.8元/100个' indicating a price. We can use the OCR tool to extract more information from the image.",
        "thought_choose": "Now we know the price of 100 balloons is 7.8元 and buying two packs of balloons will get a free pump, we can use the Calculator tool to calculate the cost of purchasing balloons and pump.",
        "input": {
            "image": 'image/input.png'
        },
        "output": """(6, 3, 371, 45) 珠光气球一包包邮
(68, 55, 293, 99) 两包送气筒
(337, 70, 377, 351) 三包送脚踩气筒""",
        "thought": "The image shows a cluster of purple and silver balloons. The text '7.8元/100个' indicates the price of 100 balloons. I will use the OCR tool to extract more information about pump from the image."
    },
    {
        "name": "Calculator",
        "thought_query": "Now that we know the image shows a cluster of purple and silver balloons, and the price is 7.8元/100个. We also know that buying two packs of balloons will get a free pump. Based on these information, let's use the Calculator tool to calculate the total cost of purchasing 200 balloons and 1 pump.",
        "thought_choose": "Now we have the calculation result, we can propose a question based on this information, allowing us to conclude the tool call process.",
        "input": {
            "expression": "7.8 / 100 * 200"
        },
        "output": "15.6",
        "thought": "Now that we know the price of 100 balloons is 7.8元, we can use Calculator to calculate the total cost of purchasing 200 balloons. Since buying two packs of balloons will get a free pump, we don't need to consider the cost of the pump."
    },
    {
        "name": "Question",
        "thought": "The last tool used is Calculator, which informed us that the total cost of purchasing 200 balloons and 1 pump is 15.6元. Based on this result, we can formulate a question about the total cost of purchasing 200 balloons and 1 pump. To ensure the answer requires viewing the image, we should avoid directly mentioning the price of the balloons.",
        "ori_question": "If I want to buy 200 (2 packs) of balloons and 1 pump, how much should I pay? Suppose the price is 7.8元/100个.",
        "question": "If I want to buy 200 (2 packs) of balloons and 1 pump, how much should I pay?",
        "rethink": "The original question directly mentioned the price of 100 balloons, which is visible in the image. To ensure the answer must refer to the image, the question should be adjusted to remove the specific price of the balloons",
        "answer": "15.6"
    }
]