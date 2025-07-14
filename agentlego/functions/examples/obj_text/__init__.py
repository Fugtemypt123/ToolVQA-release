# use for loop to simplify the code
import os
import re

files = os.listdir(os.path.dirname(__file__))
OT_EXAMPLES = []

for file in files:
    if file == '__init__.py' or file[-3:] != '.py':
        continue
    number = re.search(r'\d+', file).group()
    exec(f'from functions.examples.obj_text.{file[:-3]} import OT_EXAMPLES_{number}')
    OT_EXAMPLES.append(eval(f'OT_EXAMPLES_{number}'))

# from .example_0 import NOT_EXAMPLES_0
# from .example_1 import NOT_EXAMPLES_1
# from .example_2 import NOT_EXAMPLES_2
# from .example_3 import NOT_EXAMPLES_3

# NOT_EXAMPLES = [NOT_EXAMPLES_0, NOT_EXAMPLES_1, NOT_EXAMPLES_2, NOT_EXAMPLES_3]
