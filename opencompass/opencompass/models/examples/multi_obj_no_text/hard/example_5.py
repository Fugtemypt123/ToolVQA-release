# 5. [Caption, Detection, RAD]
# Q: What is the man sitting in the front holding in his hand in the picture?
# A: guitar


MONT_EXAMPLES_5 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "The picture shows four people holding musical instruments, but there is no specific correspondence between the people and the instruments. This is information worth exploring. We can use the TextToBbox tool to determine the coordinates of some person, and then further explore the information of the instrument he is holding.",
        "input": {
            "image": 'image/input.png'
        },
        "output": "The image depicts four individuals sitting in a setting resembling a train compartment or a bus. Each person is holding a different musical instrument: a double bass, a banjo, a guitar, and a violin. The seats have intricate, leafy green patterns, and the window has drawn curtains. The overall style of the image appears to be a detailed drawing or illustration.",
        "thought": "To solve this problem, we first need to use the ImageDescription tool to gather information about the people and musical instruments in the image."
    },  
    {
        "name": "TextToBbox",
        "thought_query": "The most prominent object in the image is a person. The image description indicates that there are four people, each holding a different musical instrument. Let's choose the person in the front.",
        "thought_choose": "Now that we have located the person in the front, we can use the RegionAttributeDescription tool to describe the musical instrument he is holding.",
        "input": {
            "image": 'image/input.png',
            "text": 'man sitting in the front'
        },
        "output": """(353, 253, 1047, 924), score 70""",
        "thought": "To identify what the man sitting in the front is holding in his hand in the picture, I need to first locate the man and then describe the object he is holding. I will use the TextToBbox tool to locate the man sitting in the front and then use the RegionAttributeDescription tool to describe the object he is holding.\n" 
    },
    {
        "name": "RegionAttributeDescription",
        "thought_query": "Now that we know the location of the man sitting in the front is (353, 253, 1047, 924), we can further describe the object he is holding.",
        "thought_choose": "Once we determine the man in the front is holding a guitar, we can use the GoogleSearch tool to look up more information related to the guitar.",
        "input": {
            "image": 'image/input.png',
            "bbox": "(353, 253, 1047, 924)",
            "attribute": "what is held in the hand"
        },
        "output": "A person in a suit is holding an acoustic guitar.",
        "thought": "The location of the man sitting in the front is (353, 253, 1047, 924). I will describe this region to see what is held in his hand."
    },
    {
        "name": "Question",
        "thought": "The final tool used is RegionAttributeDescription, which tells us the man in the front is holding a guitar in the image. Based on this result, we can formulate a question about what he is holding in his hand. In order to make the question answerable only by looking at the picture, we cannot mention any information about the guitar in the question, but only the position of the person holding the guitar.",
        "ori_question": "What is the man with the guitar holding in his hand in the picture?",
        "question": "What is the man sitting in the front holding in his hand in the picture?",
        "rethink": "The original question directly mentioned the object 'guitar.' To ensure the answer must refer to the image, the question should be adjusted to implicitly reference the object held by the person in the front.",
        "answer": "guitar"
    }
]