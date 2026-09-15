import time

def digital_clock():
    """Displays the current time in HH:MM:SS format."""
    
    try:
        while True:
            current_time = time.strftime("%H:%M:%S")
            print(f"\rCurrent TIme: {current_time}", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped.")
        
        
print("Digital Clock Started. Press Ctrl+C to stop.")

digital_clock()