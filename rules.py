from knowledge_base import theory_syllabus, practical_syllabus, exams

# 1. GET THEORY SYLLABUS
def get_theory_syllabus():
    """Returns the complete AI theory syllabus."""

    response = "\n===== AI THEORY SYLLABUS =====\n"

    for module_no, module in theory_syllabus.items():
        response += f"\nModule {module_no}: {module['title']}\n"

        for topic in module["topics"]:
            response += f"  {topic}\n"

    return response


# 2. GET PRACTICAL SYLLABUS
def get_practical_syllabus():
    """Returns the complete AI practical/lab syllabus."""

    response = "\n===== AI PRACTICAL SYLLABUS =====\n"

    for practical_no, practical in practical_syllabus.items():
        response += f"\nPractical {practical_no}: {practical['title']}\n"

        for topic in practical["topics"]:
            response += f"  {topic}\n"

    return response


# 3. GET EXAM INFORMATION
def get_exams():
    """Returns available AI theory and practical exam information."""

    response = "\n===== AI EXAMS =====\n"

    for exam_type, exam_info in exams.items():
        response += f"\n{exam_type}: {exam_info['date']}\n"
        response += f"Time: {exam_info['time']}\n"

    return response

# 4. FIND A TOPIC IN THEORY SYLLABUS
def search_theory_topic(question):
    """Searches for a topic mentioned in the user's question."""

    question = question.lower()

    for module_no, module in theory_syllabus.items():

        for topic in module["topics"]:

            if topic.lower() in question:
                return (f"Yes, '{topic}' is part of Module {module_no}: {module['title']}.")

    return None

# 5. FIND A MODULE

def search_module(question):
    """Identifies whether the user is asking about a particular module."""

    question = question.lower()

    for module_no, module in theory_syllabus.items():

        # Examples: "module 3", "module three"
        if f"module {module_no}" in question:
            response = (
                f"\nModule {module_no}: {module['title']}\n"
            )

            for topic in module["topics"]:
                response += f"  - {topic}\n"

            return response

    return None


# 6. IDENTIFY USER INTENT

def identify_intent(question):
    """Identifies the purpose of the user's question using simple keyword-based rules."""

    question = question.lower()

    # Exam-related questions
    if any(word in question for word in ["exam", "examination", "test", "paper"]):
        return "exam"

    # Practical-related questions
    elif any(word in question for word in ["practical", "lab", "experiment"]):
        return "practical"

    # Syllabus-related questions
    elif any(word in question for word in["syllabus", "module", "topic", "unit"]):
        return "syllabus"

    # Greeting
    elif any(word in question for word in ["hello", "hi", "hey"]):
        return "greeting"

    # Help
    elif "help" in question:
        return "help"

    # Exit
    elif any(word in question for word in ["exit", "quit", "bye"]):
        return "exit"

    return "unknown"


# 7. ANSWER USER'S QUESTION

def answer_question(question):
    """Main rule-based reasoning function.
    Takes the user's question, identifies the intent, and returns an appropriate response."""

    intent = identify_intent(question)

    # Rule 1: Greeting
    if intent == "greeting":
        return "Hello! I am StudyBot. How can I help you with AI?"

    # Rule 2: Help
    elif intent == "help":
        return (
            "\nYou can ask me things like:\n"
            "- When is my AI exam?\n"
            "- Show me the AI syllabus.\n"
            "- What is in Module 3?\n"
            "- What are the AI practicals?\n"
            "- Is A* algorithm in the syllabus?\n"
        )

    # Rule 3: Exit
    elif intent == "exit":
        return "Goodbye! Hope you slayyy!"

    # Rule 4: Exam question
    elif intent == "exam":
        return get_exams()

    # Rule 5: Practical question
    elif intent == "practical":
        return get_practical_syllabus()

    # Rule 6: Syllabus question
    elif intent == "syllabus":
        # First check if the user asked about aparticular module.
        module_result = search_module(question)

        if module_result:
            return module_result

        # Otherwise show the complete syllabus.
        return get_theory_syllabus()

    # Rule 7: Unknown question
    else:
        return (
            "Sorry, I don't understand that question yet.\n"
            "Try asking about the AI syllabus, modules, practicals, or exams."
        )