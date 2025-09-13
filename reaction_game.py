import time
import random
from utils import clear_screen

def play_reaction(trials=5):
    
    print('Reaction Time Game — press Enter to begin.')
    input('Ready? Press Enter to start...')
    results = []
    for i in range(trials):
        clear_screen()
        print(f'Trial {i+1} of {trials}. Get ready...')
        wait = random.uniform(1.0, 3.0)
        time.sleep(wait)
        print('\nGO! — press Enter NOW!')
        t0 = time.perf_counter()
        input()
        t1 = time.perf_counter()
        dt = t1 - t0
        print(f'Your reaction: {dt:.3f} seconds')
        results.append(dt)
        time.sleep(1.0)

    avg = sum(results) / len(results) if results else None
    summary = {
        'avg_reaction': avg,
        'trials': len(results),
        'best_reaction': min(results) if results else None
    }
    print('\nSession Summary:')
    print(f"Average reaction: {summary['avg_reaction']:.3f} s")
    print(f"Best reaction: {summary['best_reaction']:.3f} s")
    return summary