def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
            if time_bound == "yes":
                print(f"Reminder: {reminder} that requires immediate attention today!")
            else:
                print(f"Reminder: {reminder}")
        case "medium":
            reminder = f"'{task}' is a medium priority task"
            if time_bound == "yes":
                print(f"Reminder: {reminder} that requires immediate attention today!")
            else:
                print(f"Reminder: {reminder}")
        case "low":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority level.")
            return

if __name__ == "__main__":
    main()
