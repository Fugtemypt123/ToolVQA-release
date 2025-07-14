# 3. [Caption, Search, Calculator]
# Q: How many animals in the image are endangered in 2024?
# A: 5


MONT_EXAMPLES_3 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "The image contains 12 different animals, the majority of which are wild. We can use the GoogleSearch tool to look up more information about these animals.",
        "input": {
            "image": 'image/input.png'
        },
        "output": "The image shows a collection of toy animal figurines arranged in rows. The animals depicted include a deer, lion, polar bear, bison, panda, hippopotamus, leopard, rhinoceros, bear, elephant, tiger, and antelope.",
        "thought": "To obtain the number of endangered animals in the image, we should first use the ImageDescription tool to identify the animals present, then use GoogleSearch to look up the types of endangered animals, and finally calculate the answer. Let's start by identifying the animals in the image."
    },  
    {
        "name": "GoogleSearch",
        "thought_query": "Now that we know there are 12 different animals in the image, most of which are wild, an important task for modern humans is to protect wildlife. Therefore, a worthwhile question to search for is which of these animals are endangered species.",
        "thought_choose": "We have identified the types of endangered animals for 2024, and the next step is to use the Calculator tool to specifically count the number of endangered animals in the image.",
        "input": {
            "query": "Endangered status of deer, lion, polar bear, bison, panda, hippopotamus, leopard, rhinoceros, bear, elephant, tiger, antelope in 2024"
        },
        "output": """1 - 10 of the World's Most Endangered Animals in 2024 - Earth.Org: Orangutans, rhinos, gorillas, turtles, and elephants are just some of the world's most endangered animals in 2024.(Missing: deer, lion, polar bear, bison, panda, hippopotamus, antelope)""",
        "thought": "Now we know there are 12 animals in the image, we can use GoogleSearch to confirm which of them are endangered species." 
    },
    {
        "name": "Calculator",
        "thought_query": "Now that we have the list of endangered animals for 2024, it contains a lot of extra information. We can see that the first search result shows 'Missing,' which includes 7 animals, and the total number of animals is 12. Therefore, we can use a calculator to find the number of endangered animals by calculating the difference between the total and the number of missing animals.",
        "thought_choose": "Now that we have counted the number of endangered animals in the image, we can formulate a challenging question based on this information, allowing us to conclude the tool call process.",
        "input": {
            "expression": "12 - 7"
        },
        "output": "5",
        "thought": "Now that we have the list of endangered animals for 2024, we can calculate the number of endangered animals in the image by subtracting the number of missing animals from the total number of animals."
    },
    {
        "name": "Question",
        "thought": "The last tool used is Calculator, which determined the number of endangered animals in the image. Based on this result, we can formulate a question about the number of endangered animals. To ensure that the question requires viewing the image for an answer, we should avoid mentioning the specific names of the animals and instead refer to them as 'the animals in the image.'",
        "ori_question": "How many species of deer, lion, polar bear, bison, panda, hippopotamus, leopard, rhinoceros, bear, elephant, tiger, and antelope are endangered in 2024?",
        "question": "How many species in the image are endangered in 2024?",
        "rethink": "The original question directly mentioned the names of the species in the image. To ensure the answer must refer to the image, the question should be adjusted to implicitly reference the species in the image.",
        "answer": "5"
    }
]