# ========================================
# STUDYBOT - CHATBOT
# Person 2: Chatbot / User Interaction
# ========================================

from data import subjects


# ----------------------------------------
# GET AI DATA
# ----------------------------------------

ai_data = subjects["AI"]


# ----------------------------------------
# HEADER
# ----------------------------------------

def show_header():
    print("\n" + "=" * 50)
    print("🤖 STUDYBOT")
    print("      Academic Assistant")
    print("=" * 50)


# ----------------------------------------
# MENU
# ----------------------------------------

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
    syllabus = ai_data["theory_syllabus"]

    print("\n" + "=" * 50)
    print("📚 ARTIFICIAL INTELLIGENCE - THEORY SYLLABUS")
    print("=" * 50)

    for module, details in syllabus.items():

        print(f"\n{module}: {details['title']}")
        print("-" * 50)

        for topic, points in details["topics"].items():

            print(f"\n{topic}")

            for point in points:
                print(f"   • {point}")


# ========================================
# OPTION 3 - VIEW EXAMS
# ========================================

def view_exams():
    exam = ai_data["exam_details"]

    print("\n" + "=" * 50)
    print("📝 EXAM INFORMATION")
    print("=" * 50)

    print(f"\nCourse: {ai_data['course_name']}")
    print(f"Course Code: {ai_data['course_code']}")

    print("\nTheory Exam:")
    print(f"   Date: {exam['theory_exam']['date']}")

    print("\nEvaluation Scheme:")
    print(f"   CIA Activity: {exam['CIA']['Activity']} marks")
    print(f"   CIA Test: {exam['CIA']['Test']} marks")
    print(f"   CIA Attendance: {exam['CIA']['Attendance']} marks")
    print(f"   CIA Total: {exam['CIA']['Total']} marks")

    print(
        f"   Mid Semester Examination: "
        f"{exam['mid_semester_examination']['marks']} marks"
    )

    print(
        f"   End Semester Examination: "
        f"{exam['end_semester_examination']['marks']} marks"
    )


# ========================================
# OPTION 4 - VIEW PRACTICALS
# ========================================

def view_practicals():
    practical = ai_data["practical_syllabus"]

    print("\n" + "=" * 50)
    print("🔬 PRACTICAL INFORMATION")
    print("=" * 50)

    print(f"\n{practical['status']}")

    if not practical["practicals"]:
        return

    for experiment in practical["practicals"]:

        print(
            f"\nExperiment {experiment['number']}: "
            f"{experiment['title']}"
        )

        print(f"Description: {experiment['description']}")
        print(f"CO: {experiment['CO']}")
        print(f"BL: {experiment['BL']}")
        print(f"Hours: {experiment['hours']}")


# ========================================
# OPTION 5 - VIEW ASSIGNMENTS
# ========================================

def view_assignments():

    print("\n" + "=" * 50)
    print("📋 ASSIGNMENT INFORMATION")
    print("=" * 50)

    print("\nAssignment information is not currently")
    print("provided in the knowledge base.")


# ========================================
# FIND MODULE
# ========================================

def find_module(question):

    syllabus = ai_data["theory_syllabus"]

    for module in syllabus:

        if module.lower() in question:
            return module

    return None


# ========================================
# FIND TOPIC
# ========================================

def find_topic(question):

    syllabus = ai_data["theory_syllabus"]

    for module, details in syllabus.items():

        for topic, points in details["topics"].items():

            if topic.lower() in question:
                return module, topic, points

            for point in points:

                if point.lower() in question:
                    return module, topic, points

    return None


# ========================================
# ASK QUESTION
# ========================================

def ask_question():

    print("\n" + "=" * 50)
    print("❓ ASK A QUESTION")
    print("=" * 50)

    question = input("\nYou: ").lower().strip()

    # Empty input
    if not question:
        print("StudyBot: Please enter a question.")
        return

    # ------------------------------------
    # GREETING
    # ------------------------------------

    if question in ["hi", "hello", "hey", "hii"]:
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
        or "which subject" in question
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
        "exam" in question
        and (
            "when" in question
            or "date" in question
        )
    ):

        print(
            f"StudyBot: Your theory exam is on "
            f"{ai_data['exam_details']['theory_exam']['date']}."
        )
        return

    # ------------------------------------
    # MARKS / EVALUATION
    # ------------------------------------

    if (
        "marks" in question
        or "evaluation" in question
        or "cia" in question
        or "mid semester" in question
        or "end semester" in question
    ):

        exam = ai_data["exam_details"]

        print("\nStudyBot: Evaluation Scheme")

        print(
            f"   CIA Total: "
            f"{exam['CIA']['Total']} marks"
        )

        print(
            f"   Mid Semester Examination: "
            f"{exam['mid_semester_examination']['marks']} marks"
        )

        print(
            f"   End Semester Examination: "
            f"{exam['end_semester_examination']['marks']} marks"
        )

        return

    # ------------------------------------
    # PRACTICAL
    # ------------------------------------

    if "practical" in question or "lab" in question:

        print(
            f"StudyBot: "
            f"{ai_data['practical_syllabus']['status']}."
        )
        return

    # ------------------------------------
    # ASSIGNMENT
    # ------------------------------------

    if "assignment" in question:

        print(
            "StudyBot: Assignment information is "
            "not currently provided in the knowledge base."
        )
        return

    # ------------------------------------
    # MODULE NAME
    # ------------------------------------

    module = find_module(question)

    if module:

        syllabus = ai_data["theory_syllabus"]

        # If user asks what a module is about
        if (
            "name" in question
            or "title" in question
            or "about" in question
            or "topic" in question
        ):

            print(
                f"StudyBot: {module} is "
                f"'{syllabus[module]['title']}'."
            )

            return

    # ------------------------------------
    # COMPLETE MODULE DETAILS
    # ------------------------------------

    if module:

        syllabus = ai_data["theory_syllabus"]

        print(
            f"\nStudyBot: {module} - "
            f"{syllabus[module]['title']}"
        )

        for topic, points in syllabus[module]["topics"].items():

            print(f"\n{topic}")

            for point in points:
                print(f"   • {point}")

        return

    # ------------------------------------
    # SPECIFIC TOPIC
    # ------------------------------------

    topic_result = find_topic(question)

    if topic_result:

        module, topic, points = topic_result

        print(
            f"\nStudyBot: {topic}"
        )

        for point in points:
            print(f"   • {point}")

        return

    # ------------------------------------
    # SYLLABUS GENERAL QUESTION
    # ------------------------------------

    if (
        "syllabus" in question
        or "modules" in question
    ):

        print(
            "StudyBot: We have 6 theory modules."
        )

        for module, details in ai_data["theory_syllabus"].items():

            print(
                f"   • {module}: "
                f"{details['title']}"
            )

        return

    # ------------------------------------
    # UNKNOWN QUESTION
    # ------------------------------------

    print(
        "StudyBot: Sorry, I don't understand "
        "that question yet."
    )

    print(
        "You can ask about the course code, "
        "exam, marks, syllabus, modules, "
        "practicals, or assignments."
    )


# ========================================
# MAIN PROGRAM
# ========================================

def main():

    show_header()

    while True:

        show_menu()

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":

            ask_question()

        elif choice == "2":

            view_syllabus()

        elif choice == "3":

            view_exams()

        elif choice == "4":

            view_practicals()

        elif choice == "5":

            view_assignments()

        elif choice == "6":

            print(
                "\nStudyBot: Goodbye! "
                "Good luck with your studies! 📚"
            )

            break

        else:

            print(
                "\nStudyBot: Invalid choice. "
                "Please enter a number from 1 to 6."
            )


# ========================================
# RUN PROGRAM
# ========================================

if __name__ == "__main__":
    main()