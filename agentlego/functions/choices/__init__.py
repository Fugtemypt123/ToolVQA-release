from functions.examples import example_map

choice_map = {}

for key, value in example_map.items():
    choice_map[key] = {}
    for example in value:
        for i in range(len(example)):
            if i == 0:
                if 'Start' not in choice_map[key].keys():
                    choice_map[key]['Start'] = [example[i]['name']]
                elif example[i]['name'] not in choice_map[key]['Start']:
                    choice_map[key]['Start'].append(example[i]['name'])
            else:
                if example[i - 1]['name'] not in choice_map[key].keys():
                    choice_map[key][example[i - 1]['name']] = [example[i]['name']]
                elif example[i]['name'] not in choice_map[key][example[i - 1]['name']]:
                    choice_map[key][example[i - 1]['name']].append(example[i]['name'])
                    

description_map = {
    "Calculator": "A calculator tool. The input must be a single Python expression and you cannot import packages. You can use functions in the `math` package without import.",
    "OCR": "This tool can recognize all text on the input image.",
    "CountGivenObject": "The tool can count the number of a certain object in the image.",
    "ImageDescription": "A useful tool that returns a brief description of the input image.",
    "GoogleSearch": "The tool can search the input query text from Google and return the related results.",
    "RegionAttributeDescription": "Describe the attribute of a region of the input image.",
    "TextToBbox": "The tool can detect the object location according to description.",
    "Plot": "This tool can execute Python code to plot diagrams. The code should include a function named 'solution'. The function should return the matplotlib figure directly. Avoid printing the answer. The code instance format is as follows:\n\n```python\n# import packages\nimport matplotlib.pyplot as plt\ndef solution():\n    # labels and data\n    cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES']\n    data = [23, 17, 35, 29, 12, 41]\n\n    # draw diagrams\n    figure = plt.figure(figsize=(8, 6))\n    plt.pie(data, labels=cars, autopct='%1.1f%%', startangle=140)\n    plt.axis('equal')\n    plt.title('Car Distribution')\n    return figure\n```",
    "MathOCR": "This tool can recognize math expressions from an image and return the latex style expression.",
    "Solver": "This tool can execute Python code to solve math equations. The code should include a function named 'solution'. You should use the `sympy` library in your code to solve the equations. The function should return its answer in str format. Avoid printing the answer. The code instance format is as follows:\n\n```python\n# import packages\nfrom sympy import symbols, Eq, solve\ndef solution():\n    # Define symbols\n    x, y = symbols('x y')\n\n    # Define equations\n    equation1 = Eq(x**2 + y**2, 20)\n    equation2 = Eq(x**2 - 5*x*y + 6*y**2, 0)\n\n    # Solve the system of equations\n    solutions = solve((equation1, equation2), (x, y), dict=True)\n\n    # Return solutions as strings\n    return str(solutions)\n```",
    "DrawBox": "A tool to draw a box on a certain region of the input image.",
    "AddText": "A tool to add a text on a certain region of the input image.",
    "TextToImage": "This tool can generate an image according to the input text.",
    "ImageStylization": "This tool can modify the input image according to the input instruction. Here are some example instructions: \"turn him into cyborg\", \"add fireworks to the sky\", \"make his jacket out of leather\".",
    "Question": "End the process of tool calling and propose a question based on the context.",
}