# Unified Modular AI Agent (Router with Task-Specific Handlers)

import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# === Streamlit UI ===
st.set_page_config(page_title="Coaching AI Router Agent", layout="centered")
st.title("🧠 Unified AI Agent for Coaching AI")

task_type = st.selectbox("Select Agent Task", [
    "Social Media Post",
    "Web Scraping Request",
    "Database Cleaning Instruction",
    "Sales Outreach Message"
])

user_input = st.text_area("Describe the task:")

def build_prompt(task_type, user_input):
    if task_type == "Social Media Post":
        return f"""You are an AI Social Media Manager for a sports analytics platform.
Create a concise, engaging social media post for X and LinkedIn.
Focus on coaching performance analytics. Respond only with the copy.
Task: {user_input}"""
    
    elif task_type == "Web Scraping Request":
        return f"""You are an AI Web Scraping Assistant.
Interpret this request to identify what data needs to be extracted, from which site, and what format it should be returned in.
Task: {user_input}"""

    elif task_type == "Database Cleaning Instruction":
        return f"""You are an AI Database Cleaner.
Interpret the instruction to resolve data conflicts, remove duplicates, and flag incomplete entries in a coaching data table.
Task: {user_input}"""

    elif task_type == "Sales Outreach Message":
        return f"""You are an AI Sales Agent for Coaching AI.
Draft a professional, attention-grabbing email or LinkedIn message tailored to a prospect.
Focus on the value of CPAS and SQAI tools in staff evaluation and decision-making.
Task: {user_input}"""
    
    else:
        return "Unrecognized task type."

# === Run Agent ===
if st.button("Generate Output"):
    if user_input:
        # Define system prompt based on selected task
        system_prompt = build_prompt(task_type, user_input)

        # Define messages to be passed to the LLM
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_input)
        ]

        # Initialize LLM
        llm = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-3.5-turbo",
    request_timeout=90,
    max_retries=5,
    streaming=True,  # optional but reduces timeout risk
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

        # Call the model
        response = llm.invoke(messages)
        output = response.content

        st.subheader("Generated Output")
        st.write(output)
    else:
        st.warning("Please enter a task description.")
