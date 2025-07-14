# 5. [Caption, AddText]
# Q: Generate a title for the image and put it in the middle of the image.
# A: image/output.png


SONT_EXAMPLES_5 = [
    {
        "name": "ImageDescription",
        "thought_query": "Since we don't know the information in the picture, we first call tool ImageDescription to describe the picture.",
        "thought_choose": "The image displays serene pond water, dotted with green lily pads and adorned with vibrant pink water lilies in full bloom. We can use ImageStylization to convert the image to other art style.",
        "input": {
            "image": 'image/input.png'
        },
        "output": "The image displays serene pond water, dotted with green lily pads and adorned with vibrant pink water lilies in full bloom. Some of the plants have been labeled with tags attached to stakes, standing upright among the floating leaves and flowers. The clear water reflects the surrounding foliage, adding depth and tranquility to the scene.",
        "thought": "To generate a title, I will first describe the photo."
    },
    {
        "name": "AddText",
        "thought_query": "Now that we know that the image displays serene pond water, dotted with green lily pads and adorned with vibrant pink water lilies in full bloom. We can use AddText to generate a title and put it in the middle of the image. Let's generate a title for the image: water lily.",
        "thought_choose": "Now that we have added a title on the generated image, we can conclude the tool call process.",
        "input": {
            'image': 'image/output.png',
            "text": "water lily",
            "position": "mm"
        },
        "output": "image/output.png",
        "thought": "According to the image description, the image depicts some flowers floating on the water, which is likely water lily. I will add the poem on the middle of the image using AddText tool."
    },
    {
        "name": "Question",
        "thought": "The last tool used is AddText, which added a title to the middle of the generated image. Based on this result, we can formulate a question to generate an image. To ensure the question requires viewing the image for an answer, we should avoid mentioning the title and instead refer to it indirectly.",
        "ori_question": "Generate a title 'water lily' and put it in the middle of the image.",
        "question": "Generate a title and put it in the middle of the image.",
        "rethink": "The original question directly mentioned the title of the image, which can be inferred from the image information. To ensure the answer must refer to the image, the question should be adjusted to implicitly reference the title",
        "answer": "water lily (image/output.png)"
    }
]