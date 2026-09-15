import time

print("Welcome to CountDown Timer")

try:
    seconds = int(input("Enter time is seconds: "))
    if seconds < 0:
        print("Please enter a positive number.")
    else:
        print("Countdown Started...")
        while seconds >= 0:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(timer, end="\r")
            time.sleep(1)
            seconds -= 1
        print("00:00")
        print("⏱️ Time's up! 🎉")

except ValueError:
    print("Please enter a valid number.")