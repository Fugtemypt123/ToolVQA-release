# 7. [Caption, Search]
# Q: I want to make this dish. How many grams of tofu do I need according to BBC Good Food?
# A: 450


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
        "thought_query": "Now that we know the image shows a meal consisting of Mapo Tofu, a traditional Sichuan dish. We can search for some factual information about the dish, such as the weight of the ingredients it requires. To make the answer unique, we searched for the weight of tofu it requires on BBC Good Food.",
        "thought_choose": "Now that we have found the recipe for Mapo Tofu on BBC Good Food, we can conclude the tool call process.",
        "input": {
            "query": "BBC Good Food Mapo Tofu recipe"
        },
        "output": """1 - Mapo tofu recipe - BBC Good Food: Ingredients · 450g tofu · 3 tbsp groundnut oil · 100g pork mince · 2 tbsp Sichuan chilli bean paste · 1½ tbsp fermented black beans, rinsed (optional, available from ...""",
        "thought": "Now that we know the image shows a meal consisting of Mapo Tofu, the next step is to search for the recipe on BBC Good Food to find the required amount of tofu."
    },
    {
        "name": "Question",
        "thought": "The last tool used is GoogleSearch, which tells us that the BBC Good Food Mapo Tofu recipe requires 450g of tofu. Based on this result, we can formulate a question about the dish in the picture. To ensure the question requires viewing the image for an answer, we should avoid mentioning the specific name 'Mapo Tofu' of the dish and instead refer to it indirectly by 'the dish in the picture'.",
        "ori_question": "I want to make Mapo Tofu. How many grams of tofu do I need according to BBC Good Food?",
        "question": "I want to make this dish. How many grams of tofu do I need according to BBC Good Food?",
        "rethink": "The original question directly mentioned the name of the dish, which can be inferred from the image information. To ensure the answer must refer to the image, the question should be adjusted to remove the specific name of the dish.",
        "answer": "450"
    }
]