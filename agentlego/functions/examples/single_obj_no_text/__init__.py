# use for loop to simplify the code
import os
import re

files = os.listdir(os.path.dirname(__file__))
SONT_EXAMPLES = []

for file in files:
    if file == '__init__.py' or file[-3:] != '.py':
        continue
    number = re.search(r'\d+', file).group()
    exec(f'from functions.examples.single_obj_no_text.{file[:-3]} import SONT_EXAMPLES_{number}')
    SONT_EXAMPLES.append(eval(f'SONT_EXAMPLES_{number}'))

# from .example_0 import SONT_EXAMPLES_0
# from .example_1 import SONT_EXAMPLES_1
# from .example_2 import SONT_EXAMPLES_2
# from .example_3 import SONT_EXAMPLES_3
# from .example_4 import SONT_EXAMPLES_4
# from .example_5 import SONT_EXAMPLES_5
# from .example_6 import SONT_EXAMPLES_6
# from .example_7 import SONT_EXAMPLES_7
# from .example_8 import SONT_EXAMPLES_8
# from .example_9 import SONT_EXAMPLES_9
# from .example_10 import SONT_EXAMPLES_10
# from .example_11 import SONT_EXAMPLES_11

# SONT_EXAMPLES = [SONT_EXAMPLES_0, SONT_EXAMPLES_1, SONT_EXAMPLES_2, SONT_EXAMPLES_3, SONT_EXAMPLES_4, SONT_EXAMPLES_5, SONT_EXAMPLES_6, SONT_EXAMPLES_7, SONT_EXAMPLES_8, SONT_EXAMPLES_9]
