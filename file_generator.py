import os
from  datetime import datetime

def generate_plan_file(content,filename="学习计划.md"):
    save_dir = "plans"
    os.makedirs(save_dir,exist_ok=True)

    file_path = os.path.join(save_dir,filename)
    with open(file_path,"w",encoding="utf-8") as f:
        f.write(content)
    return os.path.abspath(file_path)