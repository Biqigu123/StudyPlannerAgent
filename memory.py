import json
import os
DATA_DIR = "data"
os.makedirs(DATA_DIR,exist_ok=True)
def save_data(filename,data):
    path = os.path.join(DATA_DIR,filename)

    with open(path,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)

def load_data(filename):
    path = os.path.join(DATA_DIR,filename)
    if not os.path.exists(path):
        return []
    with open(path,"r",encoding="utf-8") as f:
        return json.load(f)