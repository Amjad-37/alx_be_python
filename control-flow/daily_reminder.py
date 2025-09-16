#!/usr/bin/python3
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print(f"Reminder: {reminder}")
else:
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
        print(f"Note: {reminder}")
    else:
        # A general note for non-time-bound high/medium tasks
        reminder += ". Try to complete it today."
        print(f"Note: {reminder}")
