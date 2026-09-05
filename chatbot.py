# ========================================
# STUDYBOT - CHATBOT
# Person 2: Chatbot / User Interaction
# ========================================

from data import subjects

from rules import (
    answer_question,
    get_theory_syllabus,
    get_exams,
    get_practical_syllabus,
)


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
# MENU
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

    print(get_theory_syllabus())


# ========================================
# OPTION 3 - VIEW EXAMS
# ========================================

def view_exams():

    print(get_exams())


# ========================================
# OPTION 4 - VIEW PRACTICALS
# ========================================

def view_practicals():

    print(get_practical_syllabus())


# ========================================
# OPTION 5 - VIEW ASSIGNMENTS
# ========================================

def view_assignments():

    print("\n" + "=" * 50)
    print("              📋 ASSIGNMENTS")
    print("=" * 50)

    print(
        f"\nStatus: "
        f"{ai_data['assignments']['status']}"
    )


# ========================================
# OPTION 1 - ASK QUESTION
# ========================================

def ask_question():

    print("\n" + "=" * 50)
    print("                 ❓ ASK A QUESTION")
    print("=" * 50)

    question = input("\nYou: ").strip()

    response = answer_question(question)

    print("\nStudyBot:", response)


# ========================================
# MAIN PROGRAM
# ========================================

def main():

    show_header()

    while True:

        show_menu()

        choice = input(
            "\nEnter your choice (1-6): "
        ).strip()

        # --------------------------------
        # ASK QUESTION
        # --------------------------------

        if choice == "1":

            ask_question()

        # --------------------------------
        # VIEW SYLLABUS
        # --------------------------------

        elif choice == "2":

            view_syllabus()

        # --------------------------------
        # VIEW EXAMS
        # --------------------------------

        elif choice == "3":

            view_exams()

        # --------------------------------
        # VIEW PRACTICALS
        # --------------------------------

        elif choice == "4":

            view_practicals()

        # --------------------------------
        # VIEW ASSIGNMENTS
        # --------------------------------

        elif choice == "5":

            view_assignments()

        # --------------------------------
        # EXIT
        # --------------------------------

        elif choice == "6":

            print(
                "\nStudyBot: Goodbye! "
                "Good luck with your studies! 📚"
            )

            break

        # --------------------------------
        # INVALID CHOICE
        # --------------------------------

        else:

            print(
                "\nStudyBot: Please enter a number "
                "from 1 to 6."
            )


# ========================================
# START
# ========================================

if __name__ == "__main__":
    main()