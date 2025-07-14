# 0. [Caption, Search, Calculator]
# Q: How many kilograms of food should be prepared for this adult animal at least per week?
# A: 84


SONT_EXAMPLES_0 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "The image shows a giant panda sitting outdoors. We can use the GoogleSearch tool to find more information about pandas.",
        "input": {
            "image": 'image/input.png'
        },
        "output": """The image shows a giant panda sitting outdoors, holding and eating bamboo. The panda has its characteristic black-and-white fur pattern, with black patches around its eyes, ears, and limbs. It appears relaxed while chewing on the bamboo, surrounded by green foliage in a natural setting.""",
        "thought": "To provide an accurate answer, I need to know what type of animal is in the image and its dietary requirements. I will use the ImageDescription tool to identify the animal in the provided image."
    },
    {
        "name": "GoogleSearch",
        "thought_query": "Now that we know the animal in the picture is a panda, we can search for some factual information about pandas, such as the weight of food they consume each day.",
        "thought_choose": "Now we have found the information about the daily food intake of a panda, we can then use Calculator to formulate an expression about its food intake in several days.",
        "input": {
            "query": "panda's daily food intake in kilograms"
        },
        "output": """1 - Answer box: A panda's daily diet consists almost entirely of the leaves, stems and shoots of various bamboo species. Bamboo contains very little nutritional value so pandas must eat 12-38kg every day to meet their energy needs.""",
        "thought": """This is a panda. I can search its daily food intake in kilograms."""
    },
    {
        "name": "Calculator",
        "thought_query": "Now that we know a panda eats about 12-38 kilograms of bamboo per day, we can calculate the minimum amount of food needed per week by multiplying the lower end of the daily intake (12 kg) by 7 days.",
        "thought_choose": "Now that we have calculated the minimum amount of food needed per week, we can formulate a question based on this information, allowing us to conclude the tool call process.",
        "input": {
            "expression": "12 * 7"
        },
        "output": "84",
        "thought": """An adult panda eats about 12-38 kilograms of bamboo per day. To calculate the minimum amount of food (bamboo) needed per week, I'll use the lower end of the daily intake (12 kg) and multiply it by 7 days."""
    },
    {
        "name": "Question",
        "thought": "The last tool used is Calculator, which determined the minimum amount of food needed per week for an adult panda. Based on this result, we can formulate a question about the food intake of this animal. To ensure the question requires viewing the image for an answer, we should avoid mentioning the specific name of 'panda' and instead refer to it as 'this adult animal.'",
        "ori_question": "How many kilograms of food should be prepared for panda at least per week?",
        "question": "How many kilograms of food should be prepared for this adult animal at least per week?",
        "rethink": "The original question directly mentioned the animal name 'panda,' which is visible in the image. To ensure the answer must refer to the image, the question should be adjusted to implicitly reference the animal in the image.",
        "answer": "84"
    }
]