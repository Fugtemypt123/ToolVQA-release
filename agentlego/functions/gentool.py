from typing import Any, List, Optional, Union
from agentlego.utils import load_or_build_object, require, parse_multi_float
from agentlego.tools import BaseTool
from agentlego.types import ImageIO, Annotated, Info
from mmengine.model import BaseModel
from PIL import Image
from openai import OpenAI
import base64
import re
from io import BytesIO
from paddleocr import PaddleOCR


class ImageStylization(BaseTool):
    """A tool to stylize an image.

    Args:
        model (str): The model name used to inference. Which can be found
            in the ``diffusers`` repository.
            Defaults to 'timbrooks/instruct-pix2pix'.
        inference_steps (int): The number of inference steps. Defaults to 20.
        device (str): The device to load the model. Defaults to 'cuda'.
        toolmeta (None | dict | ToolMeta): The additional info of the tool.
            Defaults to None.
    """

    default_desc = ('This tool can modify the input image according to the '
                    'input instruction. Here are some example instructions: '
                    '"turn him into cyborg", "add fireworks to the sky", '
                    '"make his jacket out of leather".')

    @require('diffusers')
    def __init__(self,
                 model: str = 'timbrooks/instruct-pix2pix',
                 inference_steps: int = 20,
                 device: str = 'cuda',
                 toolmeta=None):
        super().__init__(toolmeta=toolmeta)
        self.model_name = model
        self.inference_steps = inference_steps
        self.device = device

    def setup(self):
        pass

    def apply(self, image: ImageIO, instruction: str) -> ImageIO:
        return 'image/output.png'
    
    def __call__(self, *args: Any, **kwargs) -> Any:
        return 'image/output.png'

    
class TextToImage(BaseTool):
    """A tool to generate image according to some keywords.

    Args:
        model (str): The stable diffusion model to use. You can choose
            from "sd" and "sdxl". Defaults to "sd".
        device (str): The device to load the model. Defaults to 'cuda'.
        toolmeta (None | dict | ToolMeta): The additional info of the tool.
            Defaults to None.
    """

    default_desc = ('This tool can generate an image according to the '
                    'input text.')

    @require('diffusers')
    def __init__(
        self,
        model: str = 'sdxl',
        num_inference_steps: int = 30,
        device: str = 'cuda',
        toolmeta=None,
    ):
        super().__init__(toolmeta=toolmeta)
        assert model in ['sd', 'sdxl', 'sdxl-turbo']
        self.model = model
        self.device = device
        self.num_inference_steps = num_inference_steps

    def setup(self):
        pass
    
    def apply(
        self,
        keywords: Annotated[str,
                            Info('A series of keywords separated by comma.')],
    ) -> ImageIO:
        return 'image/output.png'

    def __call__(self, *args: Any, **kwargs) -> Any:
        return 'image/output.png'


class DrawBox(BaseTool):
    default_desc = 'A tool to draw a box on a certain region of the input image.'

    def apply(
        self,
        image: ImageIO,
        bbox: Annotated[str,
                        Info('The bbox coordinate in the format of `(x1, y1, x2, y2)`')],
        annotation: Annotated[Optional[str],
                              Info('The extra annotation text of the bbox')] = None,
    ) -> ImageIO:
        return 'image/output.png'
    
    def __call__(self, *args: Any, **kwargs) -> Any:
        return 'image/output.png'
    

class AddText(BaseTool):
    default_desc = 'A tool to draw a box on a certain region of the input image.'

    def apply(
        self,
        image: ImageIO,
        text: str,
        position: Annotated[
            str,
            Info('The left-bottom corner coordinate in the format of `(x, y)`, '
                 'or a combination of ["l"(left), "m"(middle), "r"(right)] '
                 'and ["t"(top), "m"(middle), "b"(bottom)] like "mt" for middle-top')],
        color: str = 'red',
    ) -> ImageIO:
        return 'image/output.png'

    def __call__(self, *args: Any, **kwargs) -> Any:
        return 'image/output.png'
    

class Plot(BaseTool):
    """A tool to plot diagrams using python interpreter.

    WARNING: The PythonInterpreter only has minimal protection, don't expose to
    trustless environment.

    Args:
        timeout (int, Optional): Upper bound of waiting time for Python script execution.
            Defaults to ``20``.
        toolmeta (None | dict | ToolMeta): The additional info of the tool.
            Defaults to None.
    """
    answer_expr = 'solution()'

    @require('matplotlib')
    def __init__(self, timeout: int = 20, toolmeta=None):
        super().__init__(toolmeta=toolmeta)
        self.timeout = timeout

    def apply(self, command: Annotated[str,
                                       Info('Markdown format Python code')]) -> ImageIO:

        return 'image/output.png'

    def _call(self, command: str) -> Image.Image:
        return 'image/output.png'


GENERATE_TOOLS = {
    "ImageStylization": ImageStylization(),
    "TextToImage": TextToImage(),
    "DrawBox": DrawBox(),
    "AddText": AddText(),
    "Plot": Plot()
}