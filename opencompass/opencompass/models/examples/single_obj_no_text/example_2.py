# 2. [Caption, Search, TextToImage]
# Q: Find the cartoon with the animal in the picture as the protagonist, and generate an image of all the characters from this cartoon enjoying a meal together.
# A: image/output.png


SONT_EXAMPLES_2 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "The image contains a bear and a tiger, but there isn't much information to explore. We can use GoogleSearch to gather some external information.",
        "input": {
            "image": 'image/input.png'
        },
        "output": "The image shows a bear and a tiger in a grassy area. The tiger is lying on its side with a paw raised, while the bear is standing on all fours next to it. There is also a large rock in the background.",
        "thought": "To generate the image required by the question, we first need to use the ImageDescription tool to identify the animals in the image, then use a search engine to find animated films featuring them, and finally extract keywords for drawing to get the answer. Let's start by identifying the animals in the image."
    },
    {
        "name": "GoogleSearch",
        "thought_query": "Now that we know there is a tiger and a bear in the image, we can make some associations. For example, there are famous animated series featuring them as main characters, such as Winnie the Pooh and Tigger. A worthwhile question to search for is: what other characters are included in this animated series?",
        "thought_choose": "Now that we have gathered all the characters from the animated series, we can use this information to create an image of these characters having a meal together to show to children.",
        "input": {
            "query": "What characters are included in 'Winnie-the-Pooh'?"
        },
        "output": """1 - Answer box: Characters from the original books ___Winnie-the-Pooh. ___Christopher Robin. ___Tigger. ___Piglet. ___Eeyore. ___Rabbit. ___Kanga. ___Roo.""",
        "thought": "Now that we know there is a tiger and a bear in the image, the most famous animated series featuring them is 'Winnie-the-Pooh.' The next step is to search for the characters included in 'Winnie-the-Pooh'."
    },
    {
        "name": "TextToImage",
        "thought_query": "Now that we have gathered all the characters from 'Winnie-the-Pooh'. We can create an image of these characters enjoying a meal together.",
        "thought_choose": "Now that we have successfully generated an image, we can conclude the tool call process.",
        "input": {
            "keywords": "Winnie-the-Pooh, Tigger, enjoy meal",
        },
        "output": "image/output.png",
        "thought": "Now that we have gathered all the characters from 'Winnie-the-Pooh'. We can extract the names of all the characters and combine them with 'enjoy meal' as keywords to call the TextToImage tool to generate the final image."
    },
    {
        "name": "Question",
        "thought": "The last tool used is TextToImage, which generated an image of the characters from 'Winnie-the-Pooh' enjoying meal together. Based on this result, we can formulate a question to generate an image. To ensure the question requires viewing the image for an answer, we should avoid mentioning the name 'Winnie-the-Pooh' and instead refer to 'the animated series featuring the animals in the image', allowing the respondent to infer the name. Additionally, since the answer is an image, the question should include a phrase like 'generate an image' or something similar.",
        "ori_question": "Please generate an image of the main characters from 'Winnie-the-Pooh' enjoying a meal together.",
        "question": "Find the cartoon with the animal in the picture as the protagonist, and generate an image of the main characters from this cartoon enjoying a meal together.",
        "rethink": "The original question directly mentioned the name of the animated series, which can be inferred from the image information. To ensure the answer must refer to the image, the question should be adjusted to implicitly reference the name of the animation.",
        "answer": "image/output.png"
    }
]