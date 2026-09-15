# AI Digital Twin

An AI-powered Digital Twin that represents my professional profile and allows users to ask questions about my background, skills, education, projects, experience, and certifications.

The system uses **LLM Tool Calling** to retrieve the required information and generate natural, accurate responses based on my actual profile.

---

## Overview

Instead of using a traditional RAG pipeline, this project uses **Tool Calling**.

The LLM decides which tool should be called based on the user's question, retrieves the relevant information, and then generates the final response.

### Example

**User:**

> What projects has Ahmed worked on?

**LLM:**

```text
Call → get_projects()
```

**Tool:**

```text
Returns the available project information
```

**LLM:**

```text
Generates a natural response using the tool result
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
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
     Profile       Projects       Skills
        │             │             │
        └─────────────┼─────────────┘
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

* Ask questions about my professional profile
* Retrieve information using LLM Tool Calling
* Answer questions about:

  * Profile
  * Skills
  * Projects
  * Education
  * Experience
  * Certifications
* Simple Gradio chat interface
* CV-based context
* Structured tool responses
* Designed to minimize hallucination
* No vector database
* No embeddings
* No chunking
* No RAG pipeline

---

## Example Questions

The Digital Twin can answer questions such as:

```text
Who is Ahmed Elsayed Taha?

What are Ahmed's main skills?

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

---

## How It Works

The system is based on three main components:

### 1. Context

The project uses the CV and a structured summary as the main sources of profile information.

```text
data/
├── cv.pdf
└── summary.txt
```

`context.py` is responsible for loading and preparing this information.

---

### 2. Tools

The LLM has access to several tools through Tool Calling.

Examples:

```text
get_profile()
get_skills()
get_projects()
get_education()
get_experience()
get_certificates()
```

Each tool returns structured information related to a specific part of the profile.

For example:

```text
User:
What are Ahmed's technical skills?

        ↓

LLM

        ↓

get_skills()

        ↓

Tool Result

        ↓

LLM

        ↓

Final Answer
```

---

### 3. LLM

The LLM receives the user's question and decides whether a tool is required.

If the question requires profile information, the model calls the appropriate tool.

After receiving the tool result, the model generates the final answer.

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

Main application entry point.

Responsible for:

* Initializing the LLM
* Handling Tool Calling
* Managing the conversation
* Running the Gradio interface

---

### `context.py`

Responsible for loading the profile context from:

```text
data/cv.pdf
data/summary.txt
```

It prepares the information that will be used by the tools.

---

### `tools.py`

Contains the tools available to the LLM.

Example:

```text
get_profile()
get_skills()
get_projects()
get_education()
get_experience()
get_certificates()
```

---

### `styles.py`

Contains the custom CSS used to customize the Gradio interface.

---

### `data/cv.pdf`

The original CV containing the professional profile.

---

### `data/summary.txt`

A simplified and structured summary of the profile.

This makes it easier to organize information that the tools may need.

---

## Why Tool Calling Instead of RAG?

This project does not require a full RAG architecture because the information is:

* Small in size
* Structured
* Relatively static
* Organized into clear categories

For example, when the user asks about projects, the system does not need semantic search across thousands of documents.

It can simply call:

```text
get_projects()
```

This keeps the architecture simple and makes the Digital Twin easier to understand and maintain.

---

## RAG vs Tool Calling

### Traditional RAG

```text
Question
   ↓
Embedding
   ↓
Vector Database
   ↓
Similarity Search
   ↓
Retrieved Chunks
   ↓
LLM
   ↓
Answer
```

### This Project

```text
Question
   ↓
LLM
   ↓
Tool Calling
   ↓
Structured Profile Data
   ↓
LLM
   ↓
Answer
```

---

## Design Principle

The Digital Twin should only provide information supported by the available profile data.

If the requested information is not available, the system should clearly state that it does not have enough information instead of inventing an answer.

Example:

```text
User:
What was Ahmed's salary at his previous company?

AI:
I don't have information about Ahmed's previous salary.
```

This is important because the main goal is to create an accurate representation of the profile rather than a system that simply generates plausible answers.

---

## Technology Stack

* Python
* LLM API
* LLM Tool Calling / Function Calling
* Gradio
* Pydantic
* PDF text extraction
* HTML/CSS for UI customization

---

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ai-digital-twin
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```bash
cp .env.example .env
```

Then add your LLM API key.

Example:

```env
LLM_API_KEY=your_api_key_here
```

Do not commit your `.env` file to GitHub.

---

## Run the Application

Start the application with:

```bash
python main.py
```

After starting the application, open the Gradio interface in your browser.

---

## Example Interaction

```text
User:
Tell me about Ahmed's graduation project.

AI:
Ahmed's graduation project focused on Alzheimer’s
Detection with Generative AI...

User:
What technologies were used?

AI:
The project used technologies including...

User:
Does Ahmed have experience with LLMs?

AI:
Yes. Ahmed has worked on several LLM-related projects
and technologies including RAG, AI Agents, and LLM-based
applications.
```

The exact response is generated from the information available through the profile tools.

---

## Project Goal

The goal of this project is to build a simple but practical **AI Digital Twin** that can represent my professional profile and communicate information about my background through natural language.

The project also demonstrates practical usage of:

* LLMs
* Tool Calling
* Structured data
* Prompt engineering
* AI application architecture
* Gradio
* Python

---

## Author

**Ahmed Elsayed Taha**

AI Engineer | LLM Engineer

GitHub: `AhmedBenTaha`

LinkedIn: `Ahmed Taha`

---

## License

This project is intended for educational and portfolio purposes.
