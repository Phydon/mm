import pyautogui
import time
import random
import msvcrt

def user_exit():
    """Check if the user has pressed 'q' to exit the program."""
    return msvcrt.kbhit() and msvcrt.getch().decode(errors='ignore').lower() == 'q'

def generate_positions(screen_width, screen_height, count=3):
    """Generate a list of random screen positions."""
    return [(random.randint(10, screen_width - 10), random.randint(10, screen_height - 10)) for _ in range(count)]

def move_mouse():
    """Moves the mouse to random positions at random intervals, checking for user exit."""
    screen_width, screen_height = pyautogui.size()
    positions = generate_positions(screen_width, screen_height)
    
    try:
        while True:
            if user_exit():
                print("\nExiting program...")
                return
            
            pyautogui.moveTo(*random.choice(positions), duration=0.2)
            wait_time = random.randint(5, 30)  # Random wait time between 1 and 30 seconds
            start_time = time.time()
            while time.time() - start_time < wait_time:
                if user_exit():
                    print("\nExiting program...")
                    return
                time.sleep(0.3)  # Check user input more frequently
    except KeyboardInterrupt:
        print("\nExiting program...")

if __name__ == "__main__":
    move_mouse()
