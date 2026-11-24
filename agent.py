from llm import chat
from prompt import SYSTEM_PROMPT
from file_generator import generate_plan_file
class StudyPlannerAgent:
    def __init__(self,api_key=None):
        self.api_key = api_key
        self.messages = [
            {
                "role":"system",
                "content":SYSTEM_PROMPT,
            }
        ]
    def run (self,user_input):
        self.messages.append(
            {
                "role":"user",
                "content":user_input
            }
        )
        answer = chat(self.messages,self.api_key)
        self.messages.append({
            "role":"assistant",
            "content":answer
        })
        return answer
    def export_plan(self ,content,filename="学习计划.md"   ):
        path = generate_plan_file(content,filename)
        return path

