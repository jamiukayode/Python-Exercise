import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

# Set the countdown time in seconds
countdown_time = 5  # 10 seconds countdown
countdown_timer(countdown_time)
