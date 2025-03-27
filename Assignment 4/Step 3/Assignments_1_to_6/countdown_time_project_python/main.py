import time  # Importing time module to use the sleep function

def countdown_timer(seconds):
    """This function runs a simple countdown timer."""
    while seconds > 0:  # Loop will run until seconds become zero
        mins, secs = divmod(seconds, 60)  # Convert total seconds into minutes and seconds
        timer = f"{mins:02d}:{secs:02d}"  # Format the timer as MM:SS
        print(timer, end="\r")  # Print on the same line (overwrite previous time)
        time.sleep(1)  # Wait for 1 second
        seconds -= 1  # Decrease time by 1 second

    print("⏰ Time's up!")  # Print message when countdown is finished

# Taking user input for countdown time (in seconds)
seconds = int(input("⏳ Enter time in seconds: "))
countdown_timer(seconds)  # Calling the function
