# ========================================
# STUDYBOT - CHATBOT
# Person 2: Chatbot / User Interaction
# ========================================

from data import subjects


# ========================================
# GET AI DATA
# ========================================

ai_data = subjects["AI"]


# ========================================
# HEADER
# ========================================

def show_header():
    print("\n" + "=" * 50)
    print("                 🤖 STUDYBOT")
    print("              Academic Assistant")
    print("=" * 50)


# ========================================
# MAIN MENU
# ========================================

def show_menu():
    print("\nWhat would you like to do?")
    print("1. Ask a question")
    print("2. View syllabus")
    print("3. View exams")
    print("4. View practicals")
    print("5. View assignments")
    print("6. Exit")


# ========================================
# OPTION 2 - VIEW SYLLABUS
# ========================================

def view_syllabus():
    syllabus = ai_data["syllabus"]

    print("\n" + "=" * 50)
    print("        📚 ARTIFICIAL INTELLIGENCE SYLLABUS")
    print("=" * 50)

    for module, details in syllabus.items():

        print(f"\n{module}: {details['title']}")
        print("-" * 50)

        for topic, points in details["topics"].items():

            print(f"\n{topic}")

            for point in points:
                print(f"   • {point}")

        print(f"\nStatus: {details['status']}")

    print("\n" + "=" * 50)


# ========================================
# OPTION 3 - VIEW EXAMS
# ========================================

def view_exams():
    exam = ai_data["exam"]
    evaluation = ai_data["evaluation"]

    print("\n" + "=" * 50)
    print("              📝 EXAM INFORMATION")
    print("=" * 50)

    print(f"\nCourse Name : {ai_data['course_name']}")
    print(f"Course Code : {ai_data['course_code']}")
    print(f"Exam Date   : {exam['date']}")

    print("\nEvaluation Scheme")
    print("-" * 50)

    print(
        f"CIA Activity                : "
        f"{evaluation['CIA']['Activity']} marks"
    )

    print(
        f"CIA Test                    : "
        f"{evaluation['CIA']['Test']} marks"
    )

    print(
        f"CIA Attendance              : "
        f"{evaluation['CIA']['Attendance']} marks"
    )

    print(
        f"CIA Total                   : "
        f"{evaluation['CIA']['Total']} marks"
    )

    print(
        f"Mid Semester Examination    : "
        f"{evaluation['Mid Semester Examination']} marks"
    )

    print(
        f"End Semester Examination    : "
        f"{evaluation['End Semester Examination']} marks"
    )

    print("\n" + "=" * 50)


# ========================================
# OPTION 4 - VIEW PRACTICALS
# ========================================

def view_practicals():
    practicals = ai_data["practicals"]

    print("\n" + "=" * 50)
    print("            🔬 PRACTICAL INFORMATION")
    print("=" * 50)

    print(f"\nStatus: {practicals['status']}")

    print("\n" + "=" * 50)


# ========================================
# OPTION 5 - VIEW ASSIGNMENTS
# ========================================

def view_assignments():
    assignments = ai_data["assignments"]

    print("\n" + "=" * 50)
    print("            📋 ASSIGNMENT INFORMATION")
    print("=" * 50)

    print(f"\nStatus: {assignments['status']}")

    print("\n" + "=" * 50)


# ========================================
# FIND MODULE
# ========================================

def find_module(question):
    syllabus = ai_data["syllabus"]

    for module in syllabus:

        if module.lower() in question:
            return module

    return None


# ========================================
# FIND TOPIC
# ========================================

def find_topic(question):
    syllabus = ai_data["syllabus"]

    for module, details in syllabus.items():

        for topic, points in details["topics"].items():

            # Check topic heading
            if topic.lower() in question:
                return module, topic, points

            # Check individual topic points
            for point in points:

                if point.lower() in question:
                    return module, topic, points

    return None


# ========================================
# OPTION 1 - ASK A QUESTION
# ========================================

def ask_question():

    print("\n" + "=" * 50)
    print("                 ❓ ASK A QUESTION")
    print("=" * 50)

    question = input("\nYou: ").lower().strip()

    # ------------------------------------
    # EMPTY QUESTION
    # ------------------------------------

    if not question:
        print("StudyBot: Please enter a question.")
        return

    # ------------------------------------
    # GREETINGS
    # ------------------------------------

    if question in ["hi", "hello", "hey", "hii", "good morning",
                    "good afternoon", "good evening"]:

        print(
            "StudyBot: Hello! 😊 "
            "How can I help you with your AI course?"
        )
        return

    # ------------------------------------
    # COURSE CODE
    # ------------------------------------

    if "course code" in question:

        print(
            f"StudyBot: The course code is "
            f"{ai_data['course_code']}."
        )
        return

    # ------------------------------------
    # COURSE NAME
    # ------------------------------------

    if (
        "course name" in question
        or "subject name" in question
        or "what subject" in question
    ):

        print(
            f"StudyBot: The course is "
            f"{ai_data['course_name']}."
        )
        return

    # ------------------------------------
    # EXAM DATE
    # ------------------------------------

    if (
        ("exam" in question or "examination" in question)
        and (
            "when" in question
            or "date" in question
            or "schedule" in question
        )
    ):

        print(
            f"StudyBot: Your AI theory exam is on "
            f"{ai_data['exam']['date']}."
        )
        return

    # ------------------------------------
    # EXAM GENERAL QUESTION
    # ------------------------------------

    if "exam" in question or "examination" in question:

        print(
            f"StudyBot: Your AI theory exam is on "
            f"{ai_data['exam']['date']}."
        )
        return

    # ------------------------------------
    # EVALUATION / MARKS
    # ------------------------------------

    if (
        "marks" in question
        or "evaluation" in question
        or "cia" in question
        or "mid semester" in question
        or "end semester" in question
    ):

        evaluation = ai_data["evaluation"]

        print("\nStudyBot: Evaluation Scheme")

        print(
            f"CIA Activity: "
            f"{evaluation['CIA']['Activity']} marks"
        )

        print(
            f"CIA Test: "
            f"{evaluation['CIA']['Test']} marks"
        )

        print(
            f"CIA Attendance: "
            f"{evaluation['CIA']['Attendance']} marks"
        )

        print(
            f"CIA Total: "
            f"{evaluation['CIA']['Total']} marks"
        )

        print(
            f"Mid Semester Examination: "
            f"{evaluation['Mid Semester Examination']} marks"
        )

        print(
            f"End Semester Examination: "
            f"{evaluation['End Semester Examination']} marks"
        )

        return

    # ------------------------------------
    # PRACTICAL
    # ------------------------------------

    if "practical" in question or "lab" in question:

        print(
            f"StudyBot: "
            f"{ai_data['practicals']['status']}."
        )
        return

    # ------------------------------------
    # ASSIGNMENT
    # ------------------------------------

    if "assignment" in question:

        print(
            f"StudyBot: "
            f"{ai_data['assignments']['status']}."
        )
        return

    # ------------------------------------
    # MODULE QUESTION
    # ------------------------------------

    module = find_module(question)

    if module:

        syllabus = ai_data["syllabus"]

        # Module name / title question
        if (
            "name" in question
            or "title" in question
            or "about" in question
        ):

            print(
                f"StudyBot: {module} is "
                f"'{syllabus[module]['title']}'."
            )

            return

        # Complete module details
        print(
            f"\nStudyBot: {module} - "
            f"{syllabus[module]['title']}"
        )

        for topic, points in syllabus[module]["topics"].items():

            print(f"\n{topic}")

            for point in points:
                print(f"   • {point}")

        print(
            f"\nStatus: {syllabus[module]['status']}"
        )

        return

    # ------------------------------------
    # SPECIFIC TOPIC QUESTION
    # ------------------------------------

    topic_result = find_topic(question)

    if topic_result:

        module, topic, points = topic_result

        print(
            f"\nStudyBot: {topic}"
        )

        print(f"Module: {module}")

        for point in points:
            print(f"   • {point}")

        return

    # ------------------------------------
    # GENERAL SYLLABUS QUESTION
    # ------------------------------------

    if (
        "syllabus" in question
        or "modules" in question
        or "topics" in question
    ):

        print(
            "StudyBot: The AI syllabus contains "
            "6 modules:"
        )

        for module, details in ai_data["syllabus"].items():

            print(
                f"   • {module}: "
                f"{details['title']}"
            )

        return

    # ------------------------------------
    # UNKNOWN QUESTION
    # ------------------------------------

    print(
        "StudyBot: Sorry, I couldn't understand "
        "your question."
    )

    print(
        "You can ask about the course code, "
        "course name, exam, marks, syllabus, "
        "modules, practicals, or assignments."
    )


# ========================================
# MAIN PROGRAM
# ========================================

def main():

    show_header()

    while True:

        show_menu()

        choice = input("\nEnter your choice (1-6): ").strip()

        # --------------------------------
        # OPTION 1
        # --------------------------------

        if choice == "1":
            ask_question()

        # --------------------------------
        # OPTION 2
        # --------------------------------

        elif choice == "2":
            view_syllabus()

        # --------------------------------
        # OPTION 3
        # --------------------------------

        elif choice == "3":
            view_exams()

        # --------------------------------
        # OPTION 4
        # --------------------------------

        elif choice == "4":
            view_practicals()

        # --------------------------------
        # OPTION 5
        # --------------------------------

        elif choice == "5":
            view_assignments()

        # --------------------------------
        # OPTION 6
        # --------------------------------

        elif choice == "6":

            print(
                "\nStudyBot: Goodbye! "
                "Good luck with your studies! 📚"
            )

            break

        # --------------------------------
        # INVALID OPTION
        # --------------------------------

        else:

            print(
                "\nStudyBot: Please enter a number "
                "from 1 to 6."
            )


# ========================================
# START PROGRAM
# ========================================

if __name__ == "__main__":
    main()