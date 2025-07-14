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
from functions.gpt import get_completion_visual, get_completion
import json

import os
API_KEY = os.getenv('OPENAI_API_KEY')

with open('pretool_ours.json', 'r') as f:
    image_tool_results = json.load(f)

class ImageDescription(BaseTool):
    default_desc = ('A useful tool that returns a brief '
                    'description of the input image.')

    def __init__(self,
                 model='gpt-4o',
                 api_key=API_KEY,
                 base_url="https://29qg.com/v1",
                 toolmeta=None):
        super().__init__(toolmeta=toolmeta)
        self.model = model
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
    
    # def get_completion_visual(self, prompt, image):
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": [
    #                 {"type": "text", "text": prompt},
    #                 {
    #                     "type": "image_url",
    #                     "image_url": {
    #                         "url": "data:image/jpeg;base64," + image,
    #                     }
    #                 },
    #             ],
    #         }
    #     ]
    #     response = self.client.chat.completions.create(
    #         model=self.model,
    #         messages=messages,
    #         max_tokens=300,
    #     )
    #     return response.choices[0].message.content

    def apply(self, image: str) -> str:
        print("image", image)
        image_path = image_tool_results[image]
        if 'ImageDescription' in image_path:
            return image_path['ImageDescription']
        else:
            return 'Error: No image description found'


class CountGivenObject(BaseTool):
    default_desc = 'The tool can count the number of a certain object in the image.'

    def __init__(self,
                 model='gpt-4o',
                 api_key=API_KEY,
                 base_url="https://29qg.com/v1",
                 toolmeta=None):
        super().__init__(toolmeta=toolmeta)
        self.model = model
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
    
    # def get_completion_visual(self, prompt, image):
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": [
    #                 {"type": "text", "text": prompt},
    #                 {
    #                     "type": "image_url",
    #                     "image_url": {
    #                         "url": "data:image/jpeg;base64," + image,
    #                     }
    #                 },
    #             ],
    #         }
    #     ]
    #     response = self.client.chat.completions.create(
    #         model=self.model,
    #         messages=messages,
    #         max_tokens=300,
    #     )
    #     return response.choices[0].message.content

    def apply(
        self,
        image: str,
        text: Annotated[str, Info('The object description in English.')],
        bbox: Annotated[Optional[str],
                        Info('The bbox coordinate in the format of `(x1, y1, x2, y2)`')] = None,
    ) -> int:
        image_path = image_tool_results[image]
        if 'CountGivenObject' in image_path:
            return image_path['CountGivenObject']
        else:
            return 'Error: No object count found'


class RegionAttributeDescription(BaseTool):
    default_desc = 'Describe the attribute of a region of the input image.'

    def __init__(self,
                 model='gpt-4o',
                 api_key=API_KEY,
                 base_url="https://29qg.com/v1",
                 toolmeta=None):
        super().__init__(toolmeta=toolmeta)
        self.model = model
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
    
    # def get_completion_visual(self, prompt, image):
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": [
    #                 {"type": "text", "text": prompt},
    #                 {
    #                     "type": "image_url",
    #                     "image_url": {
    #                         "url": "data:image/jpeg;base64," + image,
    #                     }
    #                 },
    #             ],
    #         }
    #     ]
    #     response = self.client.chat.completions.create(
    #         model=self.model,
    #         messages=messages,
    #         max_tokens=500,
    #     )
    #     return response.choices[0].message.content

    def apply(
        self,
        image: str,
        bbox: Annotated[str,
                        Info('The bbox coordinate in the format of `(x1, y1, x2, y2)`')],
        attribute: Annotated[str, Info('The attribute to describe')],
    ) -> str:
        image_path = image_tool_results[image]
        if 'RegionAttributeDescription' in image_path:
            return image_path['RegionAttributeDescription']
        else:
            return 'Error: No region attribute description found'


# TODO: split question-ocr(gpt-4) and answer-ocr(paddleocr)
class OCR(BaseTool):
    """A tool to recognize the optical characters on an image.

    Args:
        lang (str | Sequence[str]): The language to be recognized.
            Defaults to 'en'.
        line_group_tolerance (int): The line group tolerance threshold.
            Defaults to -1, which means to disable the line group method.
        device (str | bool): The device to load the model. Defaults to True,
            which means automatically select device.
        **read_args: Other keyword arguments for read text. Please check the
            `EasyOCR docs <https://www.jaided.ai/easyocr/documentation/>`_.
        toolmeta (None | dict | ToolMeta): The additional info of the tool.
            Defaults to None.
    """

    default_desc = 'This tool can recognize all text on the input image.'

    def __init__(self,
                 model='gpt-4o',
                 api_key=API_KEY,
                 base_url="https://29qg.com/v1",
                 toolmeta=None):
        super().__init__(toolmeta=toolmeta)
        self.ocrmodel = {}
        self.model = model
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

    # def get_completion_visual(self, prompt, image):
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": [
    #                 {"type": "text", "text": prompt},
    #                 {
    #                     "type": "image_url",
    #                     "image_url": {
    #                         "url": "data:image/jpeg;base64," + image,
    #                     }
    #                 },
    #             ],
    #         }
    #     ]
    #     response = self.client.chat.completions.create(
    #         model=self.model,
    #         messages=messages,
    #         max_tokens=500,
    #     )
    #     return response.choices[0].message.content

    def apply(self, image: str, lang: str='en') -> str:
        '''
        args:
            image: PIL image
        return:
            result: list of item
            item: {"text": text, "conf": confidence, "bbox": (x0, y0, x1, y1)}
        '''
        image_path = image_tool_results[image]
        if 'OCR' in image_path:
            return image_path['OCR']
        else:
            return 'Error: No OCR result found'
        
class TextToBbox(BaseTool):
    """A tool to detection the given object.

    Args:
        model (str): The model name used to detect texts.
            Which can be found in the ``MMDetection`` repository.
            Defaults to ``glip_atss_swin-t_a_fpn_dyhead_pretrain_obj365``.
        device (str): The device to load the model. Defaults to 'cpu'.
        toolmeta (None | dict | ToolMeta): The additional info of the tool.
            Defaults to None.
    """

    default_desc = ('The tool can detect the object location according to '
                    'description.')

    def __init__(self,
                 model: str = 'glip_atss_swin-l_fpn_dyhead_pretrain_mixeddata',
                 device: str = 'cuda',
                 toolmeta=None):
        super().__init__(toolmeta=toolmeta)
        self.model = model
        self.device = device

    def apply(
        self,
        image: str,
        text: Annotated[str, Info('The object description in English.')],
        top1: Annotated[bool,
                        Info('If true, return the object with highest score. '
                             'If false, return all detected objects.')] = True,
    ) -> Annotated[str,
                   Info('Detected objects, include bbox in '
                        '(x1, y1, x2, y2) format, and detection score.')]:
        image_path = image_tool_results[image]
        if 'TextToBbox' in image_path:
            return image_path['TextToBbox']
        else:
            return 'Error: No text to bbox result found'

        

# class ImageStylization(BaseTool):
#     """A tool to stylize an image.

#     Args:
#         model (str): The model name used to inference. Which can be found
#             in the ``diffusers`` repository.
#             Defaults to 'timbrooks/instruct-pix2pix'.
#         inference_steps (int): The number of inference steps. Defaults to 20.
#         device (str): The device to load the model. Defaults to 'cuda'.
#         toolmeta (None | dict | ToolMeta): The additional info of the tool.
#             Defaults to None.
#     """

#     default_desc = ('This tool can modify the input image according to the '
#                     'input instruction. Here are some example instructions: '
#                     '"turn him into cyborg", "add fireworks to the sky", '
#                     '"make his jacket out of leather".')

#     @require('diffusers')
#     def __init__(self,
#                  model: str = 'timbrooks/instruct-pix2pix',
#                  inference_steps: int = 20,
#                  device: str = 'cuda',
#                  toolmeta=None):
#         super().__init__(toolmeta=toolmeta)
#         self.model_name = model
#         self.inference_steps = inference_steps
#         self.device = device

#     def setup(self):
#         pass

#     def apply(self, image: str, instruction: str) -> str:
#         return 'image/output.png'
    
#     def __call__(self, *args: Any, **kwargs) -> Any:
#         return 'image/output.png'

    
# class TextToImage(BaseTool):
#     """A tool to generate image according to some keywords.

#     Args:
#         model (str): The stable diffusion model to use. You can choose
#             from "sd" and "sdxl". Defaults to "sd".
#         device (str): The device to load the model. Defaults to 'cuda'.
#         toolmeta (None | dict | ToolMeta): The additional info of the tool.
#             Defaults to None.
#     """

#     default_desc = ('This tool can generate an image according to the '
#                     'input text.')

#     @require('diffusers')
#     def __init__(
#         self,
#         model: str = 'sdxl',
#         num_inference_steps: int = 30,
#         device: str = 'cuda',
#         toolmeta=None,
#     ):
#         super().__init__(toolmeta=toolmeta)
#         assert model in ['sd', 'sdxl', 'sdxl-turbo']
#         self.model = model
#         self.device = device
#         self.num_inference_steps = num_inference_steps

#     def setup(self):
#         pass
    
#     def apply(
#         self,
#         keywords: Annotated[str,
#                             Info('A series of keywords separated by comma.')],
#     ) -> str:
#         return 'image/output.png'

#     def __call__(self, *args: Any, **kwargs) -> Any:
#         return 'image/output.png'


# class DrawBox(BaseTool):
#     default_desc = 'A tool to draw a box on a certain region of the input image.'

#     def apply(
#         self,
#         image: str,
#         bbox: Annotated[str,
#                         Info('The bbox coordinate in the format of `(x1, y1, x2, y2)`')],
#         annotation: Annotated[Optional[str],
#                               Info('The extra annotation text of the bbox')] = None,
#     ) -> str:
#         return 'image/output.png'
    
#     def __call__(self, *args: Any, **kwargs) -> Any:
#         return 'image/output.png'
    

# class AddText(BaseTool):
#     default_desc = 'A tool to draw a box on a certain region of the input image.'

#     def apply(
#         self,
#         image: str,
#         text: str,
#         position: Annotated[
#             str,
#             Info('The left-bottom corner coordinate in the format of `(x, y)`, '
#                  'or a combination of ["l"(left), "m"(middle), "r"(right)] '
#                  'and ["t"(top), "m"(middle), "b"(bottom)] like "mt" for middle-top')],
#         color: str = 'red',
#     ) -> str:
#         return 'image/output.png'

#     def __call__(self, *args: Any, **kwargs) -> Any:
#         return 'image/output.png'


# class OCR(BaseTool):
#     """A tool to recognize the optical characters on an image.

#     Args:
#         lang (str | Sequence[str]): The language to be recognized.
#             Defaults to 'en'.
#         line_group_tolerance (int): The line group tolerance threshold.
#             Defaults to -1, which means to disable the line group method.
#         device (str | bool): The device to load the model. Defaults to True,
#             which means automatically select device.
#         **read_args: Other keyword arguments for read text. Please check the
#             `EasyOCR docs <https://www.jaided.ai/easyocr/documentation/>`_.
#         toolmeta (None | dict | ToolMeta): The additional info of the tool.
#             Defaults to None.
#     """

#     default_desc = 'This tool can recognize all text on the input image.'

#     @require('easyocr')
#     def __init__(self,
#                  lang: Union[str, Sequence[str]] = 'en',
#                  line_group_tolerance: int = -1,
#                  device: Union[bool, str] = True,
#                  toolmeta=None,
#                  **read_args):
#         super().__init__(toolmeta=toolmeta)
#         if isinstance(lang, str):
#             lang = [lang]
#         self.lang = list(lang)
#         self.read_args = read_args
#         self.device = device
#         self.line_group_tolerance = line_group_tolerance
#         read_args.setdefault('decoder', 'beamsearch')

#         if line_group_tolerance >= 0:
#             read_args.setdefault('paragraph', False)
#         else:
#             read_args.setdefault('paragraph', True)

#     def setup(self):
#         import easyocr
#         self._reader: easyocr.Reader = load_or_build_object(
#             easyocr.Reader, self.lang, gpu=self.device)

#     def apply(
#         self,
#         image: str,
#     ) -> Annotated[str,
#                    Info('OCR results, include bbox in x1, y1, x2, y2 format '
#                         'and the recognized text.')]:

#         image = image.to_array()
#         results = self._reader.readtext(image, detail=1, **self.read_args)
#         results = [(self.extract_bbox(item[0]), item[1]) for item in results]

#         if self.line_group_tolerance >= 0:
#             results.sort(key=lambda x: x[0][1])

#             groups = []
#             group = []

#             for item in results:
#                 if not group:
#                     group.append(item)
#                     continue

#                 if abs(item[0][1] - group[-1][0][1]) <= self.line_group_tolerance:
#                     group.append(item)
#                 else:
#                     groups.append(group)
#                     group = [item]

#             groups.append(group)

#             results = []
#             for group in groups:
#                 # For each line, sort the elements by their left x-coordinate and join their texts
#                 line = sorted(group, key=lambda x: x[0][0])
#                 bboxes = [item[0] for item in line]
#                 text = ' '.join(item[1] for item in line)
#                 results.append((self.extract_bbox(bboxes), text))

#         outputs = []
#         for item in results:
#             outputs.append('({}, {}, {}, {}) {}'.format(*item[0], item[1]))
#         outputs = '\n'.join(outputs)
#         return outputs

#     @staticmethod
#     def extract_bbox(char_boxes) -> Tuple[int, int, int, int]:
#         xs = [int(box[0]) for box in char_boxes]
#         ys = [int(box[1]) for box in char_boxes]
#         return min(xs), min(ys), max(xs), max(ys)

# class OCR(BaseTool):
#     """A tool to recognize the optical characters on an image.

#     Args:
#         lang (str | Sequence[str]): The language to be recognized.
#             Defaults to 'en'.
#         line_group_tolerance (int): The line group tolerance threshold.
#             Defaults to -1, which means to disable the line group method.
#         device (str | bool): The device to load the model. Defaults to True,
#             which means automatically select device.
#         **read_args: Other keyword arguments for read text. Please check the
#             `EasyOCR docs <https://www.jaided.ai/easyocr/documentation/>`_.
#         toolmeta (None | dict | ToolMeta): The additional info of the tool.
#             Defaults to None.
#     """

#     default_desc = 'This tool can recognize all text on the input image.'

#     def __init__(self,
#                  model='gpt-4o',
#                  api_key="xxx",
#                  base_url="https://29qg.com/v1",
#                  toolmeta=None):
#         super().__init__(toolmeta=toolmeta)
#         self.model = model
#         self.client = OpenAI(
#             api_key=api_key,
#             base_url=base_url
#         )
    
#     def get_completion_visual(self, prompt, image):
#         messages=[
#             {
#                 "role": "user",
#                 "content": [
#                     {"type": "text", "text": prompt},
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": "data:image/jpeg;base64," + image,
#                         }
#                     },
#                 ],
#             }
#         ]
#         response = self.client.chat.completions.create(
#             model=self.model,
#             messages=messages,
#             max_tokens=500,
#         )
#         return response.choices[0].message.content

#     def apply(self, image: str) -> str:
#         image = image.value
#         with BytesIO() as buffered:
#             image.save(buffered, format="WEBP")
#             image = base64.b64encode(buffered.getvalue()).decode("utf-8")
#         return self.get_completion_visual('Recognize the text and its position in the image. Your answer should follow that format:\n```\n(x11, y11, x12, y12): Text1\n(x21, y21, x22, y22): Text2\n```', image)

# class OCR(BaseTool):
#     """A tool to recognize the optical characters on an image.

#     Args:
#         lang (str | Sequence[str]): The language to be recognized.
#             Defaults to 'en'.
#         line_group_tolerance (int): The line group tolerance threshold.
#             Defaults to -1, which means to disable the line group method.
#         device (str | bool): The device to load the model. Defaults to True,
#             which means automatically select device.
#         **read_args: Other keyword arguments for read text. Please check the
#             `EasyOCR docs <https://www.jaided.ai/easyocr/documentation/>`_.
#         toolmeta (None | dict | ToolMeta): The additional info of the tool.
#             Defaults to None.
#     """

#     default_desc = 'This tool can recognize all text on the input image.'

#     def __init__(self,
#                  lang: Union[str, Sequence[str]] = 'en',
#                  line_group_tolerance: int = -1,
#                  device: Union[bool, str] = True,
#                  toolmeta=None,
#                  **read_args):
#         super().__init__(toolmeta=toolmeta)
#         if isinstance(lang, str):
#             lang = [lang]
#         self.lang = list(lang)
#         self.read_args = read_args
#         self.device = device
#         self.line_group_tolerance = line_group_tolerance
#         read_args.setdefault('decoder', 'beamsearch')

#         if line_group_tolerance >= 0:
#             read_args.setdefault('paragraph', False)
#         else:
#             read_args.setdefault('paragraph', True)

#     def setup(self):
#         self.ocrmodel = PaddleOCR(use_angle_cls=False, lang=self.lang[0], show_log=False)

#     def apply(
#         self,
#         image: str,
#     ) -> Annotated[str,
#                    Info('OCR results, include bbox in x1, y1, x2, y2 format '
#                         'and the recognized text.')]:

#         image = image.to_array()
#         results = self.ocrmodel.ocr(image, cls=False)[0]
#         results = [(self.extract_bbox(item[0]), item[1]) for item in results]

#         if self.line_group_tolerance >= 0:
#             print("yesssssssssssssssssssssssssssssssss")
#             results.sort(key=lambda x: x[0][1])

#             groups = []
#             group = []

#             for item in results:
#                 if not group:
#                     group.append(item)
#                     continue

#                 if abs(item[0][1] - group[-1][0][1]) <= self.line_group_tolerance:
#                     group.append(item)
#                 else:
#                     groups.append(group)
#                     group = [item]

#             groups.append(group)

#             results = []
#             for group in groups:
#                 # For each line, sort the elements by their left x-coordinate and join their texts
#                 line = sorted(group, key=lambda x: x[0][0])
#                 bboxes = [item[0] for item in line]
#                 text = ' '.join(item[1] for item in line)
#                 results.append((self.extract_bbox(bboxes), text))

#         outputs = []
#         for item in results:
#             outputs.append('({}, {}, {}, {}) {}'.format(*item[0], item[1]))
#         outputs = '\n'.join(outputs)
#         return outputs

#     @staticmethod
#     def extract_bbox(char_boxes) -> Tuple[int, int, int, int]:
#         xs = [int(box[0]) for box in char_boxes]
#         ys = [int(box[1]) for box in char_boxes]
#         return min(xs), min(ys), max(xs), max(ys)
