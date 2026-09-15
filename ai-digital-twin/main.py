import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
import os

from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_call
from styles import CSS, JS, EXAMPLES


# ============================================================
# Configuration
# ============================================================

load_dotenv(override=True)

MODEL_NAME = "openai/gpt-oss-120b"

client = OpenAI(base_url="https://api.groq.com/openai/v1",api_key=os.getenv("GROQ_API_KEY"))


SYSTEM_MESSAGE = {
    "role": "system",
    "content": TWIN_SYSTEM_PROMPT,
}


# ============================================================
# Chat Logic
# ============================================================

def chat(message, history):
    """
    Handle a user message and return the assistant response.
    """
    history = [{"role":h["role"],"content":h["content"]} for h in history]
    
    messages = [
        SYSTEM_MESSAGE,
        *history,
        {
            "role": "user",
            "content": message,
        },
    ]

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools,
    )

    # --------------------------------------------------------
    # Tool-calling loop
    # --------------------------------------------------------

    while response.choices[0].finish_reason == "tool_calls":

        assistant_message = response.choices[0].message

        tool_calls = assistant_message.tool_calls

        # Add assistant tool-call message
        messages.append(assistant_message)

        # Execute tools
        tool_results = handle_tool_call(tool_calls)

        # Add tool results
        messages.extend(tool_results)

        # Ask the model again using the tool results
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=tools,
        )

    return response.choices[0].message.content


# ============================================================
# Gradio App
# ============================================================

if __name__ == "__main__":

    demo = gr.ChatInterface(
        fn=chat,
        examples=EXAMPLES,
        title="AI Digital Twin",
        description=(
            "Talk to my AI twin about my background, "
            "projects, skills, and experience."
        ),
        chatbot=gr.Chatbot(
            show_label=False,
            height=480,
        ),
    )

    demo.launch(
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
    )