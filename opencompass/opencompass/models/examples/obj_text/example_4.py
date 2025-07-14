# 4. [Caption, OCR, Search, Search]
# Q: Who is the main character of the book published by this author in 2018?
# A: Hem and Haw


OT_EXAMPLES_4 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "Now we know the image is the cover of the book titled 'Who Moved My Cheese?' by Dr. Spencer Johnson. We can use the OCR tool to extract more information from the image.",
        "input": {
            "image": 'image/input.png'
        },
        "output": """The image is the cover of the book titled "Who Moved My Cheese?" by Dr. Spencer Johnson. The subtitle reads, "An Amazing Way to Deal With Change In Your Work and In Your Life." The cover prominently features the book's title in large red letters, with an illustration of a piece of cheese integrated into the word "Moved." The author's name is also displayed, along with a note about the foreword by Kenneth Blanchard Ph.D. and a mention of the book being a best-seller.""",
        "thought": "To answer the question, we first need to use the ImageDescription tool to identify the information of the book in the image."
    },
    {
        "name": "OCR",
        "thought_query": "Now we know the image is the cover of the book titled 'Who Moved My Cheese?' by Dr. Spencer Johnson. We can use the OCR tool to extract more information from the image.",
        "thought_choose": "Now we have known the book author is Dr. Spencer Johnson, we can use the GoogleSearch tool to find the book published by the author in 2018.",
        "input": {
            "image": 'image/input.png'
        },
        "output": """(18, 11, 316, 28) One of the most successtul business books ever
(120, 28, 215, 48) Daily Telegraph
(83, 47, 255, 139) Who
(110, 132, 226, 151) An Amezing Woy to
(38, 146, 298, 235) Moeed
(100, 229, 159, 246) Deol With
(116, 239, 230, 333) My
(176, 231, 221, 247) Change
(71, 327, 192, 341) In Your Work and in
(190, 327, 255, 342) Your Life
(29, 327, 307, 423) Cheese?
(24, 327, 308, 455) DR SPENCER IOHNSON
(34, 327, 298, 476) Foreword by KENNETH BLANCHARD PH.D
(65, 327, 270, 498) From the best-selling author of
(90, 327, 247, 515) The One Minude Manager""",
        "thought": "Now we know the image is the cover of the book titled 'Who Moved My Cheese?' by Dr. Spencer Johnson. We can use the OCR tool to extract more information from the image."
    },
    {
        "name": "GoogleSearch",
        "thought_query": "Now we know the book author is Dr. Spencer Johnson. We can use the GoogleSearch tool to search some facts about the author, such as the books published by the author in 2018.",
        "thought_choose": "Now we know the book published by Dr. Spencer Johnson in 2018 is 'Out of the Maze.' We can further search for the information about the book.",
        "input": {
            "query": "Spencer Johnson books published in 2018"
        },
        "output": """1 - Answer box: Johnson's last book, Out of the Maze, is a sequel to Who Moved My Cheese that references Johnson's struggle with cancer (which ultimately ended with his death in 2017) and was published posthumously in 2018.""",
        "thought": "To answer the question, we need to find the book published by Dr. Spencer Johnson in 2018. I will use the GoogleSearch tool to search for the information."
    },
    {
        "name": "GoogleSearch",
        "thought_query": "Now we know the book published by Dr. Spencer Johnson in 2018 is 'Out of the Maze.' We can use the GoogleSearch tool to search for more different facts about this book, rather than the 'Spencer Johnson books published in 2018'. Let's search the main character of the new book.",
        "thought_choose": "Now we have the search result, we can propose a question based on this information, allowing us to conclude the tool call process.",
        "input": {
            "query": "Who is the main character of 'Out of the Maze'?"
        },
        "output": """1 - Answer box: Our story begins with two miniature people named Hem and Haw, who live inside a maze. They spend their lives running through the maze together, looking for cheese to eat. One day, they discover a place called Cheese Station C, where there's a seemingly infinite supply of cheese.""",
        "thought": "Now we know the book published by Dr. Spencer Johnson in 2018 is 'Out of the Maze.' We can use the GoogleSearch tool to search for the main character of the book."
    },
    {
        "name": "Question",
        "thought": "The last tool used is GoogleSearch, which informed us that the main character of the book published by Dr. Spencer Johnson in 2018 is Hem and Haw. Based on this result, we can formulate a question about the book. To ensure the answer requires viewing the image, we should avoid directly mentioning the name of the book.",
        "ori_question": "Who is the main character of 'Out of the Maze'?",
        "question": "Who is the main character of the book published by this author in 2018?",
        "rethink": "The original question directly mentioned the name of the book, which can be inferred from the image. To ensure the answer must refer to the image, the question should be adjusted to remove the specific name of the book.",
        "answer": "Hem and Haw"
    }
]