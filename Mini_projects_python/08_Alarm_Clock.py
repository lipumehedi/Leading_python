from datetime import datetime
import time

print("⏰ Welcome to Alarm Clock⏰")
alarm_time = input("Enter alarm time (HH:MM:SS in 24-hour format): ")
print(f"Alarm set for {alarm_time}")

while True:
    now = datetime.now().strftime("%H:%M:%S")
    print(f"Current Time: {now}", end="\r")
    
    if now == alarm_time:
        print("\n⏰ Time to Wake up! ⏰")
        print("Alarm! Alarm! Alram!")
        break
    
    time.sleep(1)
    
print("Alarm Stooped. Have a Great Day! 😊")
