import pyautogui
import time
import random
import msvcrt


def user_exit():
    """Check if the user has pressed 'q' to exit the program."""
    return msvcrt.kbhit() and msvcrt.getch().decode(errors="ignore").lower() == "q"


def generate_positions():
    """Generate a list of random positions in the center of the screen."""
    screen_width, screen_height = pyautogui.size()

    min_width = int(screen_width * 0.45)
    max_width = int(screen_width * 0.55)
    min_height = int(screen_height * 0.45)
    max_height = int(screen_height * 0.55)

    return [
        (random.randint(min_width, max_width), random.randint(min_height, max_height))
        for _ in range(100)
    ]


def activate_mouse():
    """Moves the mouse to random positions at random intervals and clicks once, while checking for user exit."""
    positions = generate_positions()

    try:
        while True:
            if user_exit():
                return

            pyautogui.moveTo(*random.choice(positions), duration=0.2)
            # TODO make sure not to click something clickable
            time.sleep(0.3)
            pyautogui.click()

            wait_time = random.randint(5, 30)
            start_time = time.time()
            while time.time() - start_time < wait_time:
                if user_exit():
                    return
                time.sleep(0.3)

    except KeyboardInterrupt:
        print("Received Ctrl-C ...")


if __name__ == "__main__":
    activate_mouse()
