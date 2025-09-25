def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            print("Invalid priority level.")
            return

    if priority in ["high", "medium"] and time_bound == "yes":
        reminder += " that requires immediate attention today!"

    print(reminder)

if __name__ == "__main__":
    main()
