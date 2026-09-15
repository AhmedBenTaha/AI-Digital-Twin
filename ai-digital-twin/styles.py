"""Styling constants for the AI Digital Twin Gradio app."""

# ============================================================
# Theme
# ============================================================

GOLD = "#f5b82e"
BLUE = "#22a6d5"
PURPLE = "#8b5cf6"

BG = "#08090c"
SURFACE = "#0f1117"
SURFACE_2 = "#151821"
BORDER = "#242936"
BORDER_STRONG = "#343a49"

TEXT = "#f4f5f7"
MUTED = "#8b92a1"


# ============================================================
# Example Prompts
# ============================================================

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of AI projects are you working on?",
    "What are your strongest technical skills?",
    "Tell me about your LLM and RAG experience.",
    "How can I get in touch with you?",
]


# ============================================================
# CSS
# ============================================================

CSS = """
/* ==========================================================
   ROOT / THEME
   ========================================================== */

:root {
    --twin-gold: #f5b82e;
    --twin-blue: #22a6d5;
    --twin-purple: #8b5cf6;

    --twin-bg: #08090c;
    --twin-surface: #0f1117;
    --twin-surface-2: #151821;

    --twin-border: #242936;
    --twin-border-strong: #343a49;

    --twin-text: #f4f5f7;
    --twin-muted: #8b92a1;
}


/* ==========================================================
   GLOBAL
   ========================================================== */

html,
body,
gradio-app {
    background: var(--twin-bg) !important;
    color: var(--twin-text) !important;
}

body {
    margin: 0 !important;
    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif !important;
}


/* Hide Gradio branding / API elements */

footer,
.built-with,
.show-api,
.api-docs {
    display: none !important;
}


/* ==========================================================
   MAIN CONTAINER
   ========================================================== */

.gradio-container {
    width: 100% !important;
    max-width: 920px !important;
    min-width: 0 !important;

    margin: 0 auto !important;
    padding: 34px 24px 50px !important;

    background: var(--twin-bg) !important;
    color: var(--twin-text) !important;
}


/* Prevent layout overflow */

.gradio-container .main,
.gradio-container .contain,
.gradio-container .wrap {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
}

.gradio-container * {
    min-width: 0;
}


/* ==========================================================
   HEADER
   ========================================================== */

.gradio-container h1 {
    position: relative;

    margin: 4px 0 10px !important;
    padding-left: 16px !important;

    color: var(--twin-text) !important;

    font-size: 28px !important;
    font-weight: 700 !important;
    line-height: 1.2 !important;

    letter-spacing: -0.03em !important;
    text-align: left !important;
}


/* Accent line */

.gradio-container h1::before {
    content: "";

    position: absolute;
    left: 0;
    top: 2px;
    bottom: 2px;

    width: 3px;

    background: linear-gradient(
        180deg,
        var(--twin-gold),
        var(--twin-purple)
    );
}


/* ==========================================================
   BLOCKS
   ========================================================== */

.block,
.form {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}


/* Sharp product-style UI */

.chatbot,
.chatbot *,
.block,
.form,
button,
input,
textarea,
.examples button {
    border-radius: 0 !important;
}


/* ==========================================================
   CHATBOT
   ========================================================== */

.chatbot,
.chatbot.block {
    min-height: 480px !important;

    background:
        linear-gradient(
            180deg,
            rgba(255, 255, 255, 0.015),
            rgba(255, 255, 255, 0)
        ),
        var(--twin-surface) !important;

    border: 1px solid var(--twin-border) !important;

    box-shadow:
        0 0 0 1px rgba(255, 255, 255, 0.01),
        0 18px 50px rgba(0, 0, 0, 0.18) !important;

    overflow: hidden !important;
}


/* Chatbot label/header */

.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
    display: none !important;
}


/* Placeholder */

.chatbot .placeholder,
.chatbot .placeholder * {
    color: var(--twin-muted) !important;
}


/* ==========================================================
   MESSAGE ROWS
   ========================================================== */

.message-row,
.message-row > div,
.message-row .role,
.message-wrap,
.bubble-wrap {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}


/* ==========================================================
   MESSAGE BUBBLES
   ========================================================== */

.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
    padding: 9px 12px !important;

    border: none !important;
    box-shadow: none !important;

    font-size: 14px !important;
    line-height: 1.6 !important;
}


/* --------------------------
   USER MESSAGE
   -------------------------- */

.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble,
.message-row[data-role="user"] .bubble {
    background: var(--twin-blue) !important;

    color: #ffffff !important;

    border-left: 2px solid var(--twin-gold) !important;
}


/* --------------------------
   ASSISTANT MESSAGE
   -------------------------- */

.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble,
.message-row[data-role="assistant"] .bubble {
    background: var(--twin-surface-2) !important;

    color: var(--twin-text) !important;

    border-left: 2px solid var(--twin-purple) !important;
}


/* Remove duplicate nested accent borders */

.message-row .message .message,
.message-row .message .bubble,
.message-row .message .message-bubble,
.message-row .bubble .message,
.message-row .bubble .bubble,
.message-row .bubble .message-bubble,
.message-row .message-bubble .message,
.message-row .message-bubble .bubble,
.message-row .message-bubble .message-bubble {
    border-left: none !important;
}


/* ==========================================================
   MESSAGE TYPOGRAPHY
   ========================================================== */

.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
    margin: 0 0 8px !important;

    color: inherit !important;

    font-size: 14px !important;
    line-height: 1.6 !important;
}

.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child {
    margin-bottom: 0 !important;
}


/* Remove unwanted nested styling */

.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * {
    box-shadow: none !important;
    color: inherit !important;
}


/* Links */

.message-row .message a,
.message-row .message-bubble a,
.message-row .bubble a {
    color: var(--twin-gold) !important;
    text-decoration: underline;
    text-underline-offset: 3px;
}


/* Bold text */

.message-row strong,
.message-row b {
    color: inherit !important;
    font-weight: 650 !important;
}


/* ==========================================================
   INPUT AREA
   ========================================================== */

.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] {
    align-items: stretch !important;
}


/* Text input */

textarea,
input[type="text"] {
    min-height: 50px !important;

    padding: 13px 15px !important;

    background: var(--twin-surface) !important;

    border: 1px solid var(--twin-border) !important;

    color: var(--twin-text) !important;

    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif !important;

    font-size: 14px !important;
    line-height: 1.5 !important;

    transition:
        border-color 0.15s ease,
        box-shadow 0.15s ease !important;
}


/* Input focus */

textarea:focus,
input[type="text"]:focus {
    border-color: var(--twin-gold) !important;

    outline: none !important;

    box-shadow:
        0 0 0 1px var(--twin-gold),
        0 0 18px rgba(245, 184, 46, 0.08) !important;
}


/* Placeholder */

textarea::placeholder,
input::placeholder {
    color: var(--twin-muted) !important;
}


/* ==========================================================
   BUTTONS
   ========================================================== */

button {
    min-height: 50px !important;

    padding: 0 17px !important;

    background: transparent !important;

    border: 1px solid var(--twin-border) !important;

    color: var(--twin-text) !important;

    font-family:
        "JetBrains Mono",
        "SF Mono",
        Menlo,
        monospace !important;

    font-size: 11px !important;
    font-weight: 600 !important;

    letter-spacing: 0.11em !important;
    text-transform: uppercase !important;

    cursor: pointer !important;

    transition:
        background 0.15s ease,
        color 0.15s ease,
        border-color 0.15s ease,
        transform 0.15s ease !important;
}


/* Button hover */

button:hover {
    border-color: var(--twin-gold) !important;
    color: var(--twin-gold) !important;
}


/* ==========================================================
   PRIMARY / SEND BUTTON
   ========================================================== */

button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
    min-height: 50px !important;

    padding: 0 16px !important;

    background: var(--twin-gold) !important;

    border: 1px solid var(--twin-gold) !important;

    color: #111111 !important;

    display: inline-flex !important;

    align-items: center !important;
    justify-content: center !important;

    box-shadow: none !important;
}


/* Primary hover */

button.primary:hover,
button[variant="primary"]:hover,
button.submit:hover,
button.submit-button:hover,
.submit-button:hover,
button.lg.primary:hover {
    background: #ffc84d !important;

    border-color: #ffc84d !important;

    color: #111111 !important;

    transform: translateY(-1px);
}


/* Send icon */

button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {
    width: 18px !important;
    height: 18px !important;

    margin: 0 !important;

    color: #111111 !important;

    fill: currentColor !important;
    stroke: currentColor !important;
}


/* ==========================================================
   EXAMPLES
   ========================================================== */

.examples,
.examples-holder,
[data-testid="examples"] {
    margin-top: 16px !important;
    padding: 0 !important;

    background: transparent !important;
}


/* Example container */

.examples table,
.examples-table {
    background: transparent !important;

    border: none !important;
}


/* Example buttons */

.examples button,
.example,
.examples td button,
[data-testid="examples"] button {
    min-height: 0 !important;

    padding: 10px 13px !important;

    background: var(--twin-surface) !important;

    border: 1px solid var(--twin-border) !important;

    color: var(--twin-muted) !important;

    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif !important;

    font-size: 13px !important;
    font-weight: 400 !important;

    letter-spacing: 0 !important;
    text-transform: none !important;

    text-align: left !important;

    transition:
        color 0.15s ease,
        border-color 0.15s ease,
        background 0.15s ease !important;
}


/* Example hover */

.examples button:hover,
.example:hover,
[data-testid="examples"] button:hover {
    background: var(--twin-surface-2) !important;

    border-color: var(--twin-blue) !important;

    color: var(--twin-blue) !important;
}


/* ==========================================================
   ICON BUTTONS
   ========================================================== */

.icon-button,
.chatbot .icon-button {
    min-height: 0 !important;

    padding: 5px !important;

    background: transparent !important;

    border: none !important;

    color: var(--twin-muted) !important;
}


.icon-button:hover,
.chatbot .icon-button:hover {
    background: transparent !important;

    border: none !important;

    color: var(--twin-gold) !important;
}


/* ==========================================================
   SCROLLBAR
   ========================================================== */

::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: var(--twin-bg);
}

::-webkit-scrollbar-thumb {
    background: var(--twin-border-strong);
}

::-webkit-scrollbar-thumb:hover {
    background: var(--twin-purple);
}


/* ==========================================================
   TEXT SELECTION
   ========================================================== */

::selection {
    background: var(--twin-gold);
    color: #111111;
}


/* ==========================================================
   MOBILE
   ========================================================== */

@media (max-width: 640px) {

    .gradio-container {
        padding: 24px 14px 36px !important;
    }

    .gradio-container h1 {
        font-size: 23px !important;
    }

    .chatbot,
    .chatbot.block {
        min-height: 430px !important;
    }

    textarea,
    input[type="text"] {
        font-size: 13px !important;
    }

    .examples button,
    .example,
    [data-testid="examples"] button {
        font-size: 12px !important;
    }
}
"""


# ============================================================
# JavaScript
# ============================================================

JS = """
() => {

    /* Browser tab title */
    document.title = "AI Digital Twin | Ahmed Taha";


    /* Focus the chat input */
    const focusInput = () => {

        const areas = document.querySelectorAll("textarea");

        if (areas.length > 0) {
            const area = areas[areas.length - 1];

            if (!area.disabled && !area.readOnly) {
                area.focus();
            }
        }
    };


    /* Initial focus */
    setTimeout(focusInput, 400);


    /* Keep track of textareas */
    const watchTextarea = (area) => {

        if (area.dataset.twinWatched) {
            return;
        }

        area.dataset.twinWatched = "1";

        let wasDisabled =
            area.disabled ||
            area.readOnly;


        const observer = new MutationObserver(() => {

            const isDisabled =
                area.disabled ||
                area.readOnly;


            /*
             * Gradio disables the input while the model
             * is generating a response.
             *
             * Once it becomes available again,
             * automatically focus it.
             */

            if (wasDisabled && !isDisabled) {
                setTimeout(() => area.focus(), 50);
            }


            wasDisabled = isDisabled;
        });


        observer.observe(area, {
            attributes: true,
            attributeFilter: [
                "disabled",
                "readonly"
            ]
        });
    };


    /* Find textareas */
    const scan = () => {

        document
            .querySelectorAll("textarea")
            .forEach(watchTextarea);
    };


    /* Initial scan */
    setTimeout(scan, 500);


    /*
     * Gradio dynamically changes the DOM,
     * so keep watching for new elements.
     */

    new MutationObserver(scan).observe(
        document.body,
        {
            childList: true,
            subtree: true
        }
    );
}
"""