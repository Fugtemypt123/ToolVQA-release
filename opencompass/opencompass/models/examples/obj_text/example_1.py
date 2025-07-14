# 1. [Caption, OCR, Search]
# Q: Where was this photo taken? Just tell me the city.
# A: London
# image: /network_space/server126/shared/yinshaofeng/ToolLLM/GTA/agentlego/gta_dataset/image/image_26.jpg


OT_EXAMPLES_1 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "Now we know the image depicts the exterior of a café named 'Regency Cafe.' We can use the OCR tool to extract more information from the image.",
        "input": {
            "image": 'image/input.png'
        },
        "output": """The image depicts the exterior of a café named "Regency Cafe." The facade features large windows with a checkered red and white curtain. The café's name is prominently displayed in large, white letters above the windows. The building is situated on a street corner with visible redbrick and black tile work. There is a "no entry" road sign visible on the side street outside the café.""",
        "thought": "To answer the question, we first need to use the ImageDescription tool to identify the information of the countries in the image."
    },
    {
        "name": "OCR",
        "thought_query": "Now we know the image depicts the exterior of a café named 'Regency Cafe.' We can use the OCR tool to extract more information from the image.",
        "thought_choose": "Now we have extracted the text from the image, we can use the GoogleSearch tool to search for the location where the photo was taken.",
        "input": {
            "image": 'image/input.png'
        },
        "output": """(69, 12, 543, 193) REGENCY CAFE""",
        "thought": "Now we know the image depicts the exterior of a café named 'Regency Cafe.' We can use the OCR tool to extract more information from the image."
    },
    {
        "name": "GoogleSearch",
        "thought_query": "Now we know the image depicts the exterior of a café named 'Regency Cafe.' We can use the GoogleSearch tool to search some facts about the café, such as its location.",
        "thought_choose": "Now we have the search result, we can propose a question based on this information, allowing us to conclude the tool call process.",
        "input": {
            "query": "Regency Cafe location"
        },
        "output": """1 - Answer box: 17-19 Regency St, London SW1P 4BY, UK""",
        "thought": "Now we know the image depicts the exterior of a café named 'Regency Cafe.' We can use the GoogleSearch tool to search for the location where the photo was taken."
    },
    {
        "name": "Question",
        "thought": "The last tool used is GoogleSearch, which informed us that the photo was taken in London. Based on this result, we can formulate a question about the location where the photo was taken. To ensure the answer requires viewing the image, we should avoid directly mentioning the name of the city.",
        "ori_question": "Where was Regency Cafe? Just tell me the city.",
        "question": "Where was this photo taken? Just tell me the city.",
        "rethink": "The original question directly mentioned the name of the café, which is visible in the image. To ensure the answer must refer to the image, the question should be adjusted to remove the specific name of the café.",
        "answer": "London"
    }
]