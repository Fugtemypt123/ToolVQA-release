# 2. [Caption, Detection, RAD, Search]
# Q: What should you consider first when raising the dog in the middle of the image?
# A: Regular exercise


MONT_EXAMPLES_2 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "The image contains 5 dogs of different breeds, but we currently do not know the breed of each dog. This may require using the TextToBbox tool to obtain the coordinates of the dogs in the image and further gather fine-grained information.",
        "input": {
            "image": 'image/input.png'
        },
        "output": "The image shows five dogs of different breeds and sizes sitting in a row against a white background. The dogs are a mix of small to large breeds, ranging from a beagle on the left to a larger, dark-colored dog on the right. They are all facing forward with some having their tongues out.",
        "thought": "To solve this problem, we first need to use the ImageDescription tool to gather information about the dogs in the image."
    },  
    {
        "name": "TextToBbox",
        "thought_query": "The most prominent objects in the image are dogs. The image description tells us that there are five different breeds of dogs present.",
        "thought_choose": "After obtaining the coordinates of the dogs, we can use the RegionAttributeDescription tool to describe the fine-grained information about a specific dog.",
        "input": {
            "image": 'image/input.png',
            "text": 'dog'
        },
        "output": "(762, 75, 936, 532), score 74\n(595, 89, 763, 518), score 73\n(423, 140, 608, 520), score 72\n(82, 265, 253, 510), score 72\n(272, 220, 424, 508), score 68",
        "thought": "Now we know there are 5 dogs in the image. To locate the dog in the middle, I should detect all the dogs, and find the middle bounding box according to the bbox coordinates."
    },
    {
        "name": "RegionAttributeDescription",
        "thought_query": "Now that we know there are 5 dogs of different breeds in the image, one detail worth observing is the breed of one specific dog. Based on the available information, let's focus on the dog in the middle, located at (423, 140, 608, 520), and determine its breed.",
        "thought_choose": "Once we determine the breed of the dog in the middle, we can use the GoogleSearch tool to look up more information related to that breed.",
        "input": {
            "image": 'image/input.png',
            "bbox": "(423, 140, 608, 520)",
            "attribute": "breed"
        },
        "output": "Golden Retriever",
        "thought": "The middle bounding box is (423, 140, 608, 520). I will describe this region to see what the breed of dog it is."
    },
    {
        "name": "GoogleSearch",
        "thought_query": "Now that we know the breed of the middle dog is a Golden Retriever, we can search for factual information about this breed, such as the year it originated.",
        "thought_choose": "Now that we have gathered the important considerations for raising a Golden Retriever, we can formulate a complete question based on this information, allowing us to conclude the tool call process.",
        "input": {
            "query": "In which year did the Golden Retriever breed originate?"
        },
        "output": """1 - Answer box: The golden retriever breed originated in 1868 when Lord Tweedmouth mated a yellow Wavy-Coated retriever named “Nous” with a Tweed Water spaniel named “Belle.” Guisachan was the home of Dudley Coutts Majoribanks, the first Baron Tweedmouth, from 1854 to 1894. It was here he famously bred the first golden retriever.""",
        "thought": "Now that we know the breed of the middle dog is a Golden Retriever, the next step is to use a search engine to find out the year it originated."
    },
    {
        "name": "Question",
        "thought": "The final tool used is GoogleSearch, which informed us that the Golden Retriever originated in 1868. Based on this result, we can formulate a question about the origin year of the dog breed. To ensure the answer requires viewing the image, we should avoid directly mentioning the breed name 'Golden Retriever,' instead referring to the position of this breed's dog in the image. Additionally, we need to summarize the information returned by the last tool as a single number to keep the answer concise.",
        "ori_question": "In which year did the Golden Retriever breed originate?",
        "question": "In which year did the dog breed in the middle of the image originate?",
        "rethink": "The original question directly mentioned the breed of the dog, which is visible in the image. To ensure the answer must refer to the image, the question should be adjusted to implicitly reference the breed of the dog.",
        "answer": "Regular exercise and activity"
    }
]