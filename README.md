# AI Digital Twin

An AI-powered Digital Twin that represents my professional profile and allows visitors to interact with an AI version of me.

The system can answer questions about my **background, skills, education, projects, experience, and certifications** using information extracted from my CV and profile summary.

It also demonstrates practical **LLM Tool Calling**, allowing the model to call external functions when a task requires an action such as recording contact information, logging unknown questions, getting the current time, or creating follow-up tasks.

---

## Overview

Instead of building a traditional RAG pipeline with embeddings and a vector database, this project uses **LLM Tool Calling**.

The LLM receives the user's message and decides whether one of the available tools should be called.

The tool executes the requested action and returns its result to the LLM.

The LLM then uses that result to generate the final response.

### Example

**User:**

```text
What time is it right now?
```

**LLM:**

```text
Call → get_current_time()
```

**Tool:**

```text
Returns the current date and time
```

**LLM:**

```text
Generates the final response using the tool result
```

---

## Architecture

```text
                         User
                           │
                           ▼
                     Gradio UI
                           │
                           ▼
                          LLM
                           │
                    Tool Calling
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
     Profile Tools    Action Tools     Utility Tools
          │                │                │
          │                │                │
          ▼                ▼                ▼
   Profile Data       Pushover          Current Time
          │            Notifications
          │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                      Tool Result
                           │
                           ▼
                          LLM
                           │
                           ▼
                      Final Answer
```

---

## Features

* AI-powered Digital Twin
* Professional profile Q&A
* LLM Tool Calling
* CV-based context
* Structured tool schemas
* Gradio chat interface
* Contact information collection
* Unknown question logging
* Current date and time tool
* Conversation recording
* Follow-up task creation
* Pushover notifications
* Custom dark UI
* Markdown responses
* Designed to reduce hallucination
* No vector database
* No embeddings
* No chunking
* No traditional RAG pipeline

---

## Available Tools

The Digital Twin currently exposes the following tools to the LLM:

| Tool                      | Purpose                                                |
| ------------------------- | ------------------------------------------------------ |
| `record_user_details`     | Records visitor contact information                    |
| `record_unknown_question` | Logs questions the Digital Twin cannot answer          |
| `get_current_time`        | Returns the current date and time                      |
| `search_web`              | Web search interface; currently a placeholder          |
| `get_profile_info`        | Retrieves profile information; currently a placeholder |
| `record_conversation`     | Records an important conversation                      |
| `send_email`              | Email interface; currently a placeholder               |
| `create_task`             | Creates a follow-up task                               |

### `record_user_details`

Used when a visitor wants to get in touch or expresses interest.

Example:

```text
User:

My name is Ahmed and my email is ahmed@example.com.
Please save my contact details.
```

The LLM can call:

```text
record_user_details(
    email="ahmed@example.com",
    name="Ahmed"
)
```

The tool sends a notification through Pushover.

---

### `record_unknown_question`

Used when the Digital Twin does not have enough information to answer a question.

Example:

```text
User:

What was Ahmed's previous salary?
```

The system can call:

```text
record_unknown_question(
    question="What was Ahmed's previous salary?"
)
```

This allows unknown questions to be logged instead of generating unsupported information.

---

### `get_current_time`

Returns the current local date and time.

Example:

```text
User:

What time is it right now?
```

The LLM calls:

```text
get_current_time()
```

The result is then returned to the LLM so it can generate the final response.

---

### `search_web`

Provides an interface for web search.

Currently, this tool is implemented as a **placeholder** and does not perform a real internet search yet.

It can be extended later to use a search API or another web-search service.

---

### `get_profile_info`

Designed to retrieve information about Ahmed's:

* Skills
* Education
* Projects
* Experience
* Certifications

The current implementation is a placeholder.

The tool can later be connected directly to the profile data loaded by `context.py`.

---

### `record_conversation`

Used to save a summary of an important conversation.

Example:

```text
record_conversation(
    email="ahmed@example.com",
    summary="Discussed a potential AI Engineer opportunity."
)
```

The current implementation sends the information through Pushover.

---

### `send_email`

Provides an interface for sending an email.

The current implementation is a **placeholder** and does not send an actual email yet.

It currently sends a Pushover notification containing the email information.

---

### `create_task`

Used to create a follow-up task.

Example:

```text
create_task(
    title="Follow up with recruiter",
    description="Contact the recruiter about the AI Engineer opportunity."
)
```

The current implementation sends a Pushover notification.

---

## Context

The Digital Twin uses two main sources of profile information:

```text
data/

├── cv.pdf
└── summary.txt
```

### CV

`data/cv.pdf` contains the original professional CV.

The PDF text is extracted using `pypdf`.

### Summary

`data/summary.txt` contains a simplified and structured summary of the professional profile.

This gives the LLM additional context about the person it represents.

---

## How It Works

The system consists of three main layers.

### 1. Context Layer

`context.py` loads the professional information.

```text
CV
 │
 ▼
PDF Text Extraction
 │
 ▼
Profile Context
 │
 ▼
System Prompt
```

The extracted CV content and profile summary are included in the system prompt given to the LLM.

---

### 2. Tool Layer

`tools.py` contains the functions available to the LLM.

Each function has two parts:

```text
Python Function
       +
Tool Schema
```

The tool schema tells the LLM:

* The tool name
* What the tool does
* What parameters it accepts
* Which parameters are required

For example:

```text
record_user_details
```

accepts:

```text
email
name
notes
```

The LLM can decide when this function should be called.

---

### 3. LLM Layer

`main.py` handles the conversation between the user and the LLM.

The basic flow is:

```text
User Message
     │
     ▼
    LLM
     │
     ├── No Tool Needed
     │       │
     │       ▼
     │    Final Answer
     │
     └── Tool Needed
             │
             ▼
        Tool Call
             │
             ▼
        Tool Execution
             │
             ▼
        Tool Result
             │
             ▼
            LLM
             │
             ▼
        Final Answer
```

This is the main Tool Calling loop implemented in the application.

---

## Tool Calling Example

For example, when the user asks:

```text
What time is it right now?
```

The model can decide to call:

```text
get_current_time()
```

The Python application executes the function.

The tool returns:

```text
2026-09-15 18:20:00
```

The result is then sent back to the LLM.

The LLM generates the final response:

```text
The current time is 6:20 PM.
```

---

## Project Structure

```text
ai-digital-twin/
│
├── main.py
├── context.py
├── tools.py
├── styles.py
│
├── data/
│   ├── cv.pdf
│   └── summary.txt
│
├── .env.example
├── requirements.txt
└── README.md
```

### `main.py`

The main application entry point.

Responsible for:

* Initializing the LLM client
* Managing the conversation
* Sending tool schemas to the LLM
* Detecting tool calls
* Executing tools
* Returning tool results to the LLM
* Running the Gradio interface

---

### `context.py`

Responsible for loading the profile context from:

```text
data/cv.pdf
data/summary.txt
```

It extracts the CV text and combines it with the profile summary to create the system prompt.

---

### `tools.py`

Contains:

* Tool implementations
* Tool schemas
* Tool mapping
* Tool execution logic

The current tools are:

```text
record_user_details
record_unknown_question
get_current_time
search_web
get_profile_info
record_conversation
send_email
create_task
```

---

### `styles.py`

Contains the custom CSS and JavaScript used to customize the Gradio interface.

The interface uses a dark AI-oriented visual style with:

* Dark background
* Gold accents
* Purple accents
* Custom message styling
* Responsive layout
* Custom input styling

---

### `data/cv.pdf`

The professional CV used as a source of profile information.

---

### `data/summary.txt`

A structured summary of the professional profile used to provide additional context to the Digital Twin.

---

## Why Tool Calling Instead of RAG?

This project does not require a full RAG architecture for its current use case.

The profile information is:

* Relatively small
* Structured
* Mostly static
* Divided into clear categories

For a small professional profile, introducing:

```text
Embeddings
      ↓
Vector Database
      ↓
Similarity Search
      ↓
Retrieved Chunks
```

would add unnecessary complexity.

Instead, Tool Calling provides a simpler architecture where the LLM can interact with specific functions when needed.

---

## RAG vs Tool Calling

### Traditional RAG

```text
Question
   │
   ▼
Embedding
   │
   ▼
Vector Database
   │
   ▼
Similarity Search
   │
   ▼
Retrieved Chunks
   │
   ▼
LLM
   │
   ▼
Answer
```

### This Project

```text
Question
   │
   ▼
LLM
   │
   ▼
Tool Calling
   │
   ▼
Tool Execution
   │
   ▼
Tool Result
   │
   ▼
LLM
   │
   ▼
Answer
```

The important difference is that **RAG retrieves relevant text**, while **Tool Calling allows the LLM to interact with functions**.

---

## Design Principle

The Digital Twin should represent the actual professional profile rather than inventing information.

If the requested information is not available, the system should avoid hallucinating an answer.

For example:

```text
User:

What was Ahmed's previous salary?

AI:

I don't have information about Ahmed's previous salary.
```

The system can also use:

```text
record_unknown_question()
```

to log the question for future improvement.

This creates a feedback loop where unanswered questions can be reviewed and used to improve the Digital Twin later.

---

## Example Questions

The Digital Twin can answer questions such as:

```text
Who is Ahmed Elsayed Taha?

What are Ahmed's main technical skills?

What AI projects has Ahmed worked on?

Tell me about Ahmed's graduation project.

What is Ahmed's educational background?

What certifications does Ahmed have?

What technologies does Ahmed use?

Does Ahmed have experience with LLMs?

What kind of AI systems does Ahmed build?

What is Ahmed's experience with RAG?

What programming languages does Ahmed know?
```

It can also perform tool-based actions such as:

```text
What time is it right now?

My name is John and my email is john@example.com.
Please save my contact details.

Please record this conversation.

Create a task to follow up with the recruiter.
```

---

## Testing the Tools

You can test the Tool Calling system directly from the Gradio interface.

### Test Current Time

```text
What time is it right now?
```

Expected terminal output:

```text
Tool called: get_current_time
```

---

### Test Contact Collection

```text
My name is John and my email is john@example.com.
Please save my contact details.
```

Expected terminal output:

```text
Tool called: record_user_details
```

A Pushover notification should also be generated if the Pushover credentials are configured correctly.

---

### Test Unknown Questions

```text
What is Ahmed's favorite football team?
```

If the information is not available, the system can call:

```text
record_unknown_question
```

Expected terminal output:

```text
Tool called: record_unknown_question
```

---

### Test Task Creation

```text
Create a task titled "Follow up with recruiter"
with description "Contact the recruiter about the AI Engineer opportunity."
```

Expected terminal output:

```text
Tool called: create_task
```

---

## Technology Stack

* Python
* OpenAI-compatible API
* Groq API
* `openai` Python SDK
* `openai/gpt-oss-120b`
* LLM Tool Calling / Function Calling
* Gradio
* Pydantic
* PyPDF
* Requests
* Python-dotenv
* HTML/CSS/JavaScript

---

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>

cd ai-digital-twin
```

### Create a Conda Environment

```bash
conda create -n ai-digital-twin python=3.11 -y
```

Activate it:

```bash
conda activate ai-digital-twin
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Then add your API credentials.

Example:

```env
GROQ_API_KEY=your_groq_api_key

PUSHOVER_USER=your_pushover_user
PUSHOVER_TOKEN=your_pushover_token
```

The application uses the Groq OpenAI-compatible API endpoint.

Do not commit your `.env` file to GitHub.

Make sure `.env` is included in `.gitignore`.

---

## Run the Application

Start the Digital Twin:

```bash
python main.py
```

Gradio will start the local web interface.

Open the displayed local URL in your browser.

---

## Notifications

The project uses **Pushover** for notifications.

Notifications can be triggered when:

* A visitor provides contact information
* An unknown question is recorded
* An important conversation is recorded
* A follow-up task is created
* An email action is requested

Pushover is used as a notification mechanism and is not responsible for generating the AI responses.

---

## Current Limitations

Some tools are currently implemented as placeholders.

### Web Search

```text
search_web()
```

Currently returns a placeholder response instead of performing a real internet search.

### Profile Retrieval

```text
get_profile_info()
```

Currently returns a placeholder response.

### Email

```text
send_email()
```

Currently does not send an actual email. It sends a notification through Pushover instead.

### Task Management

```text
create_task()
```

Currently sends a Pushover notification instead of creating a task in an external task-management system.

These tools are intentionally structured so they can be connected to real services in future versions.

---

## Future Improvements

Possible future extensions include:

* Real web search integration
* Real email sending
* CRM integration
* Calendar integration
* External task-management integration
* Persistent conversation storage
* Better profile retrieval
* Authentication
* Analytics dashboard
* Conversation evaluation
* Tool-call monitoring
* Production deployment
* Voice interaction
* WhatsApp integration

---

## Project Goal

The goal of this project is to build a practical **AI Digital Twin** that can represent my professional profile and interact with visitors using natural language.

The project demonstrates practical implementation of:

* LLMs
* Tool Calling
* Function schemas
* Prompt engineering
* Context management
* External actions
* Structured data
* AI application architecture
* Gradio
* Python

The main focus is not simply generating text, but building an AI application that can **reason about when to use tools and interact with external functions**.

---

## Author

**Ahmed Elsayed Taha**

AI Engineer | LLM Engineer

GitHub: `AhmedBenTaha`

LinkedIn: `Ahmed Taha`

---

## License

This project is intended for educational and portfolio purposes.
