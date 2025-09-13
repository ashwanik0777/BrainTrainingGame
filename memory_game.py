import random
import time
from utils import clear_screen

def play_memory(show_time=3.0):
    
    level = 1
    correct = 0
    max_level = 0

    while True:
        length = level + 2 
        number = ''.join(str(random.randint(0,9)) for _ in range(length))
        clear_screen()
        print(f"Level {level} — Remember this number:")
        print("\n" + number + "\n")
        time.sleep(show_time)
        clear_screen()
        answer = input("Enter the number (or type 'q' to stop): ").strip()
        if answer.lower() == 'q':
            break
        if answer == number:
            print("Correct! ✅")
            correct += 1
            max_level = max(max_level, level)
            level += 1
            show_time = max(0.8, show_time - 0.15)
        else:
            print(f"Wrong. The correct number was: {number}")
            break
        time.sleep(1.0)

    summary = {
        'score': correct,
        'levels_reached': max_level,
    }
    print('\nSession Summary:')
    print(f"Score (correct rounds): {summary['score']}")
    print(f"Levels reached: {summary['levels_reached']}")
    return summary