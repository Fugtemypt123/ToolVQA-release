# version >= 1.0.0

from openai import OpenAI
from PIL import Image
import base64
from io import BytesIO
import os
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
  # api_key="sb-01de4de571ca283e762722fe1fe5e4a07309338b8004f6c5",
  api_key=api_key,
  # base_url = 'https://api.openai-sb.com/v1'
  base_url="https://29qg.com/v1"
)

# def get_completion(prompt, model="gpt-3.5-turbo-1106", temperature=0.5):
#     messages = [{"role": "user", "content": prompt}]
#     response = client.chat.completions.create(
#         model=model,
#         messages=messages,
#         temperature=temperature,
#     )
#     return response.choices[0].message.content

def get_completion(prompt, model="chatgpt-4o-latest", temperature=0.5):
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
            ],
        }
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        # max_tokens=300,
        # temperature=temperature,
    )
    return response.choices[0].message.content

def get_completion_visual(prompt, image, model="chatgpt-4o-latest"):
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "data:image/jpeg;base64," + image, # 对于claude模型，这里一定要符合图片的格式否则会出错
                    }
                },
            ],
        }
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        # max_tokens=300,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    prompt = "Does the wine in this image seem to have an AOP certification from Bordeaux?"
    with Image.open("/network_space/server126/shared/yinshaofeng/ToolLLM/GTA/datasets/MTWI/image_train/TB1lHpnLXXXXXbwapXXunYpLFXX.jpg") as img:
        img.thumbnail((800, 800))
        if img.mode == 'P' or img.mode == 'RGBA':
            img = img.convert('RGB')
        buffered = BytesIO()
        img.save(buffered, format="jpeg")  # 将图片保存到字节流
        image = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # with open(query_image_path, "rb") as f:
        #     image = base64.b64encode(f.read()).decode("utf-8")
    # image = Image.open("/network_space/server126/shared/yinshaofeng/ToolLLM/GTA/agentlego/examples/demo.png")
    print(get_completion_visual(prompt, image, model='claude-3-5-sonnet-20240620'))
    # print(get_completion("你好！"))


# version < 1.0.0

# # 目前需要设置代理才可以访问 api
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

# class ChatGPT:
#     def __init__(self): 
#         self.openai = openai
#         self.RateLimitError = RateLimitError

#     def __call__(self, msg, temperature=0.0, max_tokens=1000):
#         self.openai.api_base = "https://api.openai-sb.com/v1"
#         max_retry = 3
#         for _ in range(max_retry):
#             try:
#                 response = self.openai.ChatCompletion.create(
#                     model='gpt-3.5-turbo',
#                     messages=[{"role": "user", "content": [
#                         {"type": "text", "text": msg},
#                     ]}],
#                     temperature=temperature,
#                     max_tokens=max_tokens,
#                     api_key = "sb-01de4de571ca283e762722fe1fe5e4a07309338b8004f6c5" # from ysfff
#                 )
#                 return response.choices[0]["message"]["content"]
#             except:
#                 print("RateLimitError, retrying...") # 40K tokens per min
#                 time.sleep(30)
#                 continue
#         raise self.RateLimitError(f"Reached {max_retry} times retry, aborting...")


# if __name__ == "__main__":
#     msg = "Please write a Python function that takes a list of numbers and returns the sum of all the numbers in the list."
#     gpt = ChatGPT()
#     res = gpt(msg)
#     print(res)
    # PATH = "A-OKVQA/test2017/test2017/000000000001.jpg"
    # image = Image.open(PATH).convert("RGB")
    # caption = generate_caption(image)
    # print(caption)

# openai.api_base = "https://api.openai-sb.com/v1"

# ques = "how are you today?"
# res = get_response(ques)
# print(res)
