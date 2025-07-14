# 2. [OCR, Calculator]
# Q: How much more are the cumulative incidents with government care than the cumulative incidents with non-government care?
# A: 29


NOT_EXAMPLES_2 = [
    {
        "name": "OCR",
        "thought_query": "Since we don't know the information in the picture, we first call tool OCR to describe the picture.",
        "thought_choose": "Now we know the image contains a table that lists the level of care, provider, and cumulative events. We can use the Calculator tool to formulate some calculations based on the data in the table.",
        "input": {
            "image": 'image/input.png'
        },
        "output": """The text and numbers in the image are as follows:

| Level of Care    | Provider                      | Cumulative Events |
|------------------|-------------------------------|-------------------|
|                  |                               | No.    | %         |
| Government       | VHW*                          | 5      | 0.8%      |
|                  | Dispensary                    | 92     | 14.5%     |
|                  | Health Centre                 | 104    | 16.4%     |
|                  | Hospital                      | 67     | 10.6%     |
| Home             | Mothers                       | 19     | 3.0%      |
|                  | Family                        | 64     | 10.1%     |
| Non-Government   | Drug Shops                    | 36     | 5.7%      |
|                  | Dispensary                    | 77     | 12.2%     |
|                  | Health Centre                 | 39     | 6.2%      |
|                  | Hospital                      | 30     | 4.7%      |
|                  | TM** at Practitioner          | 30     | 11.5%     |
|                  | TM** at Home                  | 27     | 4.3%      |
|                  | Total care seeking            | 633    | 100.0%    |

*VHW: Village Health Worker
**TM: Traditional Medicine
""",
        "thought": "To calculate the difference between the cumulative incidents with government care and non-government care, I will first use the OCR tool to extract the relevant data from the image."
    },
    {
        "name": "Calculator",
        "thought_query": "Now that we know the image contains a table that lists the level of care, provider, and cumulative events, we can use the Calculator tool to perform some calculations based on the data in the table. Let's calculate the difference between the cumulative incidents with government care and non-government care.",
        "thought_choose": "Now that we have calculated the difference between the cumulative incidents with government care and non-government care, we can conclude the tool call process.",
        "input": {
            "expression": "5 + 92 + 104 + 67 - 36 - 77 - 39 - 30 - 30 - 27",
        },
        "output": "29",
        "thought": "Now I will calculate the difference between the cumulative incidents with government care and non-government care using the Calculator tool."
    },
    {
        "name": "Question",
        "thought": "The last tool used is Calculator, which calculated the difference between the cumulative incidents with government care and non-government care. Based on this result, we can formulate a question to generate an image. To ensure the question requires viewing the image for an answer, we should avoid mentioning the specific data values and instead refer to them indirectly.",
        "ori_question": "How much more are the 268 cumulative incidents with government care than the 239 cumulative incidents with non-government care?",
        "question": "How much more are the cumulative incidents with government care than the cumulative incidents with non-government care?",
        "rethink": "The original question directly mentioned the cumulative incidents with government care and non-government care, which can be inferred from the image information. To ensure the answer must refer to the image, the question should be adjusted to remove the number of cumulative incidents.", 
        "answer": "29"
    }
]