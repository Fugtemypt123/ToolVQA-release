# 5. [Caption, OCR, Search, Search]
# Q: In which year was the city that taken this photo built?
# A: 47 AD
# image: /network_space/server126/shared/yinshaofeng/ToolLLM/GTA/agentlego/gta_dataset/image/image_26.jpg


OT_EXAMPLES_5 = [
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
        "thought_choose": "Now we know the café is located at 17-19 Regency St, London SW1P 4BY, UK. We can further search for the information about the city London.",
        "input": {
            "query": "Regency Cafe location"
        },
        "output": """1 - Answer box: 17-19 Regency St, London SW1P 4BY, UK""",
        "thought": "Now we know the image depicts the exterior of a café named 'Regency Cafe.' We can use the GoogleSearch tool to search for the location where the photo was taken."
    },
    {
        "name": "GoogleSearch",
        "thought_query": "Now we know the café is located at 17-19 Regency St, London SW1P 4BY, UK. We can further search for the more different facts rather than the 'Regency Cafe location'. Let's search the information about the city London, such as the year it was built.",
        "thought_choose": "Now we have the search result, we can propose a question based on this information, allowing us to conclude the tool call process.",
        "input": {
            "query": "When was London built?"
        },
        "output": """1 - Answer box: 47 AD""",
        "thought": "Now we know the Regency Cafe is located in London. We can use the GoogleSearch tool to search for the year the city was built."
    },
    {
        "name": "Question",
        "thought": "The last tool used is GoogleSearch, which informed us that the city of London was built in 47 AD. Based on this result, we can formulate a question about the city where the photo was taken. To ensure the answer requires viewing the image, we should avoid directly mentioning the name of the city.",
        "ori_question": "In which year was London built?",
        "question": "In which year was the city that taken this photo built?",
        "rethink": "The original question directly mentioned the name of the city, which can be inferred from the image. To ensure the answer must refer to the image, the question should be adjusted to remove the specific name of the city.",
        "answer": "47 AD"
    }
]