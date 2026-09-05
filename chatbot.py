# ========================================
# STUDYBOT - CHATBOT
# Person 2: Chatbot / User Interaction
# ========================================

from data import subjects


def show_header():
    print("\n" + "=" * 45)
    print("🤖 STUDYBOT")
    print("     Academic Assistant")
    print("=" * 45)


def show_menu():
    print("\nWhat would you like to do?")
    print("1. Ask a question")
    print("2. View syllabus")
    print("3. View exams")
    print("4. View practicals")
    print("5. View assignments")
    print("6. Exit")


def view_syllabus():
    ai_data = subjects["AI"]
    syllabus = ai_data["syllabus"]

    print("\n" + "=" * 45)
    print("📚 ARTIFICIAL INTELLIGENCE SYLLABUS")
    print("=" * 45)

    for module, details in syllabus.items():
        print(f"\n{module}: {details['title']}")
        print("-" * 45)

        for topic, points in details["topics"].items():
            print(f"\n{topic}")

            for point in points:
                print(f"  • {point}")

        print(f"\nStatus: {details['status']}")


def view_exams():
    ai_data = subjects["AI"]

    print("\n" + "=" * 45)
    print("📝 EXAM INFORMATION")
    print("=" * 45)

    print(f"Course: {ai_data['course_name']}")
    print(f"Course Code: {ai_data['course_code']}")
    print(f"Exam Date: {ai_data['exam']['date']}")

    print("\nEvaluation Scheme:")
    print(f"  CIA Activity: {ai_data['evaluation']['CIA']['Activity']} marks")
    print(f"  CIA Test: {ai_data['evaluation']['CIA']['Test']} marks")
    print(f"  CIA Attendance: {ai_data['evaluation']['CIA']['Attendance']} marks")
    print(f"  CIA Total: {ai_data['evaluation']['CIA']['Total']} marks")
    print(f"  Mid Semester Examination: "
          f"{ai_data['evaluation']['Mid Semester Examination']} marks")
    print(f"  End Semester Examination: "
          f"{ai_data['evaluation']['End Semester Examination']} marks")


def view_practicals():
    ai_data = subjects["AI"]

    print("\n" + "=" * 45)
    print("🔬 PRACTICAL INFORMATION")
    print("=" * 45)

    print(ai_data["practicals"]["status"])


def view_assignments():
    ai_data = subjects["AI"]

    print("\n" + "=" * 45)
    print("📋 ASSIGNMENT INFORMATION")
    print("=" * 45)

    print(ai_data["assignments"]["status"])


def ask_question():
    print("\n" + "=" * 45)
    print("❓ ASK A QUESTION")
    print("=" * 45)

    question = input("You: ").lower().strip()

    ai_data = subjects["AI"]

    # Course information
    if "course code" in question:
        print(f"StudyBot: The course code is {ai_data['course_code']}.")

    elif "course name" in question or "subject name" in question:
        print(f"StudyBot: The course is {ai_data['course_name']}.")

    # Exam information
    elif "exam" in question or "examination" in question:
        print(
            f"StudyBot: The exam date is {ai_data['exam']['date']}."
        )

    # Syllabus information
    elif "syllabus" in question or "module" in question:
        print("StudyBot: You can select option 2 to view the complete syllabus.")

    # Practical information
    elif "practical" in question:
        print(
            f"StudyBot: {ai_data['practicals']['status']}."
        )

    # Assignment information
    elif "assignment" in question:
        print(
            f"StudyBot: {ai_data['assignments']['status']}."
        )

    # Evaluation information
    elif "marks" in question or "evaluation" in question:
        print("\nStudyBot: Evaluation Scheme")
        print(
            f"CIA: {ai_data['evaluation']['CIA']['Total']} marks"
        )
        print(
            f"Mid Semester: "
            f"{ai_data['evaluation']['Mid Semester Examination']} marks"
        )
        print(
            f"End Semester: "
            f"{ai_data['evaluation']['End Semester Examination']} marks"
        )

    else:
        print(
            "StudyBot: Sorry, I don't understand that question yet."
        )
        print(
            "Try asking about the course code, exam, syllabus, "
            "practicals, assignments, or marks."
        )


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
            print("\nStudyBot: Goodbye! 👋")
            break

        else:
            print("\nStudyBot: Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()