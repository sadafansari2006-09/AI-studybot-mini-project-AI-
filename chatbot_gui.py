# ========================================
# STUDYBOT - GUI
# Person 2: Graphical User Interface
# ========================================

import tkinter as tk
from tkinter import scrolledtext

from chatbot import ai_data
from rules import (
    answer_question,
    get_theory_syllabus,
    get_exams,
    get_practical_syllabus,
)


# ========================================
# COLORS - PINK THEME
# ========================================

BG = "#fff0f6"
SIDEBAR = "#f7c8dc"
CHAT_BG = "#fff8fb"
CARD = "#fde3ee"
TEXT = "#3d2433"
MUTED = "#7d5368"
ACCENT = "#e5487f"
ACCENT_HOVER = "#c93668"
BORDER = "#e7a8c0"


# ========================================
# WINDOW
# ========================================

root = tk.Tk()

root.title("StudyBot - Academic Assistant")
root.geometry("1100x700")
root.minsize(900, 600)

root.configure(bg=BG)


# ========================================
# ADD MESSAGE
# ========================================

def add_message(message, sender="StudyBot", user=False):

    chat_box.configure(state="normal")

    if user:

        chat_box.insert(
            tk.END,
            "\nYou\n",
            "user_name"
        )

        chat_box.insert(
            tk.END,
            message + "\n",
            "user_text"
        )

    else:

        chat_box.insert(
            tk.END,
            "\nStudyBot\n",
            "bot_name"
        )

        chat_box.insert(
            tk.END,
            message + "\n",
            "bot_text"
        )

    chat_box.configure(state="disabled")

    chat_box.see(tk.END)


# ========================================
# SEND QUESTION
# ========================================

def send_question(event=None):

    question = input_box.get(
        "1.0",
        tk.END
    ).strip()

    if not question:
        return

    # Remove placeholder
    if question == "Ask something about your AI course...":
        return

    # Show user message
    add_message(
        question,
        sender="You",
        user=True
    )

    # Send question to REAL chatbot logic
    response = answer_question(question)

    # Show chatbot response
    add_message(
        response
    )

    input_box.delete(
        "1.0",
        tk.END
    )

    input_box.focus()


# ========================================
# CLEAR CHAT
# ========================================

def clear_chat():

    chat_box.configure(state="normal")
    chat_box.delete("1.0", tk.END)
    chat_box.configure(state="disabled")

    add_message(
        "Chat cleared! 😊\n\n"
        "What would you like to know about your AI course?"
    )


# ========================================
# VIEW SYLLABUS
# ========================================

def show_syllabus():

    response = get_theory_syllabus()

    add_message(response)


# ========================================
# VIEW EXAMS
# ========================================

def show_exams():

    response = get_exams()

    add_message(response)


# ========================================
# VIEW PRACTICALS
# ========================================

def show_practicals():

    response = get_practical_syllabus()

    add_message(response)


# ========================================
# VIEW ASSIGNMENTS
# ========================================

def show_assignments():

    response = (
        "===== AI ASSIGNMENTS =====\n\n"
        f"Status: "
        f"{ai_data['assignments']['status']}"
    )

    add_message(response)


# ========================================
# SIDEBAR
# ========================================

sidebar = tk.Frame(
    root,
    bg=SIDEBAR,
    width=250
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


# Logo

tk.Label(
    sidebar,
    text="🤖",
    font=("Segoe UI Emoji", 34),
    bg=SIDEBAR,
    fg=TEXT
).pack(
    anchor="w",
    padx=25,
    pady=(30, 0)
)


tk.Label(
    sidebar,
    text="StudyBot",
    font=("Segoe UI", 23, "bold"),
    bg=SIDEBAR,
    fg=TEXT
).pack(
    anchor="w",
    padx=25
)


tk.Label(
    sidebar,
    text="Academic Assistant",
    font=("Segoe UI", 10),
    bg=SIDEBAR,
    fg=MUTED
).pack(
    anchor="w",
    padx=25,
    pady=(2, 25)
)


# Divider

tk.Frame(
    sidebar,
    bg=BORDER,
    height=1
).pack(
    fill="x",
    padx=20
)


# Menu label

tk.Label(
    sidebar,
    text="MENU",
    font=("Segoe UI", 9, "bold"),
    bg=SIDEBAR,
    fg=MUTED
).pack(
    anchor="w",
    padx=25,
    pady=(25, 10)
)


# ========================================
# SIDEBAR BUTTON
# ========================================

def create_sidebar_button(
    text,
    command,
    active=False
):

    button = tk.Button(
        sidebar,
        text=text,
        command=command,
        font=("Segoe UI", 11),
        bg=CARD if active else SIDEBAR,
        fg=TEXT,
        activebackground=CARD,
        activeforeground=TEXT,
        relief="flat",
        bd=0,
        anchor="w",
        padx=20,
        pady=12,
        cursor="hand2"
    )

    button.pack(
        fill="x",
        padx=12,
        pady=2
    )


# Buttons

create_sidebar_button(
    "💬   Chat",
    lambda: input_box.focus(),
    active=True
)

create_sidebar_button(
    "📚   View Syllabus",
    show_syllabus
)

create_sidebar_button(
    "📝   View Exams",
    show_exams
)

create_sidebar_button(
    "🔬   Practicals",
    show_practicals
)

create_sidebar_button(
    "📋   Assignments",
    show_assignments
)

create_sidebar_button(
    "🧹   Clear Chat",
    clear_chat
)


# Online status

tk.Label(
    sidebar,
    text="●  StudyBot is online",
    font=("Segoe UI", 9),
    bg=SIDEBAR,
    fg="#d43d73"
).pack(
    side="bottom",
    anchor="w",
    padx=25,
    pady=25
)


# ========================================
# MAIN AREA
# ========================================

main = tk.Frame(
    root,
    bg=BG
)

main.pack(
    side="left",
    fill="both",
    expand=True
)


# ========================================
# TOP HEADER
# ========================================

header = tk.Frame(
    main,
    bg=BG
)

header.pack(
    fill="x",
    padx=30,
    pady=(25, 15)
)


tk.Label(
    header,
    text="AI Academic Assistant",
    font=("Segoe UI", 21, "bold"),
    bg=BG,
    fg=TEXT
).pack(
    anchor="w"
)


tk.Label(
    header,
    text="Ask questions about your Artificial Intelligence course",
    font=("Segoe UI", 10),
    bg=BG,
    fg=MUTED
).pack(
    anchor="w",
    pady=(4, 0)
)


# ========================================
# CHAT AREA
# ========================================

chat_frame = tk.Frame(
    main,
    bg=CHAT_BG
)

chat_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=(0, 10)
)


chat_box = scrolledtext.ScrolledText(
    chat_frame,
    wrap=tk.WORD,
    font=("Segoe UI", 11),
    bg=CHAT_BG,
    fg=TEXT,
    insertbackground=TEXT,
    selectbackground=ACCENT,
    relief="flat",
    borderwidth=0,
    padx=25,
    pady=20
)

chat_box.pack(
    fill="both",
    expand=True
)


# Text colors

chat_box.tag_config(
    "user_name",
    foreground="#c92f67",
    font=("Segoe UI", 10, "bold")
)

chat_box.tag_config(
    "user_text",
    foreground=TEXT,
    font=("Segoe UI", 11)
)

chat_box.tag_config(
    "bot_name",
    foreground="#d43d73",
    font=("Segoe UI", 10, "bold")
)

chat_box.tag_config(
    "bot_text",
    foreground=TEXT,
    font=("Segoe UI", 11)
)

chat_box.configure(
    state="disabled"
)


# ========================================
# INPUT AREA
# ========================================

input_frame = tk.Frame(
    main,
    bg=BG
)

input_frame.pack(
    fill="x",
    padx=30,
    pady=(0, 25)
)


input_container = tk.Frame(
    input_frame,
    bg=CARD
)

input_container.pack(
    fill="x"
)


input_box = tk.Text(
    input_container,
    height=2,
    wrap=tk.WORD,
    font=("Segoe UI", 11),
    bg=CARD,
    fg=MUTED,
    insertbackground=TEXT,
    relief="flat",
    borderwidth=0,
    padx=15,
    pady=10
)

input_box.pack(
    side="left",
    fill="both",
    expand=True
)


# Placeholder

placeholder = "Ask something about your AI course..."

input_box.insert(
    "1.0",
    placeholder
)


def remove_placeholder(event):

    current = input_box.get(
        "1.0",
        tk.END
    ).strip()

    if current == placeholder:

        input_box.delete(
            "1.0",
            tk.END
        )

        input_box.config(
            fg=TEXT
        )


input_box.bind(
    "<FocusIn>",
    remove_placeholder
)


# ========================================
# SEND BUTTON
# ========================================

send_button = tk.Button(
    input_container,
    text="Send  ➤",
    command=send_question,
    font=("Segoe UI", 11, "bold"),
    bg=ACCENT,
    fg="white",
    activebackground=ACCENT_HOVER,
    activeforeground="white",
    relief="flat",
    bd=0,
    padx=22,
    pady=12,
    cursor="hand2"
)

send_button.pack(
    side="right",
    padx=10,
    pady=10
)


# ========================================
# ENTER KEY
# ========================================

def handle_enter(event):

    send_question()

    return "break"


input_box.bind(
    "<Return>",
    handle_enter
)


# ========================================
# WELCOME MESSAGE
# ========================================

add_message(
    "Hello! 👋\n\n"
    "I'm StudyBot, your AI Academic Assistant.\n\n"
    "You can ask me things like:\n"
    "• What is the course code?\n"
    "• When is my exam?\n"
    "• What is Module 3?\n"
    "• Is A* algorithm in the syllabus?\n"
    "• How many marks is the CIA?\n\n"
    "You can also use the options on the left."
)


# ========================================
# START GUI
# ========================================

root.mainloop()