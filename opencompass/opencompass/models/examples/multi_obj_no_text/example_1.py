# 1. [Caption, Count, Count, Calculator]
# Q: What is the percentage of adults?
# A: 50


MONT_EXAMPLES_1 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "The image mentions a family walking by the seaside. Although the description mentions the number of people, this information can still be further confirmed using tools. So we can first use the CountGivenObject tool to determine the total number of people, as well as the number of adults.",
        "input": {
            "image": 'image/input.png'
        },
        "output": "A family of four is walking on the beach at sunset. The two adults are holding hands with the children, enjoying a peaceful moment together near the ocean. The sunlight creates a warm and serene atmosphere. They are dressed in casual, comfortable clothing.",
        "thought": "To calculate the percentage of adults, we first need to use the ImageDescription tool to identify the people in the image."
    },
    {
        "name": "CountGivenObject",
        "thought_query": "The most obvious countable object in the picture are people.",
        "thought_choose": "We have already counted the quantity of people in the image. Among these people there are both adults and children, so we can continue to use CountGivenObject to obtain the quantities of adults.",
        "input": {
            "image": 'image/input.png',
            "text": 'people'
        },
        "output": "4",
        "thought": "Now we know that the picture depicts a family at the beach, but we don't know the number of people. To calculate the proportion of adults, we should first use the CountGivenObject tool to count the total number of people, then use CountGivenObject to count the number of adults, and finally use the Calculator tool to calculate the proportion."
    },
    {
        "name": "CountGivenObject",
        "thought_query": "Among these people there are both adults and children, so we can continue to use CountGivenObject to obtain the quantities of adults.",
        "thought_choose": "We have already counted the quantities of people and adults. We can now use the Calculator tool to calculate the percentage of adults.",
        "input": {
            "image": 'image/input.png',
            "text": 'adults'
        },
        "output": "2",
        "thought": "Now that I know there are 4 people in the image, the next step is to count the number of adults."
    },
    {
        "name": "Calculator",
        "thought_query": "Now that we know there are 4 people in the image, and 2 of them are adults, we can calculate the percentage of adults by dividing the number of adults by the total number of people and multiplying by 100. The formula for calculating the percentage of adults is: (Number of adults / Total number of people) * 100 = (2 / 4) * 100.",
        "thought_choose": "Now that we have calculated the percentage of adults, we can formulate a complete question based on this information, allowing us to conclude the tool call process.",
        "input": {
            "expression": "2 / 4 * 100"
        },
        "output": "50",
        "thought": "Now that we have counted the number of adults and the total number of people in the image, we can calculate the percentage of adults by dividing the number of adults by the total number of people and multiplying by 100."
    },
    {
        "name": "Question",
        "thought": "The last tool used is Calculator, which determined the percentage of adults in the image. Based on this result, we can formulate a question regarding the percentage of adults. To ensure the question requires viewing the image for an answer, we will NOT mention the total number of people or adults.",
        "ori_question": "What is the percentage of adults? There are 2 adults and the total number is 4.",
        "question": "What is the percentage of adults?",
        "rethink": "The original question directly included the number of adults and the total number of people. We should adjust the question to remove these details to make the questions have to be answered by looking at the picture.", 
        "answer": "50"
    }
]