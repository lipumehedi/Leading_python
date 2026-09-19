from datetime import datetime, timedelta

tasks = []

print("\nSMART SCHEDULING SYSTEM")
print("=" * 45)

while True:
    start = input("Start time (HH:MM): ").strip()

    try:
        current_time = datetime.strptime(start, "%H:%M")
        break
    except ValueError:
        print("Use 24-hour format, e.g. 09:30.")

while True:
    task = input("\nTask name (or 'done'): ").strip()

    if task.lower() == "done":
        break

    if not task:
        print("Task name cannot be empty.")
        continue

    while True:
        duration_input = input("Duration (minutes): ").strip()

        try:
            duration = int(duration_input)

            if duration <= 0:
                print("Duration must be greater than 0.")
                continue

            break

        except ValueError:
            print("Enter duration as a whole number.")

    tasks.append((task, duration))

if not tasks:
    print("\nNO tasks entered.")

else:
    print("\nYOUR SMART SCHEDULE")
    print("=" * 55)

    total_minutes = 0

    for task, duration in tasks:
        end_time = current_time + timedelta(minutes=duration)

        start_text = current_time.strftime("%I:%M %p")
        end_text = end_time.strftime("%I:%M %p")

        print(f"{start_text} - {end_text} | {task}")

        current_time = end_time
        total_minutes += duration

    hours, minutes = divmod(total_minutes, 60)

    print("-" * 55)
    print(f"Total scheduled time: {hours}h {minutes}m")