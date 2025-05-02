import time
import sys
import os

def clear():
    # Clear screen for Windows or Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def birthday_surprise():
    clear()
    print("Let's create a birthday surprise!")
    name = input("Enter your friend's name: ").strip()

    clear()
    print("Preparing surprise...")
    time.sleep(2)

    clear()
    slow_print("3...", 0.5)
    time.sleep(1)
    slow_print("2...", 0.5)
    time.sleep(1)
    slow_print("1...", 0.5)
    time.sleep(1)

    clear()
    slow_print(f"🎉🎂 Happy Birthday, {name} Bhaiya! 🎂🎉", 0.1)
    time.sleep(1)
    slow_print("Wishing you a day filled with love, laughter, and cake! 🍰🥳", 0.08)
    slow_print("Have an amazing year ahead! 🚀✨", 0.08)

if __name__ == "__main__":
    birthday_surprise()