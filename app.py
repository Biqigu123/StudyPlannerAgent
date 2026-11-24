import streamlit as st
from agent import StudyPlannerAgent
from file_generator import generate_plan_file
st.set_page_config(
    page_title="Study Planner",
    page_icon="📚",
    layout="wide"
)
st.title("📚 StudyPlannerAgent")
st.caption("你的智能学习规划助手")

st.sidebar.header("模型配置")
api_key = st.sidebar.text_input(
    "DeepSeek API Key",
    type="password",
    placeholder="请输入你的 API Key"
)
if "messages" not in st.session_state:
    st.session_state.messages = []
if api_key:
    if(
        "agent" not in st.session_state
        or st.session_state.get("active_key") != api_key

    ):
        st.session_state.agent = StudyPlannerAgent(
            api_key=api_key
        )
        st.session_state.active_key = api_key

else:

        st.session_state.pop("agent",None)
        st.session_state.pop("active_key",None)
        st.session_state.pop("messages",None)

if not api_key:
        st.info("请先在左侧输入自己的 DeepSeek API Key。")
        st.stop()

if st.sidebar.button("清空对话"):

        st.session_state.agent.clear_memory()
        st.session_state.messages = []
        st.rerun()

for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


user_input = st.chat_input("请输入你的学习目标或问题...")

if user_input:
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })
        with st.chat_message("user"):
            st.markdown(user_input)
        with st.chat_message("assistant"):

         with st.spinner("Agent 正在思考..."):
            try:
                answer = st.session_state.agent.run(user_input)
                st.markdown(answer)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })
            except Exception as e:
                st.error(f"发生错误：{e}")
if st.session_state.messages:
        last_answer = next(
            (
                item["content"]
                for item in reversed(st.session_state.messages)
                if item["role"] == "assistant"
            ),
            ""
        )
        if last_answer:
          st.sidebar.download_button(
            "📥 下载最近一次回答",
            data=last_answer,
            file_name="study_plan.md",
            mime="text/markdown"
        )

