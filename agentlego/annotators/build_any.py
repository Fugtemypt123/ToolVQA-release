import json
import concurrent.futures
from annotators.build_epoch import build_epoch, build_epoch_fixed
import random

random.seed(57)

with open("../datasets/datas.json", "r") as f:
    datas = json.load(f)

print("Total data: ", len(datas))

NUM = 10
parts = []
for i in range(NUM):
    parts.append(datas[i*len(datas)//NUM:(i+1)*len(datas)//NUM])
parts[-1] += datas[(i+1)*len(datas)//NUM:]
    
param_list = []
for i in range(NUM):
    param_list.append((i, i, parts[i]))

with concurrent.futures.ThreadPoolExecutor(max_workers=NUM) as executor:
    for param in param_list:
        executor.submit(build_epoch, param[0], param[1], param[2])
