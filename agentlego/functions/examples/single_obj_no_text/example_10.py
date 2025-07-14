# 6. [Caption, Search]
# Q: Who first discovered the bird in the picture?
# A: Carl Linnaeus


SONT_EXAMPLES_10 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "Now that we know the image shows a small bird, likely a Eurasian tree sparrow, perched on a mossy branch, we can use GoogleSearch to find more information about this bird.",
        "input": {
            "image": 'image/input.png'
        },
        "output": "The image shows a small bird, likely a Eurasian tree sparrow, perched on a mossy branch. The bird has a brown head, black facial markings, and brown and white feathers on its body and wings. The background is blurred, focusing attention on the sparrow, and the lighting suggests a natural outdoor environment with warm tones.",
        "thought": "To answer the question, I will first use the ImageDescription tool to identify the bird in the image."
    },
    {
        "name": "GoogleSearch",
        "thought_query": "Now that we know the image shows a Eurasian tree sparrow. We can search for some factual information about the bird, such as who first discovered it.",
        "thought_choose": "Now that we have found the information about the Eurasian tree sparrow, we can conclude the tool call process.",
        "input": {
            "query": "Who first discovered Eurasian tree sparrow?"
        },
        "output": """1 - Answer box: The Eurasian tree sparrow was first described by Carl Linnaeus in his 1758 Systema Naturae as Fringilla montana, but, along with the house sparrow, it was soon moved from the finches (family Fringillidae) into the new genus Passer created by French zoologist Mathurin Jacques Brisson in 1760.""",
        "thought": "Now that we know the image shows a Eurasian tree sparrow, the next step is to search for information about who first discovered this bird."
    },
    {
        "name": "Question",
        "thought": "The last tool used is GoogleSearch, which tells us that the Eurasian tree sparrow was first discovered by Carl Linnaeus. Based on this result, we can formulate a question about it. To ensure the question requires viewing the image for an answer, we should avoid mentioning the specific name 'Eurasian tree sparrow' of the bird and instead refer to it indirectly by 'the bird in the picture'.",
        "ori_question": "Who first discovered Eurasian tree sparrow?",
        "question": "Who first discovered the bird in the picture?",
        "rethink": "The original question directly mentioned the name of the bird, which can be inferred from the image information. To ensure the answer must refer to the image, the question should be adjusted to remove the specific name of the bird.",
        "answer": "Carl Linnaeus"
    }
]