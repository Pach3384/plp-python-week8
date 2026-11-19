# Personal Mini-Toolkit
# Brings together variables, input/output, conditionals, loops, lists, and f-strings.


# Tool 1: Manages a live list of tasks where users can add, view, or remove items during a session.
def task_list_tool(tasks):
    print("\n--- Study & Task List Manager ---")
    while True:
        print("\nTask Options:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task by number")
        print("4. Back to main menu")

        action = input("Choose an option (1-4): ").strip()

        if action == "1":
            if not tasks:
                print("Your task list is currently empty.")
            else:
                print("Your current tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")

        elif action == "2":
            new_task = input("Enter a new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Added '{new_task}'! You now have {len(tasks)} task(s).")
            else:
                print("Task cannot be blank. Nothing was added.")

        elif action == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")
                choice = input("Enter the task number to remove: ").strip()
                if choice.isdigit():
                    task_num = int(choice)
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"Removed '{removed}'. Remaining tasks: {len(tasks)}.")
                    else:
                        print(f"Please enter a number between 1 and {len(tasks)}.")
                else:
                    print("Please enter a valid task number.")

        elif action == "4":
            print("Returning to the main menu...")
            break

        else:
            print(f"'{action}' is not a valid option. Please pick 1 to 4.")


# Tool 2: Evaluates a numeric score (0-100) using conditionals and returns a grade and feedback.
def score_evaluator_tool():
    print("\n--- Score & Grade Evaluator ---")
    raw_score = input("Enter a score from 0 to 100: ").strip()

    try:
        score = float(raw_score)
    except ValueError:
        print(f"'{raw_score}' is not a valid number. Please try again.")
        return

    if score < 0 or score > 100:
        print(f"Score {score} is out of range. Please enter a value between 0 and 100.")
        return

    if score >= 80:
        grade = "A"
        remark = "Excellent work!"
    elif score >= 70:
        grade = "B"
        remark = "Great job, keep pushing!"
    elif score >= 60:
        grade = "C"
        remark = "Solid progress."
    elif score >= 50:
        grade = "D"
        remark = "Pass — room to grow with extra practice."
    else:
        grade = "E"
        remark = "Below pass mark — review the topic and try again."

    print(f"Score: {score} | Grade: {grade} — {remark}")


# Tool 3: Counts down from a chosen starting number using a loop and displays a friendly finish message.
def countdown_tool():
    print("\n--- Countdown Helper ---")
    raw_start = input("Enter a positive starting number (e.g., 5): ").strip()

    if not raw_start.isdigit():
        print(f"'{raw_start}' is not a positive whole number.")
        return

    start_num = int(raw_start)
    if start_num <= 0:
        print("Please enter a number greater than 0.")
        return

    print(f"Starting countdown from {start_num}...")
    current = start_num
    while current >= 1:
        print(f"  {current}...")
        current -= 1

    print(f"Countdown from {start_num} complete! Ready to go.")


def show_menu():
    print("\n=== Personal Mini-Toolkit ===")
    print("1. Study & Task List Manager")
    print("2. Score & Grade Evaluator")
    print("3. Countdown Helper")
    print("4. Quit")


def main():
    print("Welcome to the Personal Mini-Toolkit! Let's get things done.")
    session_tasks = []

    while True:
        show_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            task_list_tool(session_tasks)
        elif choice == "2":
            score_evaluator_tool()
        elif choice == "3":
            countdown_tool()
        elif choice == "4":
            print("Thanks for using the Personal Mini-Toolkit. Goodbye and have a great day!")
            break
        else:
            print(f"'{choice}' is not on the menu. Please choose a number from 1 to 4.")


if __name__ == "__main__":
    main()
