from random import choice
from sys import path
import os
import sys



from agent import StudyPlannerAgent

def main():
    agent = StudyPlannerAgent()

    print("="*40)
    print("     Study Planner Agent")
    print("     AI 学习规划助手")
    print("="*40)

    print("输入 exit 退出程序\n")

    while True:
        user_input = input("你： ")
        if user_input.lower() == "exit":
            print("学习助手已退出")
            break
        try:
            answer = agent.run(user_input)
            print("\nAI: ")
            print(answer)
            print()
            choice = input("\n是否保存为文件？(y/n):")
            if choice.lower() == "y":
                path = agent.export_plan(answer)
                print(f"\n文件已保存: {path}")
        except Exception as e:
            print("error:",e)
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n程序运行出错：{e}")
    finally:
        input("\n程序已结束，按回车键关闭窗口...")