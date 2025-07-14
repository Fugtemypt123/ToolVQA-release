from .calculator import CALCULATOR_PROMPT
from .googlesearch import GOOGLESEARCH_PROMPT
from .plot import PLOT_PROMPT
from .solver import SOLVER_PROMPT
from .ocr import OCR_PROMPT
from .imagedescription import IMAGEDESCRIPTION_PROMPT
from .texttobbox import TEXTTOBBOX_PROMPT
from .countgivenobject import COUNTGIVENOBJECT_PROMPT
from .mathocr import MATHOCR_PROMPT
from .drawbox import DRAWBOX_PROMPT
from .addtext import ADDTEXT_PROMPT
from .texttoimage import TEXTTOIMAGE_PROMPT
from .imagestylization import IMAGESTYLIZATION_PROMPT
from .regionattributedescription import REGIONATTRIBUTEDESCRIPTION_PROMPT
from .question import QUESTION_PROMPT
from .rethink import RETHINK_QUESTION_PROMPT
from .thought import THOUGHT_PROMPT
from .nextstep import NEXTSTEP_PROMPT

prompt_map = {
    'Calculator': CALCULATOR_PROMPT,
    'GoogleSearch': GOOGLESEARCH_PROMPT,
    'Plot': PLOT_PROMPT,
    'Solver': SOLVER_PROMPT,
    'OCR': OCR_PROMPT,
    'ImageDescription': IMAGEDESCRIPTION_PROMPT,
    'TextToBbox': TEXTTOBBOX_PROMPT,
    'CountGivenObject': COUNTGIVENOBJECT_PROMPT,
    'MathOCR': MATHOCR_PROMPT,
    'DrawBox': DRAWBOX_PROMPT,
    'AddText': ADDTEXT_PROMPT,
    'TextToImage': TEXTTOIMAGE_PROMPT,
    'ImageStylization': IMAGESTYLIZATION_PROMPT,
    'RegionAttributeDescription': REGIONATTRIBUTEDESCRIPTION_PROMPT,
    'Question': QUESTION_PROMPT,
    'RethinkQuestion': RETHINK_QUESTION_PROMPT,
    'Thought': THOUGHT_PROMPT,
    'NextStep': NEXTSTEP_PROMPT,
}