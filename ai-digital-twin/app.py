import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_call
from styles import CSS, JS, EXAMPLES


# ============================================================
# Configuration
# ============================================================

load_dotenv(override=True)

MODEL_NAME = "openai/gpt-oss-120b"

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
)

SYSTEM_MESSAGE = {
    "role": "system",
    "content": TWIN_SYSTEM_PROMPT,
}


# ============================================================
# Chat Logic
# ============================================================

def chat(message, history):

    history = [
        {
            "role": item["role"],
            "content": item["content"],
        }
        for item in history
    ]

    messages = [
        SYSTEM_MESSAGE,
        *history,
        {
            "role": "user",
            "content": message,
        },
    ]

    # ========================================================
    # Agent Loop
    # ========================================================

    for _ in range(10):

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=tools,
            tool_choice="auto",
        )

        assistant_message = response.choices[0].message

        print(
            f"Finish reason: {response.choices[0].finish_reason}",
            flush=True,
        )

        # ----------------------------------------------------
        # No tool call -> final answer
        # ----------------------------------------------------

        if not assistant_message.tool_calls:
            return assistant_message.content

        # ----------------------------------------------------
        # Tool calls detected
        # ----------------------------------------------------

        print(
            f"Tool calls detected: {len(assistant_message.tool_calls)}",
            flush=True,
        )

        messages.append(assistant_message)

        # Execute tools
        tool_results = handle_tool_call(
            assistant_message.tool_calls
        )

        messages.extend(tool_results)

    return "I couldn't complete the request."


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