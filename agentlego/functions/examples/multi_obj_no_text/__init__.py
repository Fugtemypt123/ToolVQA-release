# use for loop to simplify the code
import os
import re

files = os.listdir(os.path.dirname(__file__))
MONT_EXAMPLES = []

for file in files:
    if file == '__init__.py' or file[-3:] != '.py':
        continue
    number = re.search(r'\d+', file).group()
    exec(f'from functions.examples.multi_obj_no_text.{file[:-3]} import MONT_EXAMPLES_{number}')
    MONT_EXAMPLES.append(eval(f'MONT_EXAMPLES_{number}'))

# from .example_0 import MONT_EXAMPLES_0
# from .example_1 import MONT_EXAMPLES_1
# from .example_2 import MONT_EXAMPLES_2
# from .example_3 import MONT_EXAMPLES_3
# from .example_4 import MONT_EXAMPLES_4
# from .example_5 import MONT_EXAMPLES_5
# from .example_6 import MONT_EXAMPLES_6
# from .example_7 import MONT_EXAMPLES_7
# from .example_8 import MONT_EXAMPLES_8
# from .example_9 import MONT_EXAMPLES_9

# MONT_EXAMPLES = [MONT_EXAMPLES_0, MONT_EXAMPLES_1, MONT_EXAMPLES_2, MONT_EXAMPLES_3, MONT_EXAMPLES_4, MONT_EXAMPLES_5, MONT_EXAMPLES_6, MONT_EXAMPLES_7, MONT_EXAMPLES_8, MONT_EXAMPLES_9]
