import json
import os
from datetime import datetime

import requests
from dotenv import load_dotenv


# ============================================================
# Environment
# ============================================================

load_dotenv(override=True)

pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")

pushover_url = "https://api.pushover.net/1/messages.json"


# ============================================================
# Pushover
# ============================================================

def push(text):
    """Send a notification through Pushover."""

    response = requests.post(
        pushover_url,
        data={
            "token": pushover_token,
            "user": pushover_user,
            "message": text,
        },
        timeout=10,
    )

    response.raise_for_status()

    return response.json()


# ============================================================
# Tool Functions
# ============================================================

def get_current_time():
    """Return the current local date and time."""

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def record_user_details(
    email,
    name="Name not provided",
    notes="not provided",
):
    """Record contact details of an interested user."""

    push(
        f"Recording interest from {name} "
        f"with email {email} and notes {notes}"
    )

    return "OK"


def record_unknown_question(question):
    """Record a question that the assistant could not answer."""

    push(
        f"Recording question that I couldn't answer:\n{question}"
    )

    return "OK"


def search_web(query):
    """
    Search the web for up-to-date information.

    Currently this is a placeholder.
    """

    return f"Search results for: {query}"


def get_profile_info(topic):
    """
    Retrieve information about Ahmed's profile,
    experience, education, skills, or projects.

    Currently this is a placeholder.
    """

    return f"Profile information about: {topic}"


def record_conversation(email, summary):
    """Record a summary of an important conversation."""

    push(
        f"Conversation recorded with {email}\n"
        f"Summary: {summary}"
    )

    return "OK"


def send_email(to, subject, body):
    """
    Send an email to a recipient.

    Currently this is a placeholder.
    """

    push(
        f"Email sent to {to}\n"
        f"Subject: {subject}"
    )

    return "OK"


def create_task(title, description="not provided"):
    """Create a task for later follow-up."""

    push(
        f"New task created: {title}\n"
        f"Description: {description}"
    )

    return "OK"


# ============================================================
# Tool Schemas
# ============================================================

record_user_details_json = {
    "type": "function",
    "function": {
        "name": "record_user_details",
        "description": (
            "Record the user's contact details and any "
            "additional notes when they express interest."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string",
                    "description": "The user's email address.",
                },
                "name": {
                    "type": "string",
                    "description": "The user's name.",
                },
                "notes": {
                    "type": "string",
                    "description": (
                        "Additional notes about the user's interest."
                    ),
                },
            },
            "required": ["email"],
        },
    },
}


record_unknown_question_json = {
    "type": "function",
    "function": {
        "name": "record_unknown_question",
        "description": (
            "Record a question that the assistant was unable to answer."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": (
                        "The question that the assistant "
                        "could not answer."
                    ),
                },
            },
            "required": ["question"],
        },
    },
}


get_current_time_json = {
    "type": "function",
    "function": {
        "name": "get_current_time",
        "description": "Get the current local date and time.",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },
}


search_web_json = {
    "type": "function",
    "function": {
        "name": "search_web",
        "description": (
            "Search the internet for up-to-date information "
            "that may not be available in the assistant's knowledge."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": (
                        "The search query to look up on the internet."
                    ),
                },
            },
            "required": ["query"],
        },
    },
}


get_profile_info_json = {
    "type": "function",
    "function": {
        "name": "get_profile_info",
        "description": (
            "Retrieve information about Ahmed's professional profile, "
            "including his education, skills, projects, experience, "
            "and certifications."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": (
                        "The profile topic to retrieve information about, "
                        "such as skills, education, projects, experience, "
                        "or certifications."
                    ),
                },
            },
            "required": ["topic"],
        },
    },
}


record_conversation_json = {
    "type": "function",
    "function": {
        "name": "record_conversation",
        "description": (
            "Record a summary of an important conversation "
            "for future reference."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string",
                    "description": (
                        "The email address associated with "
                        "the conversation."
                    ),
                },
                "summary": {
                    "type": "string",
                    "description": (
                        "A concise summary of the conversation."
                    ),
                },
            },
            "required": ["email", "summary"],
        },
    },
}


send_email_json = {
    "type": "function",
    "function": {
        "name": "send_email",
        "description": "Send an email to a specified recipient.",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {
                    "type": "string",
                    "description": "The recipient's email address.",
                },
                "subject": {
                    "type": "string",
                    "description": "The subject of the email.",
                },
                "body": {
                    "type": "string",
                    "description": "The content of the email.",
                },
            },
            "required": ["to", "subject", "body"],
        },
    },
}


create_task_json = {
    "type": "function",
    "function": {
        "name": "create_task",
        "description": (
            "Create a task that needs to be completed "
            "or followed up later."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "The title of the task.",
                },
                "description": {
                    "type": "string",
                    "description": "Additional details about the task.",
                },
            },
            "required": ["title"],
        },
    },
}


# ============================================================
# All Tools
# ============================================================

tools = [
    record_user_details_json,
    record_unknown_question_json,
    get_current_time_json,
    search_web_json,
    get_profile_info_json,
    record_conversation_json,
    send_email_json,
    create_task_json,
]


# ============================================================
# Tool Map
# ============================================================

tool_map = {
    "record_user_details": record_user_details,
    "record_unknown_question": record_unknown_question,
    "get_current_time": get_current_time,
    "search_web": search_web,
    "get_profile_info": get_profile_info,
    "record_conversation": record_conversation,
    "send_email": send_email,
    "create_task": create_task,
}


# ============================================================
# Tool Call Handler
# ============================================================

def handle_tool_call(tool_calls):
    """Execute tool calls returned by the LLM."""

    results = []

    for tool_call in tool_calls:

        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print(f"Tool called: {tool_name}", flush=True)

        tool = tool_map.get(tool_name)

        if tool is None:
            result = f"Unknown tool: {tool_name}"

        else:
            try:
                result = tool(**arguments)

            except Exception as e:
                result = f"Tool execution failed: {str(e)}"

        results.append(
            {
                "role": "tool",
                "content": json.dumps(result),
                "tool_call_id": tool_call.id,
            }
        )

    return results