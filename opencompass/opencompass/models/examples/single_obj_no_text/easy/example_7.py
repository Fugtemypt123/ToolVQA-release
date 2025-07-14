# 7. [Caption, Search]
# Q: When was this dish invented?
# A: in the late 1800s


SONT_EXAMPLES_7 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "Now that we know the image shows a meal consisting of Mapo Tofu, a traditional Sichuan dish, we can use the GoogleSearch tool to find more information about the dish.",
        "input": {
            "image": 'image/input.png'
        },
        "output": "The image shows a meal consisting of a bowl of Mapo Tofu, a traditional Sichuan dish featuring tofu cubes in a spicy red sauce with minced meat and garnished with chopped green onions. There is a bowl of white rice and a pair of wooden chopsticks next to it on a light-colored surface.",
        "thought": "To find the specific amount of pork mince required for a dish according to BBC Good Food, I will use the ImageDescription tool to understand what the dish is from the provided image. Then, I can use the GoogleSearch tool to find the recipe on BBC Good Food and determine the required amount of pork mince."
    },
    {
        "name": "GoogleSearch",
        "thought_query": "Now that we know the image shows a meal consisting of Mapo Tofu, a traditional Sichuan dish. We can search for some factual information about the dish, such as the time of its invention.",
        "thought_choose": "Now that we have found the recipe for Mapo Tofu on BBC Good Food, we can conclude the tool call process.",
        "input": {
            "query": "When was Mapo Tofu invented?"
        },
        "output": """1 - Answer box: Mapo tofu is said to have originated in Chengdu in the late 1800s. Ma translates to “pockmarks”, while po refers to an older woman. Together these reference the dish's inventor, Mrs Chen, an elderly woman with smallpox scars.""",
        "thought": "Now that we know the image shows a meal consisting of Mapo Tofu, the next step is to search for the date when the dish was invented. This information will provide additional context about the dish and its history."
    },
    {
        "name": "Question",
        "thought": "The last tool used is GoogleSearch, which tells us that Mapo Tofu was invented in the late 1800s. Now, I will ask a question based on this information.",
        "ori_question": "When was this dish invented?",
        "question": "When was this dish invented?",
        "rethink": None,
        "answer": "in the late 1800s"
    }
]