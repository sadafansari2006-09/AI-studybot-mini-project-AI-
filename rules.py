# ========================================
# STUDYBOT - RULES / REASONING
# Person 3: Rule-Based Chatbot Logic
# ========================================

from data import subjects


# ========================================
# GET AI DATA
# ========================================

ai_data = subjects["AI"]


# ========================================
# 1. GET THEORY SYLLABUS
# ========================================

def get_theory_syllabus():
    """Return the complete AI theory syllabus."""

    syllabus = ai_data["syllabus"]

    response = "\n===== AI THEORY SYLLABUS =====\n"

    for module_name, module in syllabus.items():

        response += (
            f"\n{module_name}: "
            f"{module['title']}\n"
        )

        for topic, points in module["topics"].items():

            response += f"\n  {topic}\n"

            for point in points:
                response += f"    • {point}\n"

        response += (
            f"  Status: {module['status']}\n"
        )

    return response


# ========================================
# 2. GET PRACTICAL INFORMATION
# ========================================

def get_practical_syllabus():
    """Return AI practical information."""

    practicals = ai_data["practicals"]

    response = "\n===== AI PRACTICALS =====\n"

    response += (
        f"\nStatus: {practicals['status']}\n"
    )

    return response


# ========================================
# 3. GET EXAM INFORMATION
# ========================================

def get_exams():
    """Return AI examination information."""

    exam = ai_data["exam"]
    evaluation = ai_data["evaluation"]

    response = "\n===== AI EXAMS =====\n"

    response += (
        f"\nCourse: {ai_data['course_name']}\n"
        f"Course Code: {ai_data['course_code']}\n"
        f"Theory Exam Date: {exam['date']}\n"
    )

    response += "\nEvaluation Scheme:\n"

    response += (
        f"  CIA Activity: "
        f"{evaluation['CIA']['Activity']} marks\n"
    )

    response += (
        f"  CIA Test: "
        f"{evaluation['CIA']['Test']} marks\n"
    )

    response += (
        f"  CIA Attendance: "
        f"{evaluation['CIA']['Attendance']} marks\n"
    )

    response += (
        f"  CIA Total: "
        f"{evaluation['CIA']['Total']} marks\n"
    )

    response += (
        f"  Mid Semester Examination: "
        f"{evaluation['Mid Semester Examination']} marks\n"
    )

    response += (
        f"  End Semester Examination: "
        f"{evaluation['End Semester Examination']} marks\n"
    )

    return response


# ========================================
# 4. SEARCH FOR A THEORY TOPIC
# ========================================

def search_theory_topic(question):
    """
    Search for a topic or keyword from the
    AI syllabus.
    """

    question = question.lower().strip()

    syllabus = ai_data["syllabus"]

    for module_name, module in syllabus.items():

        for topic, points in module["topics"].items():

            # --------------------------------
            # Check complete topic name
            # --------------------------------

            topic_lower = topic.lower()

            if topic_lower in question:

                response = (
                    f"\n📚 {module_name}: "
                    f"{module['title']}\n\n"
                    f"{topic}\n"
                )

                for point in points:
                    response += (
                        f"  • {point}\n"
                    )

                return response

            # --------------------------------
            # Check individual syllabus points
            # --------------------------------

            for point in points:

                point_lower = point.lower()

                # Exact match
                if point_lower in question:

                    return (
                        f"\n📚 {module_name}: "
                        f"{module['title']}\n\n"
                        f"{topic}\n"
                        f"  • {point}"
                    )

                # --------------------------------
                # Keyword matching
                # --------------------------------

                words = [
                    word.strip(
                        ".,!?()[]{}:;/-"
                    )
                    for word in point_lower.split()
                ]

                important_words = [
                    word
                    for word in words
                    if len(word) >= 4
                ]

                for word in important_words:

                    if word in question:

                        return (
                            f"\n📚 {module_name}: "
                            f"{module['title']}\n\n"
                            f"{topic}\n"
                            f"  • {point}"
                        )

    return None


# ========================================
# 5. FIND A MODULE
# ========================================

def search_module(question):
    """
    Identify whether the user is asking
    about a particular module.
    """

    question = question.lower().strip()

    syllabus = ai_data["syllabus"]

    for module_name, module in syllabus.items():

        module_number = module_name.split()[-1]

        # Examples:
        # module 1
        # module 2
        # module 3

        if (
            f"module {module_number}" in question
            or f"module{module_number}" in question
        ):

            response = (
                f"\n📚 {module_name}: "
                f"{module['title']}\n"
            )

            for topic, points in module["topics"].items():

                response += (
                    f"\n{topic}\n"
                )

                for point in points:

                    response += (
                        f"  • {point}\n"
                    )

            response += (
                f"\nStatus: {module['status']}\n"
            )

            return response

    return None


# ========================================
# 6. IDENTIFY USER INTENT
# ========================================

def identify_intent(question):
    """
    Identify the purpose of the user's
    question using keyword-based rules.
    """

    question = question.lower().strip()


    # ------------------------------------
    # EXIT
    # ------------------------------------

    if any(
        word in question
        for word in [
            "exit",
            "quit",
            "bye"
        ]
    ):

        return "exit"


    # ------------------------------------
    # GREETING
    # ------------------------------------

    if any(
        word in question
        for word in [
            "hello",
            "hi",
            "hey",
            "hii"
        ]
    ):

        return "greeting"


    # ------------------------------------
    # HELP
    # ------------------------------------

    if "help" in question:

        return "help"


    # ------------------------------------
    # EXAM
    # ------------------------------------

    if any(
        word in question
        for word in [
            "exam",
            "examination",
            "test",
            "paper"
        ]
    ):

        return "exam"


    # ------------------------------------
    # PRACTICAL
    # ------------------------------------

    if any(
        word in question
        for word in [
            "practical",
            "lab",
            "experiment"
        ]
    ):

        return "practical"


    # ------------------------------------
    # ASSIGNMENT
    # ------------------------------------

    if "assignment" in question:

        return "assignment"


    # ------------------------------------
    # MARKS / EVALUATION
    # ------------------------------------

    if any(
        word in question
        for word in [
            "marks",
            "evaluation",
            "cia"
        ]
    ):

        return "evaluation"


    # ------------------------------------
    # COURSE CODE
    # ------------------------------------

    if "course code" in question:

        return "course_code"


    # ------------------------------------
    # COURSE NAME
    # ------------------------------------

    if (
        "course name" in question
        or "subject name" in question
    ):

        return "course_name"


    # ------------------------------------
    # SYLLABUS / MODULE
    # ------------------------------------

    if any(
        word in question
        for word in [
            "syllabus",
            "module",
            "modules",
            "topic",
            "unit"
        ]
    ):

        return "syllabus"


    # ------------------------------------
    # SPECIFIC SYLLABUS TOPIC
    # ------------------------------------

    if search_theory_topic(question) is not None:

        return "syllabus"


    # ------------------------------------
    # UNKNOWN
    # ------------------------------------

    return "unknown"


# ========================================
# 7. ANSWER USER QUESTION
# ========================================

def answer_question(question):
    """
    Main rule-based reasoning function.

    Takes the user's question,
    identifies its intent,
    accesses data.py,
    and returns the answer.
    """

    intent = identify_intent(question)


    # ------------------------------------
    # GREETING
    # ------------------------------------

    if intent == "greeting":

        return (
            "Hello! 👋\n"
            "I am StudyBot, your AI academic "
            "assistant.\n"
            "How can I help you?"
        )


    # ------------------------------------
    # HELP
    # ------------------------------------

    elif intent == "help":

        return (
            "\nYou can ask me things like:\n\n"
            "- What is the course code?\n"
            "- What is the course name?\n"
            "- When is my AI exam?\n"
            "- Show me the AI syllabus.\n"
            "- What is in Module 3?\n"
            "- What is robotics?\n"
            "- Is A* algorithm in the syllabus?\n"
            "- What are the practicals?\n"
            "- What are the assignments?\n"
            "- How many marks is the CIA?\n"
        )


    # ------------------------------------
    # EXIT
    # ------------------------------------

    elif intent == "exit":

        return (
            "Goodbye! 👋\n"
            "Good luck with your studies!"
        )


    # ------------------------------------
    # COURSE CODE
    # ------------------------------------

    elif intent == "course_code":

        return (
            f"The course code is "
            f"{ai_data['course_code']}."
        )


    # ------------------------------------
    # COURSE NAME
    # ------------------------------------

    elif intent == "course_name":

        return (
            f"The course is "
            f"{ai_data['course_name']}."
        )


    # ------------------------------------
    # EXAM
    # ------------------------------------

    elif intent == "exam":

        return get_exams()


    # ------------------------------------
    # PRACTICAL
    # ------------------------------------

    elif intent == "practical":

        return get_practical_syllabus()


    # ------------------------------------
    # ASSIGNMENT
    # ------------------------------------

    elif intent == "assignment":

        return (
            "\n===== AI ASSIGNMENTS =====\n\n"
            f"Status: "
            f"{ai_data['assignments']['status']}"
        )


    # ------------------------------------
    # EVALUATION
    # ------------------------------------

    elif intent == "evaluation":

        evaluation = ai_data["evaluation"]

        return (
            "\n===== EVALUATION =====\n\n"
            f"CIA Activity: "
            f"{evaluation['CIA']['Activity']} marks\n"
            f"CIA Test: "
            f"{evaluation['CIA']['Test']} marks\n"
            f"CIA Attendance: "
            f"{evaluation['CIA']['Attendance']} marks\n"
            f"CIA Total: "
            f"{evaluation['CIA']['Total']} marks\n"
            f"Mid Semester Examination: "
            f"{evaluation['Mid Semester Examination']} marks\n"
            f"End Semester Examination: "
            f"{evaluation['End Semester Examination']} marks\n"
        )


    # ------------------------------------
    # SYLLABUS
    # ------------------------------------

    elif intent == "syllabus":

        # First check a specific module

        module_result = search_module(question)

        if module_result:

            return module_result


        # Then check a specific topic

        topic_result = search_theory_topic(question)

        if topic_result:

            return topic_result


        # Otherwise return complete syllabus

        return get_theory_syllabus()


    # ------------------------------------
    # UNKNOWN
    # ------------------------------------

    else:

        return (
            "Sorry, I don't understand "
            "that question yet.\n\n"
            "Try asking about:\n"
            "- Course information\n"
            "- AI syllabus\n"
            "- Modules\n"
            "- Exams\n"
            "- Practicals\n"
            "- Assignments\n"
            "- Marks"
        )