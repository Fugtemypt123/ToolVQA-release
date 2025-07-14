# 8. [Caption, Detection, DrawBox]
# Q: Circle the primary consumers in the image.
# A: image/output.png


MONT_EXAMPLES_8 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "Now we know the image depicts a marine food web, illustrating the relationships between various marine organisms. We can use the TextToBbox tool to locate one of the marine organisms.",
        "input": {
            "image": 'image/input.png'
        },
        "output": "The image depicts a marine food web, illustrating the relationships between various marine organisms. Key species represented include an orca, a sea otter, a kelp bass, a black rockfish, plainfin midshipman, and benthic organisms like a bat star, sea cucumber, and sea urchin. It also includes primary producers like phytoplankton and kelp, as well as primary consumers like zooplankton. Arrows indicate the direction of energy flow and predation among these organisms.",
        "thought": "To answer the question, we first need to use the ImageDescription tool to identify the information of the animals in the image."
    },
    {
        "name": "TextToBbox",
        "thought_query": "The picture shows many marine organisms, and the most unique one is the primary consumers like zooplankton. This is because there is only one organism in this category. So we can try to get its location.",
        "thought_choose": "Now we know the location of the primary consumers like zooplankton. We can use the DrawBox tool to circle the primary consumers in the image.",
        "input": {
            "image": 'image/input.png',
            "text": 'zooplankton'
        },
        "output": "(2, 61, 358, 230), score 71\n",
        "thought": "Now we know the primary consumers like zooplankton are in the image. I will use the 'TextToBbox' tool to locate the zooplankton in the image."
    },
    {
        "name": "DrawBox",
        "thought_query": "Now that we know the location of the zooplankton, we can use the DrawBox tool to circle it in the image.",
        "thought_choose": "Now that we have circled the zooplankton in the image, we can formulate a question based on this information, allowing us to conclude the tool call process.",
        "input": {
            "image": 'image/input.png',
            "bbox": "(2, 61, 358, 230)"
        },
        "output": "image/output.png",
        "thought": "Now that we have located the primary consumers like zooplankton in the image, the next step is to circle them using the 'DrawBox' tool."
    },
    {
        "name": "Question",
        "thought": "The last tool used is DrawBox, which circled the primary consumers like zooplankton in the image. Based on this result, we can formulate a question about the primary consumers in the image. To ensure the answer requires viewing the image, we should avoid directly mentioning the name 'zooplankton' and instead refer to the primary consumers.",
        "ori_question": "Circle the zooplankton in the image, which is located at (2, 61, 358, 230).",
        "question": "Circle the primary consumers in the image.",
        "rethink": "The original question directly mentioned the name and the location of the primary consumers, which is visible in the image. To ensure the answer must refer to the image, the question should be adjusted to remove the specific name and location of the primary consumers.",
        "answer": "image/output.png"
    }
]